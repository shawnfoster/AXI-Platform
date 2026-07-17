from __future__ import annotations

from dataclasses import FrozenInstanceError
from datetime import datetime

import pytest

from Runtime.CapabilityRegistry import Capability, CapabilityRegistry
from Runtime.DependencyResolver import Dependency, DependencyResolver
from Runtime.EngineRegistry import Engine, EngineRegistry
from Runtime.EventBus import EventBus, Subscriber
from Runtime.ObjectModel import PlatformObject
from Runtime.ObjectRegistry import ObjectRegistry
from Runtime.ServiceRegistry import Service, ServiceRegistry
from Runtime.Validation import (
    ValidationResult,
    ValidationRule,
    Validator,
    validate,
    validate_contract,
    validate_dependencies,
    validate_metadata,
    validate_object,
    validate_runtime,
    validate_schema,
)


def build_object(i: int) -> PlatformObject:
    return PlatformObject(
        object_id=f"OBJ-{i:06d}",
        namespace="AXI-ENG",
        object_type="Engine",
        name=f"Engine {i}",
        version="1.0",
        status="Approved",
        owner="Platform",
        metadata={"owner": "test"},
    )


def build_capability(i: int) -> Capability:
    return Capability(
        capability_id=f"CAP-{i:03d}",
        name=f"Capability {i}",
        description=f"Capability description {i}",
        version="1.0",
        status="Approved",
        metadata={"owner": "test"},
    )


def build_service(
    i: int,
    *,
    capabilities: list[str] | None = None,
    metadata: dict[str, object] | None = None,
) -> Service:
    return Service(
        object_id=f"OBJ-{i:06d}",
        namespace="AXI-SVC",
        object_type="Service",
        name=f"Service {i}",
        version="1.0",
        status="Approved",
        owner="Platform",
        capabilities=capabilities or [],
        metadata=(
            metadata
            if metadata is not None
            else {
                "lifecycle_state": "Registered",
                "transport": "in-process",
            }
        ),
    )


def build_engine(
    i: int,
    *,
    capabilities: list[str] | None = None,
    metadata: dict[str, object] | None = None,
) -> Engine:
    return Engine(
        object_id=f"OBJ-{i:06d}",
        namespace="AXI-ENG",
        object_type="Engine",
        name=f"Engine {i}",
        version="1.0",
        status="Approved",
        owner="Platform",
        capabilities=capabilities or [],
        metadata=(
            metadata
            if metadata is not None
            else {
                "lifecycle_state": "Registered",
                "runtime": "local",
            }
        ),
    )


def build_runtime_components() -> tuple[
    ObjectRegistry,
    CapabilityRegistry,
    ServiceRegistry,
    EventBus,
    DependencyResolver,
]:
    object_registry = ObjectRegistry()
    capability_registry = CapabilityRegistry()
    service_registry = ServiceRegistry(capability_registry)
    event_bus = EventBus()

    engine = build_object(1)
    capability = build_capability(1)
    service = build_service(
        2,
        capabilities=[capability.capability_id],
    )

    object_registry.register(engine)
    object_registry.register(service)
    capability_registry.register(capability)
    service_registry.register_service(service)

    event_bus.subscribe(
        Subscriber(
            subscriber_id="SUB-001",
            event_types=("dependency.registered",),
            handler=lambda event: None,
        )
    )

    dependency_resolver = DependencyResolver(
        object_registry=object_registry,
        capability_registry=capability_registry,
        service_registry=service_registry,
        event_bus=event_bus,
    )
    dependency_resolver.register_dependency(
        Dependency(source=engine, target=service)
    )
    dependency_resolver.register_dependency(
        Dependency(source=service, target=capability)
    )

    return (
        object_registry,
        capability_registry,
        service_registry,
        event_bus,
        dependency_resolver,
    )


def assert_no_invalid(results: list[ValidationResult]) -> None:
    assert all(result.status == "valid" for result in results)


def assert_has_invalid_rule(
    results: list[ValidationResult],
    rule_id: str,
) -> None:
    assert any(
        result.rule_id == rule_id and result.status == "invalid"
        for result in results
    )


def test_validation_result_is_immutable() -> None:
    result = ValidationResult(
        status="valid",
        severity="info",
        rule_id="result.test",
        message="Validation result created",
        source="test",
    )

    assert isinstance(result.timestamp, datetime)

    with pytest.raises(FrozenInstanceError):
        result.message = "changed"


