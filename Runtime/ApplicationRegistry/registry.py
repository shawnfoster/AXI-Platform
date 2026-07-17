"""
AXI Platform Runtime

Application Registry

Registry of AXI runtime applications.
"""

from __future__ import annotations

from collections.abc import Iterable

from Runtime.ApplicationRegistry.application import Application
from Runtime.ApplicationRegistry.lifecycle import transition_lifecycle
from Runtime.CapabilityRegistry import CapabilityRegistry
from Runtime.DependencyResolver import Dependency, DependencyResolver
from Runtime.EventBus import Event, EventBus
from Runtime.ObjectModel.platform_object import PlatformObject
from Runtime.ObjectRegistry import ObjectRegistry
from Runtime.PluginLoader import PluginLoader
from Runtime.Registry import BaseRegistry
from Runtime.ServiceRegistry import ServiceRegistry
from Runtime.Validation import ValidationResult, Validator
from Runtime.exceptions import (
    CapabilityNotFoundError,
    DependencyError,
    ObjectNotFoundError,
    RegistryError,
)


class _ApplicationDependencyResolver(DependencyResolver):
    """
    Registry-local dependency resolver that accepts managed application IDs.
    """

    def __init__(
        self,
        *,
        application_ids: Iterable[str],
        object_registry: ObjectRegistry | None = None,
        capability_registry: CapabilityRegistry | None = None,
        service_registry: ServiceRegistry | None = None,
    ) -> None:
        super().__init__(
            object_registry=object_registry,
            capability_registry=capability_registry,
            service_registry=service_registry,
        )
        self._application_ids = set(application_ids)

    def _identifier_exists(self, identifier: str) -> bool:
        """
        Resolve identifiers from registry-managed applications first.
        """
        return (
            identifier in self._application_ids
            or super()._identifier_exists(identifier)
        )


