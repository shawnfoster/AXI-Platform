"""
AXI Platform Runtime

Validation Framework

Centralized validation engine for runtime objects, metadata, schemas,
contracts, dependencies, and runtime foundations.
"""

from __future__ import annotations

import json
import re
from collections.abc import Mapping
from datetime import datetime
from pathlib import Path
from typing import Any

from Runtime.CapabilityRegistry import Capability, CapabilityRegistry
from Runtime.DependencyResolver import DependencyResolver
from Runtime.EventBus import EventBus
from Runtime.ObjectModel import PlatformObject
from Runtime.ObjectRegistry import ObjectRegistry
from Runtime.Registry import BaseRegistry
from Runtime.ServiceRegistry import Service, ServiceRegistry
from Runtime.Validation.result import ValidationResult
from Runtime.Validation.rules import (
    RULE_TARGET_CONTRACT,
    RULE_TARGET_DEPENDENCIES,
    RULE_TARGET_METADATA,
    RULE_TARGET_OBJECT,
    RULE_TARGET_RUNTIME,
    RULE_TARGET_SCHEMA,
    ValidationRule,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
GOVERNANCE_ROOT = REPOSITORY_ROOT / "Governance"
SCHEMA_REGISTRY_PATH = GOVERNANCE_ROOT / "Schemas" / "SCHEMA_REGISTRY.md"
CONTRACT_PATHS = {
    "REGISTER_CONTRACT": GOVERNANCE_ROOT
    / "Contracts"
    / "REGISTER_CONTRACT.md",
    "SERVICE_CONTRACT": GOVERNANCE_ROOT
    / "Contracts"
    / "SERVICE_CONTRACT.md",
    "ENGINE_CONTRACT": GOVERNANCE_ROOT
    / "Contracts"
    / "ENGINE_CONTRACT.md",
}


class Validator:
    """
    Reusable runtime validation engine.
    """

    def __init__(
        self,
        *,
        object_registry: ObjectRegistry | None = None,
        capability_registry: CapabilityRegistry | None = None,
        service_registry: ServiceRegistry | None = None,
        event_bus: EventBus | None = None,
        dependency_resolver: DependencyResolver | None = None,
    ) -> None:
        """Initialize the validation engine."""
        self._object_registry = object_registry
        self._capability_registry = capability_registry
        self._service_registry = service_registry
        self._event_bus = event_bus
        self._dependency_resolver = dependency_resolver
        self._rules = BaseRegistry[ValidationRule]()
        self._published_schemas = self._load_published_schemas()
        self._published_contracts = self._load_published_contracts()
        self._schema_cache: dict[str, dict[str, Any]] = {}
        self._register_builtin_rules()

    def register_rule(self, rule: ValidationRule) -> None:
        """
        Register a reusable validation rule.
        """
        self._rules.register(rule.rule_id, rule)

    def enable_rule(self, rule_id: str) -> None:
        """
        Enable a validation rule.
        """
        self._require_rule(rule_id).enabled = True

    def disable_rule(self, rule_id: str) -> None:
        """
        Disable a validation rule.
        """
        self._require_rule(rule_id).enabled = False

    def validate(self, target: object) -> list[ValidationResult]:
        """
        Validate a target using the most specific published behavior.
        """
        if isinstance(target, PlatformObject):
            return self.validate_object(target)

        if isinstance(target, Capability):
            return self.validate_schema(target)

        if isinstance(target, Mapping):
            return self.validate_metadata(target)

        if isinstance(target, ServiceRegistry):
            return self.validate_contract(target, "SERVICE_CONTRACT")

        if isinstance(target, BaseRegistry):
            return self.validate_contract(target, "REGISTER_CONTRACT")

        if isinstance(target, DependencyResolver):
            return self.validate_dependencies(target)

        if isinstance(target, EventBus):
            return self.validate_runtime(event_bus=target)

        return [
            self._invalid_result(
                "validation.target.unsupported",
                (
                    "Unsupported validation target: "
                    f"{target.__class__.__name__}"
                ),
                self._source_name(target),
            )
        ]

    def validate_object(
        self,
        obj: object,
        *,
        capability_registry: CapabilityRegistry | None = None,
    ) -> list[ValidationResult]:
        """
        Validate a PlatformObject using published object rules.
        """
        payload = {
            "object": obj,
            "source": self._source_name(obj),
            "capability_registry": (
                capability_registry or self._capability_registry
            ),
        }
        return self._execute_rules(RULE_TARGET_OBJECT, payload)

    def validate_metadata(
        self,
        metadata: object,
        *,
        source: str = "metadata",
    ) -> list[ValidationResult]:
        """
        Validate metadata for runtime artifacts.
        """
        payload = {
            "metadata": metadata,
            "source": source,
        }
        return self._execute_rules(RULE_TARGET_METADATA, payload)

    def validate_schema(
        self,
        target: object,
        schema_ref: str | None = None,
    ) -> list[ValidationResult]:
        """
        Validate a target against a published schema.
        """
        payload = {
            "instance": target,
            "schema_ref": schema_ref,
            "source": self._source_name(target),
        }
        return self._execute_rules(RULE_TARGET_SCHEMA, payload)

    def validate_contract(
        self,
        target: object,
        contract_name: str | None = None,
        *,
        capability_registry: CapabilityRegistry | None = None,
    ) -> list[ValidationResult]:
        """
        Validate a target against a published contract.
        """
        payload = {
            "target": target,
            "contract_name": contract_name,
            "source": self._source_name(target),
            "capability_registry": (
                capability_registry or self._capability_registry
            ),
        }
        return self._execute_rules(RULE_TARGET_CONTRACT, payload)

    def validate_dependencies(
        self,
        target: DependencyResolver | None = None,
    ) -> list[ValidationResult]:
        """
        Validate dependency relationships.
        """
        payload = {
            "target": target or self._dependency_resolver,
            "source": self._source_name(target or "DependencyResolver"),
        }
        return self._execute_rules(RULE_TARGET_DEPENDENCIES, payload)

    def validate_runtime(
        self,
        *,
        object_registry: ObjectRegistry | None = None,
        capability_registry: CapabilityRegistry | None = None,
        service_registry: ServiceRegistry | None = None,
        event_bus: EventBus | None = None,
        dependency_resolver: DependencyResolver | None = None,
    ) -> list[ValidationResult]:
        """
        Validate runtime foundations using published rules.
        """
        payload = {
            "object_registry": object_registry or self._object_registry,
            "capability_registry": (
                capability_registry or self._capability_registry
            ),
            "service_registry": service_registry or self._service_registry,
            "event_bus": event_bus or self._event_bus,
            "dependency_resolver": (
                dependency_resolver or self._dependency_resolver
            ),
        }
        return self._execute_rules(RULE_TARGET_RUNTIME, payload)

    def _require_rule(self, rule_id: str) -> ValidationRule:
        """
        Retrieve a registered validation rule.
        """
        rule = self._rules.get(rule_id)

        if rule is None:
            raise KeyError(rule_id)

        return rule

    def _iter_rules(self, target_type: str) -> list[ValidationRule]:
        """
        Return enabled rules in deterministic order.
        """
        return sorted(
            [
                rule
                for rule in self._rules.values()
                if rule.target_type == target_type and rule.enabled
            ],
            key=lambda rule: (rule.order, rule.rule_id),
        )

    def _execute_rules(
        self,
        target_type: str,
        payload: dict[str, object],
    ) -> list[ValidationResult]:
        """
        Execute every enabled rule for a target type.
        """
        results: list[ValidationResult] = []

        for rule in self._iter_rules(target_type):
            results.extend(rule.execute(payload, self))

        return results

    def _register_builtin_rules(self) -> None:
        """
        Register published built-in validation rules.
        """
        builtin_rules = [
            ValidationRule(
                "object.instance",
                RULE_TARGET_OBJECT,
                self._rule_object_instance,
                order=10,
            ),
            ValidationRule(
                "object.identifier",
                RULE_TARGET_OBJECT,
                self._rule_object_identifier,
                order=20,
            ),
            ValidationRule(
                "object.metadata",
                RULE_TARGET_OBJECT,
                self._rule_object_metadata,
                order=30,
            ),
            ValidationRule(
                "object.schema",
                RULE_TARGET_OBJECT,
                self._rule_object_schema,
                order=40,
            ),
            ValidationRule(
                "object.service_contract",
                RULE_TARGET_OBJECT,
                self._rule_object_service_contract,
                order=50,
            ),
            ValidationRule(
                "object.engine_contract",
                RULE_TARGET_OBJECT,
                self._rule_object_engine_contract,
                order=60,
            ),
            ValidationRule(
                "metadata.mapping",
                RULE_TARGET_METADATA,
                self._rule_metadata_mapping,
                order=10,
            ),
            ValidationRule(
                "metadata.lifecycle_state",
                RULE_TARGET_METADATA,
                self._rule_metadata_lifecycle_state,
                order=20,
            ),
            ValidationRule(
                "schema.published",
                RULE_TARGET_SCHEMA,
                self._rule_schema_published,
                order=10,
            ),
            ValidationRule(
                "schema.evaluate",
                RULE_TARGET_SCHEMA,
                self._rule_schema_evaluate,
                order=20,
            ),
            ValidationRule(
                "contract.published",
                RULE_TARGET_CONTRACT,
                self._rule_contract_published,
                order=10,
            ),
            ValidationRule(
                "contract.register",
                RULE_TARGET_CONTRACT,
                self._rule_contract_register,
                order=20,
            ),
            ValidationRule(
                "contract.service",
                RULE_TARGET_CONTRACT,
                self._rule_contract_service,
                order=30,
            ),
            ValidationRule(
                "contract.engine",
                RULE_TARGET_CONTRACT,
                self._rule_contract_engine,
                order=40,
            ),
            ValidationRule(
                "dependencies.target",
                RULE_TARGET_DEPENDENCIES,
                self._rule_dependencies_target,
                order=10,
            ),
            ValidationRule(
                "dependencies.validate",
                RULE_TARGET_DEPENDENCIES,
                self._rule_dependencies_validate,
                order=20,
            ),
            ValidationRule(
                "runtime.components",
                RULE_TARGET_RUNTIME,
                self._rule_runtime_components,
                order=10,
            ),
            ValidationRule(
                "runtime.object_registry",
                RULE_TARGET_RUNTIME,
                self._rule_runtime_object_registry,
                order=20,
            ),
            ValidationRule(
                "runtime.capability_registry",
                RULE_TARGET_RUNTIME,
                self._rule_runtime_capability_registry,
                order=30,
            ),
            ValidationRule(
                "runtime.service_registry",
                RULE_TARGET_RUNTIME,
                self._rule_runtime_service_registry,
                order=40,
            ),
            ValidationRule(
                "runtime.event_bus",
                RULE_TARGET_RUNTIME,
                self._rule_runtime_event_bus,
                order=50,
            ),
            ValidationRule(
                "runtime.dependency_resolver",
                RULE_TARGET_RUNTIME,
                self._rule_runtime_dependency_resolver,
                order=60,
            ),
        ]

        for rule in builtin_rules:
            self.register_rule(rule)

    def _rule_object_instance(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Ensure the target is a PlatformObject.
        """
        obj = payload["object"]
        source = str(payload["source"])

        if not isinstance(obj, PlatformObject):
            return [
                self._invalid_result(
                    "object.instance",
                    "Validation target is not a PlatformObject",
                    source,
                )
            ]

        return [
            self._valid_result(
                "object.instance",
                "PlatformObject target is valid",
                source,
            )
        ]

    def _rule_object_identifier(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Detect missing platform object identifiers.
        """
        obj = payload["object"]
        source = str(payload["source"])

        if not isinstance(obj, PlatformObject):
            return []

        if not isinstance(obj.object_id, str) or not obj.object_id:
            return [
                self._invalid_result(
                    "object.identifier",
                    "PlatformObject object_id is required",
                    source,
                )
            ]

        return [
            self._valid_result(
                "object.identifier",
                "PlatformObject object_id is present",
                source,
            )
        ]

    def _rule_object_metadata(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Validate object metadata.
        """
        obj = payload["object"]
        source = str(payload["source"])

        if not isinstance(obj, PlatformObject):
            return []

        return validator.validate_metadata(obj.metadata, source=source)

    def _rule_object_schema(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Validate a PlatformObject against the published object schema.
        """
        obj = payload["object"]

        if not isinstance(obj, PlatformObject):
            return []

        return validator.validate_schema(obj, "AXI-SCH-007")

    def _rule_object_service_contract(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Validate service-specific object rules when applicable.
        """
        obj = payload["object"]
        capability_registry = payload["capability_registry"]

        if not isinstance(obj, Service):
            return []

        return validator.validate_contract(
            obj,
            "SERVICE_CONTRACT",
            capability_registry=(
                capability_registry
                if isinstance(capability_registry, CapabilityRegistry)
                else None
            ),
        )

    def _rule_object_engine_contract(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Validate engine-specific object rules when applicable.
        """
        obj = payload["object"]
        capability_registry = payload["capability_registry"]

        if not self._is_engine_target(obj):
            return []

        return validator.validate_contract(
            obj,
            "ENGINE_CONTRACT",
            capability_registry=(
                capability_registry
                if isinstance(capability_registry, CapabilityRegistry)
                else None
            ),
        )

    def _rule_metadata_mapping(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Ensure metadata is mapping-shaped.
        """
        metadata = payload["metadata"]
        source = str(payload["source"])

        if not isinstance(metadata, Mapping):
            return [
                self._invalid_result(
                    "metadata.mapping",
                    "Metadata must be a mapping",
                    source,
                )
            ]

        return [
            self._valid_result(
                "metadata.mapping",
                "Metadata mapping is valid",
                source,
            )
        ]

    def _rule_metadata_lifecycle_state(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Detect invalid lifecycle state metadata when present.
        """
        metadata = payload["metadata"]
        source = str(payload["source"])

        if not isinstance(metadata, Mapping):
            return []

        if "lifecycle_state" not in metadata:
            return []

        lifecycle_state = metadata["lifecycle_state"]

        if not isinstance(lifecycle_state, str) or not lifecycle_state:
            return [
                self._invalid_result(
                    "metadata.lifecycle_state",
                    "lifecycle_state must be a non-empty string",
                    source,
                )
            ]

        return [
            self._valid_result(
                "metadata.lifecycle_state",
                "lifecycle_state is valid",
                source,
            )
        ]

    def _rule_schema_published(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Ensure the requested schema is published in SCHEMA_REGISTRY.
        """
        instance = payload["instance"]
        source = str(payload["source"])
        schema_id = self._resolve_schema_id(
            instance,
            payload["schema_ref"],
        )

        if schema_id is None:
            requested = payload["schema_ref"] or instance.__class__.__name__
            return [
                self._invalid_result(
                    "schema.published",
                    (
                        "Schema is not published in SCHEMA_REGISTRY: "
                        f"{requested}"
                    ),
                    source,
                )
            ]

        schema_path = self._published_schemas.get(schema_id)

        if schema_path is None or not schema_path.exists():
            return [
                self._invalid_result(
                    "schema.published",
                    f"Published schema artifact is missing: {schema_id}",
                    source,
                )
            ]

        return [
            self._valid_result(
                "schema.published",
                f"Published schema resolved: {schema_id}",
                source,
            )
        ]

    def _rule_schema_evaluate(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Evaluate a target against a published schema.
        """
        instance = payload["instance"]
        source = str(payload["source"])
        schema_id = self._resolve_schema_id(
            instance,
            payload["schema_ref"],
        )

        if schema_id is None:
            return []

        normalized = self._normalize_schema_instance(instance)

        if not isinstance(normalized, Mapping):
            return [
                self._invalid_result(
                    "schema.evaluate",
                    "Schema validation requires a mapping-compatible target",
                    source,
                )
            ]

        errors = self._validate_schema_instance(
            dict(normalized),
            self._load_schema(schema_id),
            path="$",
        )

        if not errors:
            return [
                self._valid_result(
                    "schema.evaluate",
                    f"Schema validation passed for {schema_id}",
                    source,
                )
            ]

        return [
            self._invalid_result(
                "schema.evaluate",
                error,
                source,
            )
            for error in errors
        ]

    def _rule_contract_published(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Ensure the requested contract is published.
        """
        target = payload["target"]
        source = str(payload["source"])
        contract_name = self._resolve_contract_name(
            target,
            payload["contract_name"],
        )

        if contract_name is None:
            requested = payload["contract_name"] or target.__class__.__name__
            return [
                self._invalid_result(
                    "contract.published",
                    f"Contract is not published: {requested}",
                    source,
                )
            ]

        return [
            self._valid_result(
                "contract.published",
                f"Published contract resolved: {contract_name}",
                source,
            )
        ]

    def _rule_contract_register(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Validate REGISTER_CONTRACT.
        """
        target = payload["target"]
        source = str(payload["source"])
        contract_name = self._resolve_contract_name(
            target,
            payload["contract_name"],
        )

        if contract_name != "REGISTER_CONTRACT":
            return []

        return self._validate_register_contract_target(target, source)

    def _rule_contract_service(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Validate SERVICE_CONTRACT.
        """
        target = payload["target"]
        source = str(payload["source"])
        contract_name = self._resolve_contract_name(
            target,
            payload["contract_name"],
        )
        capability_registry = payload["capability_registry"]

        if contract_name != "SERVICE_CONTRACT":
            return []

        return self._validate_service_contract_target(
            target,
            source,
            capability_registry=(
                capability_registry
                if isinstance(capability_registry, CapabilityRegistry)
                else None
            ),
        )

    def _rule_contract_engine(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Validate ENGINE_CONTRACT.
        """
        target = payload["target"]
        source = str(payload["source"])
        contract_name = self._resolve_contract_name(
            target,
            payload["contract_name"],
        )
        capability_registry = payload["capability_registry"]

        if contract_name != "ENGINE_CONTRACT":
            return []

        return self._validate_engine_contract_target(
            target,
            source,
            capability_registry=(
                capability_registry
                if isinstance(capability_registry, CapabilityRegistry)
                else None
            ),
        )

    def _rule_dependencies_target(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Ensure dependency validation targets a resolver.
        """
        target = payload["target"]
        source = str(payload["source"])

        if not isinstance(target, DependencyResolver):
            return [
                self._invalid_result(
                    "dependencies.target",
                    "Dependency validation requires a DependencyResolver",
                    source,
                )
            ]

        return [
            self._valid_result(
                "dependencies.target",
                "DependencyResolver target is valid",
                source,
            )
        ]

    def _rule_dependencies_validate(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Validate dependency graph state.
        """
        target = payload["target"]
        source = str(payload["source"])

        if not isinstance(target, DependencyResolver):
            return []

        try:
            target.validate_dependencies()
        except Exception as exc:
            return [
                self._invalid_result(
                    "dependencies.validate",
                    str(exc),
                    source,
                )
            ]

        dependency_ids = [
            dependency.dependency_id
            for dependency in target.list_dependencies()
        ]

        if dependency_ids != sorted(dependency_ids):
            return [
                self._invalid_result(
                    "dependencies.validate",
                    "Dependencies are not listed in deterministic order",
                    source,
                )
            ]

        return [
            self._valid_result(
                "dependencies.validate",
                "Dependency graph is valid",
                source,
            )
        ]

    def _rule_runtime_components(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Ensure runtime validation has at least one component to inspect.
        """
        if any(component is not None for component in payload.values()):
            return [
                self._valid_result(
                    "runtime.components",
                    "Runtime validation components are available",
                    "runtime",
                )
            ]

        return [
            self._invalid_result(
                "runtime.components",
                "No runtime components were provided for validation",
                "runtime",
            )
        ]

    def _rule_runtime_object_registry(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Validate object registry state.
        """
        object_registry = payload["object_registry"]
        capability_registry = payload["capability_registry"]

        if not isinstance(object_registry, ObjectRegistry):
            return []

        results = validator.validate_contract(
            object_registry,
            "REGISTER_CONTRACT",
        )

        for object_id in object_registry.keys():
            obj = object_registry.get(object_id)
            if obj is not None:
                results.extend(
                    validator.validate_object(
                        obj,
                        capability_registry=(
                            capability_registry
                            if isinstance(
                                capability_registry,
                                CapabilityRegistry,
                            )
                            else None
                        ),
                    )
                )

        return results

    def _rule_runtime_capability_registry(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Validate capability registry state.
        """
        capability_registry = payload["capability_registry"]

        if not isinstance(capability_registry, CapabilityRegistry):
            return []

        results = validator.validate_contract(
            capability_registry,
            "REGISTER_CONTRACT",
        )

        for capability in capability_registry.list_capabilities():
            results.extend(
                validator.validate_schema(capability, "AXI-SCH-008")
            )

        return results

    def _rule_runtime_service_registry(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Validate service registry state.
        """
        service_registry = payload["service_registry"]
        capability_registry = payload["capability_registry"]

        if not isinstance(service_registry, ServiceRegistry):
            return []

        results = validator.validate_contract(
            service_registry,
            "SERVICE_CONTRACT",
            capability_registry=(
                capability_registry
                if isinstance(capability_registry, CapabilityRegistry)
                else None
            ),
        )

        for service in service_registry.list_services():
            results.extend(
                validator.validate_object(
                    service,
                    capability_registry=(
                        capability_registry
                        if isinstance(capability_registry, CapabilityRegistry)
                        else None
                    ),
                )
            )

        return results

    def _rule_runtime_event_bus(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Validate deterministic event bus subscriber state.
        """
        event_bus = payload["event_bus"]

        if not isinstance(event_bus, EventBus):
            return []

        subscribers = event_bus.list_subscribers()
        subscriber_ids = [
            subscriber.subscriber_id for subscriber in subscribers
        ]

        if subscriber_ids != sorted(subscriber_ids):
            return [
                self._invalid_result(
                    "runtime.event_bus",
                    "Event bus subscribers are not ordered deterministically",
                    "EventBus",
                )
            ]

        for subscriber in subscribers:
            if subscriber.event_types != tuple(
                sorted(set(subscriber.event_types))
            ):
                return [
                    self._invalid_result(
                        "runtime.event_bus",
                        (
                            "Subscriber event types are not normalized: "
                            f"{subscriber.subscriber_id}"
                        ),
                        "EventBus",
                    )
                ]

        return [
            self._valid_result(
                "runtime.event_bus",
                "Event bus subscriber state is valid",
                "EventBus",
            )
        ]

    def _rule_runtime_dependency_resolver(
        self,
        payload: dict[str, object],
        validator: Validator,
    ) -> list[ValidationResult]:
        """
        Validate dependency resolver state.
        """
        dependency_resolver = payload["dependency_resolver"]

        if not isinstance(dependency_resolver, DependencyResolver):
            return []

        return [
            self._valid_result(
                "runtime.dependency_resolver",
                "DependencyResolver component is available",
                "DependencyResolver",
            ),
            *validator.validate_dependencies(dependency_resolver),
        ]

    def _validate_register_contract_target(
        self,
        target: object,
        source: str,
    ) -> list[ValidationResult]:
        """
        Validate published register contract behavior.
        """
        if not isinstance(target, BaseRegistry):
            return [
                self._invalid_result(
                    "contract.register",
                    "REGISTER_CONTRACT requires a BaseRegistry target",
                    source,
                )
            ]

        required_methods = (
            "register",
            "unregister",
            "get",
            "update",
            "exists",
            "keys",
            "values",
            "items",
            "count",
            "clear",
            "load",
        )
        missing_methods = [
            method_name
            for method_name in required_methods
            if not callable(getattr(target, method_name, None))
        ]

        if missing_methods:
            return [
                self._invalid_result(
                    "contract.register",
                    (
                        "Registry target is missing required methods: "
                        + ", ".join(sorted(missing_methods))
                    ),
                    source,
                )
            ]

        keys = target.keys()
        values = target.values()
        items = target.items()

        errors: list[ValidationResult] = []

        if keys != sorted(keys):
            errors.append(
                self._invalid_result(
                    "contract.register",
                    "Registry keys are not deterministic",
                    source,
                )
            )

        if len(keys) != len(set(keys)):
            errors.append(
                self._invalid_result(
                    "contract.register",
                    "Registry keys are not unique",
                    source,
                )
            )

        if target.count() != len(keys):
            errors.append(
                self._invalid_result(
                    "contract.register",
                    "Registry count does not match registered keys",
                    source,
                )
            )

        if len(values) != len(keys) or len(items) != len(keys):
            errors.append(
                self._invalid_result(
                    "contract.register",
                    "Registry values/items do not match registered keys",
                    source,
                )
            )

        if errors:
            return errors

        return [
            self._valid_result(
                "contract.register",
                "REGISTER_CONTRACT validation passed",
                source,
            )
        ]

    def _validate_service_contract_target(
        self,
        target: object,
        source: str,
        *,
        capability_registry: CapabilityRegistry | None = None,
    ) -> list[ValidationResult]:
        """
        Validate published service contract behavior.
        """
        if isinstance(target, Service):
            errors: list[ValidationResult] = []

            if target.namespace != "AXI-SVC":
                errors.append(
                    self._invalid_result(
                        "contract.service",
                        "Service namespace must be 'AXI-SVC'",
                        source,
                    )
                )

            if target.object_type != "Service":
                errors.append(
                    self._invalid_result(
                        "contract.service",
                        "Service object_type must be 'Service'",
                        source,
                    )
                )

            if target.service_id != target.object_id:
                errors.append(
                    self._invalid_result(
                        "contract.service",
                        "service_id must map to object_id",
                        source,
                    )
                )

            if not isinstance(target.metadata, Mapping) or not target.metadata:
                errors.append(
                    self._invalid_result(
                        "contract.service",
                        "Service metadata is required",
                        source,
                    )
                )

            if not target.lifecycle_state:
                errors.append(
                    self._invalid_result(
                        "contract.service",
                        "Service lifecycle_state is required",
                        source,
                    )
                )

            if capability_registry is not None:
                for capability_id in target.capabilities:
                    if not capability_registry.exists(capability_id):
                        errors.append(
                            self._invalid_result(
                                "contract.service",
                                (
                                    "Service capability reference does not "
                                    f"resolve: {capability_id}"
                                ),
                                source,
                            )
                        )

            if errors:
                return errors

            return [
                self._valid_result(
                    "contract.service",
                    "SERVICE_CONTRACT validation passed",
                    source,
                )
            ]

        if isinstance(target, ServiceRegistry):
            required_methods = (
                "register_service",
                "unregister_service",
                "resolve_service",
                "has_service",
                "list_services",
                "update_service",
            )
            missing_methods = [
                method_name
                for method_name in required_methods
                if not callable(getattr(target, method_name, None))
            ]

            if missing_methods:
                return [
                    self._invalid_result(
                        "contract.service",
                        (
                            "ServiceRegistry is missing required methods: "
                            + ", ".join(sorted(missing_methods))
                        ),
                        source,
                    )
                ]

            results = self._validate_register_contract_target(
                target,
                source,
            )
            service_ids = [
                service.service_id
                for service in target.list_services()
            ]

            if service_ids != sorted(service_ids):
                results.append(
                    self._invalid_result(
                        "contract.service",
                        "ServiceRegistry service order is not deterministic",
                        source,
                    )
                )

            if target.count() != len(service_ids):
                results.append(
                    self._invalid_result(
                        "contract.service",
                        "ServiceRegistry count does not match listed services",
                        source,
                    )
                )

            for service in target.list_services():
                results.extend(
                    self._validate_service_contract_target(
                        service,
                        service.service_id,
                        capability_registry=capability_registry,
                    )
                )

            return results

        return [
            self._invalid_result(
                "contract.service",
                "SERVICE_CONTRACT requires a Service or ServiceRegistry target",
                source,
            )
        ]

    def _validate_engine_contract_target(
        self,
        target: object,
        source: str,
        *,
        capability_registry: CapabilityRegistry | None = None,
    ) -> list[ValidationResult]:
        """
        Validate published engine contract behavior.
        """
        if self._is_engine_target(target):
            errors: list[ValidationResult] = []

            if target.namespace != "AXI-ENG":
                errors.append(
                    self._invalid_result(
                        "contract.engine",
                        "Engine namespace must be 'AXI-ENG'",
                        source,
                    )
                )

            if target.object_type != "Engine":
                errors.append(
                    self._invalid_result(
                        "contract.engine",
                        "Engine object_type must be 'Engine'",
                        source,
                    )
                )

            if target.engine_id != target.object_id:
                errors.append(
                    self._invalid_result(
                        "contract.engine",
                        "engine_id must map to object_id",
                        source,
                    )
                )

            if not isinstance(target.metadata, Mapping) or not target.metadata:
                errors.append(
                    self._invalid_result(
                        "contract.engine",
                        "Engine metadata is required",
                        source,
                    )
                )

            if not target.lifecycle_state:
                errors.append(
                    self._invalid_result(
                        "contract.engine",
                        "Engine lifecycle_state is required",
                        source,
                    )
                )

            if capability_registry is not None:
                for capability_id in target.capabilities:
                    if not capability_registry.exists(capability_id):
                        errors.append(
                            self._invalid_result(
                                "contract.engine",
                                (
                                    "Engine capability reference does not "
                                    f"resolve: {capability_id}"
                                ),
                                source,
                            )
                        )

            if errors:
                return errors

            return [
                self._valid_result(
                    "contract.engine",
                    "ENGINE_CONTRACT validation passed",
                    source,
                )
            ]

        required_methods = (
            "register_engine",
            "unregister_engine",
            "lookup_engine",
            "list_engines",
            "update_engine",
            "start_engine",
            "stop_engine",
            "restart_engine",
        )

        if (
            isinstance(target, BaseRegistry)
            and all(
                callable(getattr(target, method_name, None))
                for method_name in required_methods
            )
        ):
            results = self._validate_register_contract_target(
                target,
                source,
            )
            listed_engines = target.list_engines()
            engine_ids = [engine.engine_id for engine in listed_engines]

            if engine_ids != sorted(engine_ids):
                results.append(
                    self._invalid_result(
                        "contract.engine",
                        "EngineRegistry engine order is not deterministic",
                        source,
                    )
                )

            if target.count() != len(engine_ids):
                results.append(
                    self._invalid_result(
                        "contract.engine",
                        "EngineRegistry count does not match listed engines",
                        source,
                    )
                )

            for engine in listed_engines:
                results.extend(
                    self._validate_engine_contract_target(
                        engine,
                        engine.engine_id,
                        capability_registry=capability_registry,
                    )
                )

            return results

        return [
            self._invalid_result(
                "contract.engine",
                "ENGINE_CONTRACT requires an Engine or EngineRegistry target",
                source,
            )
        ]

    def _resolve_schema_id(
        self,
        instance: object,
        schema_ref: object,
    ) -> str | None:
        """
        Resolve a published schema identifier.
        """
        if isinstance(schema_ref, str) and schema_ref:
            normalized = schema_ref.strip()

            for schema_id, schema_path in self._published_schemas.items():
                if normalized in {
                    schema_id,
                    schema_path.name,
                    schema_path.stem,
                }:
                    return schema_id

            return None

        if isinstance(instance, PlatformObject):
            return "AXI-SCH-007"

        if isinstance(instance, Capability):
            return "AXI-SCH-008"

        return None

    def _resolve_contract_name(
        self,
        target: object,
        contract_name: object,
    ) -> str | None:
        """
        Resolve a published contract name.
        """
        if isinstance(contract_name, str) and contract_name:
            normalized = contract_name.strip()

            for name, contract_path in self._published_contracts.items():
                if normalized in {
                    name,
                    contract_path.name,
                    contract_path.stem,
                }:
                    return name

            return None

        if isinstance(target, Service | ServiceRegistry):
            return "SERVICE_CONTRACT"

        if self._is_engine_target(target):
            return "ENGINE_CONTRACT"

        if (
            isinstance(target, BaseRegistry)
            and all(
                callable(getattr(target, method_name, None))
                for method_name in (
                    "register_engine",
                    "unregister_engine",
                    "lookup_engine",
                    "list_engines",
                    "update_engine",
                    "start_engine",
                    "stop_engine",
                    "restart_engine",
                )
            )
        ):
            return "ENGINE_CONTRACT"

        if isinstance(target, BaseRegistry):
            return "REGISTER_CONTRACT"

        return None

    def _load_published_schemas(self) -> dict[str, Path]:
        """
        Load published schema references from SCHEMA_REGISTRY.
        """
        if not SCHEMA_REGISTRY_PATH.exists():
            return {}

        published: dict[str, Path] = {}
        content = SCHEMA_REGISTRY_PATH.read_text(encoding="utf-8")

        for line in content.splitlines():
            if not line.startswith("| `AXI-SCH-"):
                continue

            columns = [
                column.strip()
                for column in line.split("|")[1:-1]
            ]

            if len(columns) != 4:
                continue

            schema_id = columns[0].strip("`")
            schema_path = columns[2].strip("`")
            status = columns[3].strip("`")

            if status != "Published":
                continue

            published[schema_id] = REPOSITORY_ROOT / schema_path

        return published

    @staticmethod
    def _is_engine_target(target: object) -> bool:
        """
        Determine whether a target exposes the published engine boundary.
        """
        return (
            isinstance(target, PlatformObject)
            and target.namespace == "AXI-ENG"
            and target.object_type == "Engine"
            and hasattr(target, "engine_id")
            and hasattr(type(target), "lifecycle_state")
        )

    def _load_published_contracts(self) -> dict[str, Path]:
        """
        Load approved published contracts used by the current runtime.
        """
        published: dict[str, Path] = {}

        for contract_name, contract_path in CONTRACT_PATHS.items():
            if not contract_path.exists():
                continue

            content = contract_path.read_text(encoding="utf-8")

            if "**Status:** Approved" in content:
                published[contract_name] = contract_path

        return published

    def _load_schema(self, schema_id: str) -> dict[str, Any]:
        """
        Load a published JSON schema by identifier.
        """
        if schema_id in self._schema_cache:
            return self._schema_cache[schema_id]

        schema_path = self._published_schemas[schema_id]

        with schema_path.open("r", encoding="utf-8") as schema_file:
            schema = json.load(schema_file)

        self._schema_cache[schema_id] = schema
        return schema

    def _normalize_schema_instance(self, instance: object) -> object:
        """
        Normalize supported runtime objects to schema dictionaries.
        """
        if isinstance(instance, PlatformObject):
            return instance.to_dict()

        if isinstance(instance, Capability):
            return instance.to_dict()

        if isinstance(instance, Mapping):
            return dict(instance)

        return instance

    def _validate_schema_instance(
        self,
        instance: object,
        schema: Mapping[str, Any],
        *,
        path: str,
    ) -> list[str]:
        """
        Validate a target against the limited published schema surface.
        """
        errors: list[str] = []
        schema_type = schema.get("type")

        if schema_type == "object":
            if not isinstance(instance, Mapping):
                return [f"{path} must be an object"]

            properties = schema.get("properties", {})
            required = schema.get("required", [])

            for required_key in required:
                if required_key not in instance:
                    errors.append(f"{path}.{required_key} is required")

            additional_properties = schema.get(
                "additionalProperties",
                True,
            )

            for key, value in instance.items():
                child_path = f"{path}.{key}"

                if key in properties:
                    errors.extend(
                        self._validate_schema_instance(
                            value,
                            properties[key],
                            path=child_path,
                        )
                    )
                    continue

                if additional_properties is False:
                    errors.append(f"{child_path} is not allowed")

            return errors

        if schema_type == "array":
            if not isinstance(instance, list | tuple):
                return [f"{path} must be an array"]

            items_schema = schema.get("items")

            if schema.get("uniqueItems"):
                serialized = [
                    json.dumps(
                        item,
                        sort_keys=True,
                        default=str,
                    )
                    for item in instance
                ]

                if len(serialized) != len(set(serialized)):
                    errors.append(f"{path} must contain unique items")

            if isinstance(items_schema, Mapping):
                for index, item in enumerate(instance):
                    errors.extend(
                        self._validate_schema_instance(
                            item,
                            items_schema,
                            path=f"{path}[{index}]",
                        )
                    )

            return errors

        if schema_type == "string":
            if not isinstance(instance, str):
                return [f"{path} must be a string"]

            min_length = schema.get("minLength")
            if isinstance(min_length, int) and len(instance) < min_length:
                errors.append(
                    f"{path} must have length >= {min_length}"
                )

            enum_values = schema.get("enum")
            if isinstance(enum_values, list) and instance not in enum_values:
                errors.append(
                    f"{path} must be one of {', '.join(enum_values)}"
                )

            pattern = schema.get("pattern")
            if isinstance(pattern, str) and re.search(pattern, instance) is None:
                errors.append(
                    f"{path} does not match pattern {pattern}"
                )

            if schema.get("format") == "date-time":
                try:
                    datetime.fromisoformat(instance)
                except ValueError:
                    errors.append(f"{path} must be a valid date-time")

            return errors

        return errors

    @staticmethod
    def _source_name(target: object) -> str:
        """
        Derive a stable validation source name.
        """
        if isinstance(target, Service) and target.service_id:
            return target.service_id

        if isinstance(target, PlatformObject) and target.object_id:
            return target.object_id

        if isinstance(target, Capability) and target.capability_id:
            return target.capability_id

        if isinstance(target, str) and target:
            return target

        return target.__class__.__name__

    @staticmethod
    def _valid_result(
        rule_id: str,
        message: str,
        source: str,
    ) -> ValidationResult:
        """
        Build a successful validation result.
        """
        return ValidationResult(
            status="valid",
            severity="info",
            rule_id=rule_id,
            message=message,
            source=source,
        )

    @staticmethod
    def _invalid_result(
        rule_id: str,
        message: str,
        source: str,
        *,
        severity: str = "error",
    ) -> ValidationResult:
        """
        Build a failed validation result.
        """
        return ValidationResult(
            status="invalid",
            severity=severity,
            rule_id=rule_id,
            message=message,
            source=source,
        )


def _ensure_validator(
    validator: Validator | None = None,
    **kwargs: object,
) -> Validator:
    """
    Reuse a provided validator or build a default one.
    """
    if validator is not None:
        return validator

    return Validator(**kwargs)


def validate(
    target: object,
    *,
    validator: Validator | None = None,
) -> list[ValidationResult]:
    """
    Validate a target using published dispatch rules.
    """
    return _ensure_validator(validator).validate(target)


def validate_object(
    obj: object,
    *,
    validator: Validator | None = None,
    capability_registry: CapabilityRegistry | None = None,
) -> list[ValidationResult]:
    """
    Validate a PlatformObject.
    """
    active_validator = _ensure_validator(
        validator,
        capability_registry=capability_registry,
    )
    return active_validator.validate_object(
        obj,
        capability_registry=capability_registry,
    )


def validate_metadata(
    metadata: object,
    *,
    validator: Validator | None = None,
    source: str = "metadata",
) -> list[ValidationResult]:
    """
    Validate metadata.
    """
    return _ensure_validator(validator).validate_metadata(
        metadata,
        source=source,
    )


def validate_schema(
    target: object,
    schema_ref: str | None = None,
    *,
    validator: Validator | None = None,
) -> list[ValidationResult]:
    """
    Validate a target against a published schema.
    """
    return _ensure_validator(validator).validate_schema(
        target,
        schema_ref,
    )


def validate_contract(
    target: object,
    contract_name: str | None = None,
    *,
    validator: Validator | None = None,
    capability_registry: CapabilityRegistry | None = None,
) -> list[ValidationResult]:
    """
    Validate a target against a published contract.
    """
    active_validator = _ensure_validator(
        validator,
        capability_registry=capability_registry,
    )
    return active_validator.validate_contract(
        target,
        contract_name,
        capability_registry=capability_registry,
    )


def validate_dependencies(
    target: DependencyResolver | None = None,
    *,
    validator: Validator | None = None,
    dependency_resolver: DependencyResolver | None = None,
) -> list[ValidationResult]:
    """
    Validate dependency relationships.
    """
    active_validator = _ensure_validator(
        validator,
        dependency_resolver=dependency_resolver or target,
    )
    return active_validator.validate_dependencies(
        target or dependency_resolver,
    )


def validate_runtime(
    *,
    validator: Validator | None = None,
    object_registry: ObjectRegistry | None = None,
    capability_registry: CapabilityRegistry | None = None,
    service_registry: ServiceRegistry | None = None,
    event_bus: EventBus | None = None,
    dependency_resolver: DependencyResolver | None = None,
) -> list[ValidationResult]:
    """
    Validate runtime component state.
    """
    active_validator = _ensure_validator(
        validator,
        object_registry=object_registry,
        capability_registry=capability_registry,
        service_registry=service_registry,
        event_bus=event_bus,
        dependency_resolver=dependency_resolver,
    )
    return active_validator.validate_runtime(
        object_registry=object_registry,
        capability_registry=capability_registry,
        service_registry=service_registry,
        event_bus=event_bus,
        dependency_resolver=dependency_resolver,
    )
