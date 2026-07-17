"""
AXI Platform Runtime

Engine Registry

Registry of AXI runtime engines.
"""

from __future__ import annotations

from collections.abc import Iterable

from Runtime.ApplicationRegistry import ApplicationRegistry
from Runtime.CapabilityRegistry import CapabilityRegistry
from Runtime.DependencyResolver import Dependency, DependencyResolver
from Runtime.EngineRegistry.engine import Engine
from Runtime.EngineRegistry.lifecycle import transition_lifecycle
from Runtime.EventBus import Event, EventBus
from Runtime.ObjectModel.platform_object import PlatformObject
from Runtime.ObjectRegistry import ObjectRegistry
from Runtime.PluginLoader import PluginLoader
from Runtime.Registry import BaseRegistry
from Runtime.ServiceRegistry import ServiceRegistry
from Runtime.Validation import ValidationResult, Validator
from Runtime.exceptions import (
    CapabilityNotFoundError,
    ObjectNotFoundError,
    RegistryError,
)


class _EngineDependencyResolver(DependencyResolver):
    """
    Registry-local dependency resolver that accepts managed engine IDs.
    """

    def __init__(
        self,
        *,
        engine_ids: Iterable[str],
        application_registry: ApplicationRegistry | None = None,
        object_registry: ObjectRegistry | None = None,
        capability_registry: CapabilityRegistry | None = None,
        service_registry: ServiceRegistry | None = None,
    ) -> None:
        super().__init__(
            object_registry=object_registry,
            capability_registry=capability_registry,
            service_registry=service_registry,
        )
        self._engine_ids = set(engine_ids)
        self._application_registry = application_registry

    def _identifier_exists(self, identifier: str) -> bool:
        """
        Resolve identifiers from registry-managed engines first.
        """
        return (
            identifier in self._engine_ids
            or (
                self._application_registry is not None
                and self._application_registry.exists(identifier)
            )
            or super()._identifier_exists(identifier)
        )


