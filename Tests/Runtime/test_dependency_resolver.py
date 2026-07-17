from __future__ import annotations

import pytest

from Runtime.CapabilityRegistry import Capability, CapabilityRegistry
from Runtime.DependencyResolver import Dependency, DependencyResolver
from Runtime.EventBus import Event, EventBus, Subscriber
from Runtime.ObjectModel.platform_object import PlatformObject
from Runtime.ObjectRegistry import ObjectRegistry
from Runtime.ServiceRegistry import Service, ServiceRegistry
from Runtime.exceptions import DependencyError, DuplicateRegistrationError


def build_capability(i: int) -> Capability:
    return Capability(
        capability_id=f"CAP-{i:03d}",
        name=f"Capability {i}",
        description=f"Capability description {i}",
        version="1.0",
        status="Approved",
    )


def build_service(i: int) -> Service:
    return Service(
        object_id=f"OBJ-{i:06d}",
        namespace="AXI-SVC",
        object_type="Service",
        name=f"Service {i}",
        version="1.0",
        status="Approved",
        owner="Platform",
        metadata={
            "lifecycle_state": "Registered",
            "transport": "in-process",
        },
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
    )


def build_resolver() -> tuple[
    DependencyResolver,
    ObjectRegistry,
    CapabilityRegistry,
    ServiceRegistry,
]:
    object_registry = ObjectRegistry()
    capability_registry = CapabilityRegistry()
    service_registry = ServiceRegistry(capability_registry)

    engine = build_object(1)
    service_a = build_service(2)
    service_b = build_service(3)
    capability_a = build_capability(1)
    capability_b = build_capability(2)

    object_registry.register(engine)
    capability_registry.register(capability_a)
    capability_registry.register(capability_b)
    service_registry.register_service(service_a)
    service_registry.register_service(service_b)

    resolver = DependencyResolver(
        object_registry=object_registry,
        capability_registry=capability_registry,
        service_registry=service_registry,
    )

    return resolver, object_registry, capability_registry, service_registry


def test_dependency_registration_and_listing_preserve_metadata() -> None:
    resolver, object_registry, capability_registry, service_registry = build_resolver()
    dependency = Dependency(
        source=object_registry.get("OBJ-000001"),
        target=service_registry.resolve_service("OBJ-000002"),
        metadata={"kind": "runtime"},
    )

    resolver.register_dependency(dependency)

    listed = resolver.list_dependencies()

    assert len(listed) == 1
    assert listed[0].dependency_id == "OBJ-000001->OBJ-000002"
    assert dict(listed[0].metadata) == {"kind": "runtime"}

    with pytest.raises(TypeError):
        listed[0].metadata["kind"] = "changed"


def test_dependency_resolver_rejects_duplicates() -> None:
    resolver, _, capability_registry, service_registry = build_resolver()
    dependency = Dependency(
        source=service_registry.resolve_service("OBJ-000002"),
        target=capability_registry.require("CAP-001"),
    )

    resolver.register_dependency(dependency)

    with pytest.raises(DuplicateRegistrationError):
        resolver.register_dependency(dependency)


def test_dependency_resolver_resolves_transitive_dependencies_in_order() -> None:
    resolver, object_registry, capability_registry, service_registry = build_resolver()

    resolver.register_dependency(
        Dependency(
            source=object_registry.get("OBJ-000001"),
            target=service_registry.resolve_service("OBJ-000003"),
        )
    )
    resolver.register_dependency(
        Dependency(
            source=service_registry.resolve_service("OBJ-000003"),
            target=capability_registry.require("CAP-002"),
        )
    )
    resolver.register_dependency(
        Dependency(
            source=object_registry.get("OBJ-000001"),
            target=capability_registry.require("CAP-001"),
        )
    )

    assert resolver.resolve("OBJ-000001") == [
        "CAP-001",
        "CAP-002",
        "OBJ-000003",
    ]
    assert resolver.resolve_all() == [
        "CAP-001",
        "CAP-002",
        "OBJ-000003",
        "OBJ-000001",
    ]


def test_dependency_resolver_detects_circular_dependencies() -> None:
    resolver, object_registry, _, service_registry = build_resolver()

    resolver.register_dependency(
        Dependency(
            source=object_registry.get("OBJ-000001"),
            target=service_registry.resolve_service("OBJ-000002"),
        )
    )

    with pytest.raises(DependencyError):
        resolver.register_dependency(
            Dependency(
                source=service_registry.resolve_service("OBJ-000002"),
                target=object_registry.get("OBJ-000001"),
            )
        )

    assert [dependency.dependency_id for dependency in resolver.list_dependencies()] == [
        "OBJ-000001->OBJ-000002"
    ]


def test_dependency_resolver_rejects_missing_dependencies() -> None:
    resolver, _, capability_registry, service_registry = build_resolver()

    with pytest.raises(DependencyError):
        resolver.register_dependency(
            Dependency(
                source=service_registry.resolve_service("OBJ-000002"),
                target="OBJ-999999",
            )
        )

    resolver.register_dependency(
        Dependency(
            source=service_registry.resolve_service("OBJ-000002"),
            target=capability_registry.require("CAP-001"),
        )
    )
    service_registry.unregister_service("OBJ-000002")

    with pytest.raises(DependencyError):
        resolver.validate_dependencies()


def test_dependency_rejects_invalid_definitions() -> None:
    with pytest.raises(DependencyError):
        Dependency(source="", target="CAP-001")

    with pytest.raises(DependencyError):
        Dependency(
            source="OBJ-000001",
            target="CAP-001",
            metadata=[],
        )


def test_dependency_resolver_unregisters_dependencies() -> None:
    resolver, _, capability_registry, service_registry = build_resolver()
    dependency = Dependency(
        source=service_registry.resolve_service("OBJ-000002"),
        target=capability_registry.require("CAP-001"),
    )

    resolver.register_dependency(dependency)
    resolver.unregister_dependency(dependency.dependency_id)

    assert resolver.list_dependencies() == []


def test_dependency_resolver_publishes_events_when_bus_is_present() -> None:
    event_bus = EventBus()
    received: list[Event] = []

    event_bus.subscribe(
        Subscriber(
            subscriber_id="SUB-DEPENDENCY",
            event_types=("dependency.registered",),
            handler=lambda event: received.append(event),
        )
    )

    resolver, _, capability_registry, service_registry = build_resolver()
    resolver = DependencyResolver(
        capability_registry=capability_registry,
        service_registry=service_registry,
        event_bus=event_bus,
    )

    resolver.register_dependency(
        Dependency(
            source=service_registry.resolve_service("OBJ-000002"),
            target=capability_registry.require("CAP-001"),
        )
    )

    assert len(received) == 1
    assert received[0].event_type == "dependency.registered"
    assert received[0].source == "Runtime.DependencyResolver"
    assert received[0].payload["dependency_id"] == "OBJ-000002->CAP-001"