class ApplicationRegistry(BaseRegistry[Application]):
    """
    Registry of applications keyed by application identifier.
    """

    def __init__(
        self,
        *,
        object_registry: ObjectRegistry | None = None,
        capability_registry: CapabilityRegistry | None = None,
        service_registry: ServiceRegistry | None = None,
        plugin_loader: PluginLoader | None = None,
        event_bus: EventBus | None = None,
        validator: Validator | None = None,
    ) -> None:
        """
        Initialize the application registry.
        """
        super().__init__()
        self._object_registry = object_registry
        self._capability_registry = capability_registry
        self._service_registry = service_registry
        self._plugin_loader = plugin_loader
        self._event_bus = event_bus
        self._validator = validator or Validator(
            object_registry=object_registry,
            capability_registry=capability_registry,
            service_registry=service_registry,
            event_bus=event_bus,
        )

    def register(self, application: Application) -> None:
        """
        Register an application using its application identifier.
        """
        self._validate_application(application)
        super().register(application.application_id, application)
        self._register_capability_implementations(application)
        self._publish_event("application.registered", application)

    def register_application(self, application: Application) -> None:
        """
        Register an application.
        """
        self.register(application)

    def unregister(self, application_id: str) -> None:
        """
        Remove an application by identifier.
        """
        application = self.get(application_id)

        if application is None:
            return

        self._clear_capability_implementations(application_id)
        super().unregister(application_id)
        self._publish_event("application.unregistered", application)

    def unregister_application(self, application_id: str) -> None:
        """
        Remove an application by identifier.
        """
        self.unregister(application_id)

    def lookup_application(self, application_id: str) -> Application | None:
        """
        Return a registered application without mutating registry state.
        """
        return self.get(application_id)

    def list_applications(self) -> list[Application]:
        """
        Return applications in deterministic identifier order.
        """
        return [
            self._require_application(application_id)
            for application_id in self.keys()
        ]

    def update(self, application: Application) -> None:
        """
        Replace an existing application definition.
        """
        self._validate_application(application)
        self._require_application(application.application_id)
        self._clear_capability_implementations(application.application_id)
        super().update(application.application_id, application)
        self._register_capability_implementations(application)
        self._publish_event("application.updated", application)

    def update_application(self, application: Application) -> None:
        """
        Replace an existing application definition.
        """
        self.update(application)

    def start_application(self, application_id: str) -> Application:
        """
        Transition an application to its started state.
        """
        application = self._require_application(application_id)
        application.lifecycle_state = transition_lifecycle(
            application.lifecycle_state,
            "start",
        )
        self._publish_event("application.started", application)
        return application

    def stop_application(self, application_id: str) -> Application:
        """
        Transition an application to its stopped state.
        """
        application = self._require_application(application_id)
        application.lifecycle_state = transition_lifecycle(
            application.lifecycle_state,
            "stop",
        )
        self._publish_event("application.stopped", application)
        return application

    def restart_application(self, application_id: str) -> Application:
        """
        Transition an application through its restart boundary.
        """
        application = self._require_application(application_id)
        application.lifecycle_state = transition_lifecycle(
            application.lifecycle_state,
            "restart",
        )
        self._publish_event("application.restarted", application)
        return application

    def _require_application(self, application_id: str) -> Application:
        """
        Resolve a registered application.
        """
        application = self.get(application_id)

        if application is None:
            raise ObjectNotFoundError(
                f"Application not found: '{application_id}'"
            )

        return application

    def _validate_application(self, application: Application) -> None:
        """
        Validate an application before registration or update.
        """
        if not isinstance(application, Application):
            raise RegistryError(
                "Invalid application registration: expected Application"
            )

        if application.namespace != "AXI-APP":
            raise RegistryError(
                "Invalid application namespace: expected 'AXI-APP'"
            )

        if application.object_type != "Application":
            raise RegistryError(
                "Invalid application object_type: expected 'Application'"
            )

        if not application.metadata:
            raise RegistryError(
                "Invalid application metadata: metadata is required"
            )

        if not application.lifecycle_state:
            raise RegistryError(
                "Invalid application metadata: lifecycle_state is required"
            )

        self._validate_capabilities(application)
        self._raise_for_invalid_results(
            application.application_id,
            self._validation_results(application),
        )
        self._build_dependency_resolver(application)

    def _validate_capabilities(self, application: Application) -> None:
        """
        Validate declared application capabilities.
        """
        if self._capability_registry is None:
            return

        for capability_id in application.capabilities:
            if not self._capability_registry.exists(capability_id):
                raise CapabilityNotFoundError(
                    f"Capability not found: '{capability_id}'"
                )

    def _validation_results(
        self,
        application: Application,
    ) -> list[ValidationResult]:
        """
        Collect validation results for an application input.
        """
        results = self._validator.validate_schema(
            PlatformObject.to_dict(application),
            "AXI-SCH-007",
        )
        results.extend(
            self._validator.validate_metadata(
                application.metadata,
                source=application.application_id,
            )
        )
        results.extend(
            self._validator.validate_schema(
                self._schema_payload(application),
                "AXI-SCH-010",
            )
        )
        return results

    @staticmethod
    def _schema_payload(application: Application) -> dict[str, object]:
        """
        Build the published M14 schema payload for an application.
        """
        return {
            "application_id": application.application_id,
            "name": application.name,
            "version": application.version,
            "description": application.description,
            "owner": application.owner,
            "capabilities": list(application.capabilities),
            "dependencies": list(application.dependencies),
            "services": list(application.services),
            "plugins": list(application.plugins),
            "lifecycle_state": application.lifecycle_state,
            "metadata": dict(application.metadata),
        }

    @staticmethod
    def _raise_for_invalid_results(
        application_id: str,
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
            f"Application '{application_id}' failed validation: {messages}"
        )

    def _build_dependency_resolver(
        self,
        application: Application,
    ) -> DependencyResolver:
        """
        Build and validate the application dependency graph.
        """
        applications = {
            existing.application_id: existing
            for existing in self.list_applications()
        }
        applications[application.application_id] = application

        resolver = _ApplicationDependencyResolver(
            application_ids=applications.keys(),
            object_registry=self._object_registry,
            capability_registry=self._capability_registry,
            service_registry=self._service_registry,
        )

        for candidate in applications.values():
            for dependency_id in candidate.dependencies:
                resolver.register_dependency(
                    Dependency(candidate.application_id, dependency_id)
                )

        return resolver

    def _register_capability_implementations(
        self,
        application: Application,
    ) -> None:
        """
        Associate an application to its declared capabilities.
        """
        if self._capability_registry is None:
            return

        for capability_id in application.capabilities:
            self._capability_registry.add_implementation(
                capability_id,
                application,
            )

    def _clear_capability_implementations(self, application_id: str) -> None:
        """
        Remove an application from every capability implementation set.
        """
        if self._capability_registry is None:
            return

        for capability in self._capability_registry:
            capability.remove_object(application_id)

    def _publish_event(
        self,
        event_type: str,
        application: Application,
    ) -> None:
        """
        Publish an application lifecycle event when an event bus exists.
        """
        if self._event_bus is None:
            return

        payload = {
            "application_id": application.application_id,
            "name": application.name,
            "version": application.version,
            "lifecycle_state": application.lifecycle_state,
            "capabilities": tuple(application.capabilities),
            "dependencies": tuple(application.dependencies),
            "services": tuple(application.services),
            "plugins": tuple(application.plugins),
        }

        if self._plugin_loader is not None:
            payload["loaded_plugins"] = tuple(
                plugin.plugin_id for plugin in self._plugin_loader.list_plugins()
            )

        self._event_bus.publish(
            Event(
                event_type=event_type,
                source="Runtime.ApplicationRegistry",
                payload=payload,
            )
        )