class EngineRegistry(BaseRegistry[Engine]):
    """
    Registry of engines keyed by engine identifier.
    """

    def __init__(
        self,
        *,
        object_registry: ObjectRegistry | None = None,
        capability_registry: CapabilityRegistry | None = None,
        service_registry: ServiceRegistry | None = None,
        plugin_loader: PluginLoader | None = None,
        application_registry: ApplicationRegistry | None = None,
        event_bus: EventBus | None = None,
        validator: Validator | None = None,
    ) -> None:
        """
        Initialize the engine registry.
        """
        super().__init__()
        self._object_registry = object_registry
        self._capability_registry = capability_registry
        self._service_registry = service_registry
        self._plugin_loader = plugin_loader
        self._application_registry = application_registry
        self._event_bus = event_bus
        self._validator = validator or Validator(
            object_registry=object_registry,
            capability_registry=capability_registry,
            service_registry=service_registry,
            event_bus=event_bus,
        )

    def register(self, engine: Engine) -> None:
        """
        Register an engine using its engine identifier.
        """
        self._validate_engine(engine)
        super().register(engine.engine_id, engine)
        self._register_capability_implementations(engine)
        self._publish_event("engine.registered", engine)

    def register_engine(self, engine: Engine) -> None:
        """
        Register an engine.
        """
        self.register(engine)

    def unregister(self, engine_id: str) -> None:
        """
        Remove an engine by identifier.
        """
        engine = self.get(engine_id)

        if engine is None:
            return

        self._clear_capability_implementations(engine_id)
        super().unregister(engine_id)
        self._publish_event("engine.unregistered", engine)

    def unregister_engine(self, engine_id: str) -> None:
        """
        Remove an engine by identifier.
        """
        self.unregister(engine_id)

    def lookup_engine(self, engine_id: str) -> Engine | None:
        """
        Return a registered engine without mutating registry state.
        """
        return self.get(engine_id)

    def list_engines(self) -> list[Engine]:
        """
        Return engines in deterministic identifier order.
        """
        return [
            self._require_engine(engine_id)
            for engine_id in self.keys()
        ]

    def update(self, engine: Engine) -> None:
        """
        Replace an existing engine definition.
        """
        self._validate_engine(engine)
        self._require_engine(engine.engine_id)
        self._clear_capability_implementations(engine.engine_id)
        super().update(engine.engine_id, engine)
        self._register_capability_implementations(engine)
        self._publish_event("engine.updated", engine)

    def update_engine(self, engine: Engine) -> None:
        """
        Replace an existing engine definition.
        """
        self.update(engine)

    def start_engine(self, engine_id: str) -> Engine:
        """
        Transition an engine to its started state.
        """
        engine = self._require_engine(engine_id)
        engine.lifecycle_state = transition_lifecycle(
            engine.lifecycle_state,
            "start",
        )
        self._publish_event("engine.started", engine)
        return engine

    def stop_engine(self, engine_id: str) -> Engine:
        """
        Transition an engine to its stopped state.
        """
        engine = self._require_engine(engine_id)
        engine.lifecycle_state = transition_lifecycle(
            engine.lifecycle_state,
            "stop",
        )
        self._publish_event("engine.stopped", engine)
        return engine

    def restart_engine(self, engine_id: str) -> Engine:
        """
        Transition an engine through its restart boundary.
        """
        engine = self._require_engine(engine_id)
        engine.lifecycle_state = transition_lifecycle(
            engine.lifecycle_state,
            "restart",
        )
        self._publish_event("engine.restarted", engine)
        return engine

    def _require_engine(self, engine_id: str) -> Engine:
        """
        Resolve a registered engine.
        """
        engine = self.get(engine_id)

        if engine is None:
            raise ObjectNotFoundError(
                f"Engine not found: '{engine_id}'"
            )

        return engine

    def _validate_engine(self, engine: Engine) -> None:
        """
        Validate an engine before registration or update.
        """
        if not isinstance(engine, Engine):
            raise RegistryError(
                "Invalid engine registration: expected Engine"
            )

        if engine.namespace != "AXI-ENG":
            raise RegistryError(
                "Invalid engine namespace: expected 'AXI-ENG'"
            )

        if engine.object_type != "Engine":
            raise RegistryError(
                "Invalid engine object_type: expected 'Engine'"
            )

        if not engine.metadata:
            raise RegistryError(
                "Invalid engine metadata: metadata is required"
            )

        if not engine.lifecycle_state:
            raise RegistryError(
                "Invalid engine metadata: lifecycle_state is required"
            )

        self._validate_capabilities(engine)
        self._raise_for_invalid_results(
            engine.engine_id,
            self._validation_results(engine),
        )
        self._build_dependency_resolver(engine)

    def _validate_capabilities(self, engine: Engine) -> None:
        """
        Validate declared engine capabilities.
        """
        if self._capability_registry is None:
            return

        for capability_id in engine.capabilities:
            if not self._capability_registry.exists(capability_id):
                raise CapabilityNotFoundError(
                    f"Capability not found: '{capability_id}'"
                )

    def _validation_results(
        self,
        engine: Engine,
    ) -> list[ValidationResult]:
        """
        Collect validation results for an engine input.
        """
        results = self._validator.validate_schema(
            PlatformObject.to_dict(engine),
            "AXI-SCH-007",
        )
        results.extend(
            self._validator.validate_metadata(
                engine.metadata,
                source=engine.engine_id,
            )
        )
        results.extend(
            self._validator.validate_schema(
                self._schema_payload(engine),
                "AXI-SCH-011",
            )
        )
        return results

    @staticmethod
    def _schema_payload(engine: Engine) -> dict[str, object]:
        """
        Build the published M15 schema payload for an engine.
        """
        return {
            "engine_id": engine.engine_id,
            "name": engine.name,
            "version": engine.version,
            "description": engine.description,
            "owner": engine.owner,
            "capabilities": list(engine.capabilities),
            "dependencies": list(engine.dependencies),
            "lifecycle_state": engine.lifecycle_state,
            "status": engine.status,
            "metadata": dict(engine.metadata),
        }

    @staticmethod
    def _raise_for_invalid_results(
        engine_id: str,
        results: list[ValidationResult],
    ) -> None:
        """
        Raise a registry error when validation results contain failures.
        """
        invalid_results = [
            result for result in results if result.status == "invalid"
        ]

        if not invalid_results:
            return

        messages = "; ".join(
            f"{result.rule_id}: {result.message}"
            for result in invalid_results
        )
        raise RegistryError(
            f"Engine '{engine_id}' failed validation: {messages}"
        )

    def _build_dependency_resolver(
        self,
        engine: Engine,
    ) -> DependencyResolver:
        """
        Build and validate the engine dependency graph.
        """
        engines = {
            existing.engine_id: existing
            for existing in self.list_engines()
        }
        engines[engine.engine_id] = engine

        resolver = _EngineDependencyResolver(
            engine_ids=engines.keys(),
            application_registry=self._application_registry,
            object_registry=self._object_registry,
            capability_registry=self._capability_registry,
            service_registry=self._service_registry,
        )

        for candidate in engines.values():
            for dependency_id in candidate.dependencies:
                resolver.register_dependency(
                    Dependency(candidate.engine_id, dependency_id)
                )

        return resolver

    def _register_capability_implementations(
        self,
        engine: Engine,
    ) -> None:
        """
        Associate an engine to its declared capabilities.
        """
        if self._capability_registry is None:
            return

        for capability_id in engine.capabilities:
            self._capability_registry.add_implementation(
                capability_id,
                engine,
            )

    def _clear_capability_implementations(self, engine_id: str) -> None:
        """
        Remove an engine from every capability implementation set.
        """
        if self._capability_registry is None:
            return

        for capability in self._capability_registry:
            capability.remove_object(engine_id)

    def _publish_event(
        self,
        event_type: str,
        engine: Engine,
    ) -> None:
        """
        Publish an engine lifecycle event when an event bus exists.
        """
        if self._event_bus is None:
            return

        payload: dict[str, object] = {
            "engine_id": engine.engine_id,
            "name": engine.name,
            "version": engine.version,
            "status": engine.status,
            "lifecycle_state": engine.lifecycle_state,
            "capabilities": tuple(engine.capabilities),
            "dependencies": tuple(engine.dependencies),
        }

        if self._plugin_loader is not None:
            payload["loaded_plugins"] = tuple(
                plugin.plugin_id
                for plugin in self._plugin_loader.list_plugins()
            )

        if self._application_registry is not None:
            payload["registered_applications"] = tuple(
                application.application_id
                for application in self._application_registry.list_applications()
            )

        self._event_bus.publish(
            Event(
                event_type=event_type,
                source="Runtime.EngineRegistry",
                payload=payload,
            )
        )