def test_validator_supports_rule_registration_order_and_enable_disable() -> None:
    validator = Validator()
    validator.disable_rule("metadata.mapping")
    validator.disable_rule("metadata.lifecycle_state")
    execution_order: list[str] = []

    def first_rule(target, runtime_validator):
        execution_order.append("first")
        return [
            ValidationResult(
                status="valid",
                severity="info",
                rule_id="custom.first",
                message="First custom rule executed",
                source="custom",
            )
        ]

    def second_rule(target, runtime_validator):
        execution_order.append("second")
        return [
            ValidationResult(
                status="invalid",
                severity="warning",
                rule_id="custom.second",
                message="Second custom rule executed",
                source="custom",
            )
        ]

    validator.register_rule(
        ValidationRule(
            rule_id="custom.second",
            target_type="metadata",
            handler=second_rule,
            order=20,
        )
    )
    validator.register_rule(
        ValidationRule(
            rule_id="custom.first",
            target_type="metadata",
            handler=first_rule,
            order=10,
        )
    )

    validator.disable_rule("custom.second")
    execution_order.clear()
    results = validator.validate_metadata({})

    assert execution_order == ["first"]
    assert [result.rule_id for result in results] == ["custom.first"]

    validator.enable_rule("custom.second")
    execution_order.clear()
    results = validator.validate_metadata({})

    assert execution_order == ["first", "second"]
    assert [result.rule_id for result in results] == [
        "custom.first",
        "custom.second",
    ]
    assert results[1].severity == "warning"


def test_validate_metadata_reports_mapping_and_lifecycle_errors() -> None:
    results = validate_metadata(
        {"lifecycle_state": "Running"},
        source="metadata",
    )
    assert_no_invalid(results)

    results = validate_metadata(
        {"lifecycle_state": ""},
        source="metadata",
    )
    assert_has_invalid_rule(results, "metadata.lifecycle_state")

    results = validate_metadata(["not", "mapping"], source="metadata")
    assert_has_invalid_rule(results, "metadata.mapping")


def test_validate_object_and_dispatch_use_published_object_rules() -> None:
    service = build_service(10)

    assert_no_invalid(validate(service))
    assert_no_invalid(validate_object(service))

    invalid_service = build_service(
        11,
        metadata={"lifecycle_state": ""},
    )
    invalid_service.object_id = ""

    results = validate_object(invalid_service)

    assert_has_invalid_rule(results, "object.identifier")
    assert_has_invalid_rule(results, "metadata.lifecycle_state")
    assert_has_invalid_rule(results, "contract.service")


def test_validate_schema_uses_only_published_schema_registry_entries() -> None:
    platform_object = build_object(20)
    capability = build_capability(21)

    assert_no_invalid(validate_schema(platform_object, "AXI-SCH-007"))
    assert_no_invalid(validate_schema(capability))

    invalid_capability = build_capability(22)
    invalid_capability.depends_on.add("NOT-A-CAPABILITY")

    results = validate_schema(invalid_capability, "AXI-SCH-008")
    assert_has_invalid_rule(results, "schema.evaluate")

    results = validate_schema(platform_object, "AXI-SCH-001")
    assert_has_invalid_rule(results, "schema.published")


def test_validate_contract_supports_register_service_and_engine_contracts() -> None:
    object_registry = ObjectRegistry()
    object_registry.register(build_object(30))

    capability_registry = CapabilityRegistry()
    capability = build_capability(31)
    capability_registry.register(capability)
    service_registry = ServiceRegistry(capability_registry)
    service = build_service(
        32,
        capabilities=[capability.capability_id],
    )
    service_registry.register_service(service)
    engine_registry = EngineRegistry(
        capability_registry=capability_registry,
    )
    engine = build_engine(
        33,
        capabilities=[capability.capability_id],
    )
    engine_registry.register_engine(engine)

    assert_no_invalid(
        validate_contract(object_registry, "REGISTER_CONTRACT")
    )
    assert_no_invalid(
        validate_contract(
            service_registry,
            "SERVICE_CONTRACT",
            capability_registry=capability_registry,
        )
    )
    assert_no_invalid(
        validate_contract(
            service,
            "SERVICE_CONTRACT",
            capability_registry=capability_registry,
        )
    )
    assert_no_invalid(
        validate_contract(
            engine,
            "ENGINE_CONTRACT",
            capability_registry=capability_registry,
        )
    )
    assert_no_invalid(
        validate_contract(
            engine_registry,
            "ENGINE_CONTRACT",
            capability_registry=capability_registry,
        )
    )

    invalid_service = build_service(34, metadata={})
    results = validate_contract(invalid_service, "SERVICE_CONTRACT")
    assert_has_invalid_rule(results, "contract.service")

    results = validate_contract(object_registry, "ENGINE_CONTRACT")
    assert_has_invalid_rule(results, "contract.engine")


def test_validate_dependencies_reports_dependency_failures() -> None:
    (
        object_registry,
        capability_registry,
        service_registry,
        event_bus,
        dependency_resolver,
    ) = build_runtime_components()

    assert_no_invalid(validate_dependencies(dependency_resolver))

    service_registry.unregister_service("OBJ-000002")
    object_registry.unregister("OBJ-000002")
    results = validate_dependencies(dependency_resolver)

    assert_has_invalid_rule(results, "dependencies.validate")


def test_validate_runtime_checks_runtime_foundations() -> None:
    (
        object_registry,
        capability_registry,
        service_registry,
        event_bus,
        dependency_resolver,
    ) = build_runtime_components()

    results = validate_runtime(
        object_registry=object_registry,
        capability_registry=capability_registry,
        service_registry=service_registry,
        event_bus=event_bus,
        dependency_resolver=dependency_resolver,
    )

    assert_no_invalid(results)
    assert any(
        result.rule_id == "runtime.dependency_resolver"
        for result in results
    )
