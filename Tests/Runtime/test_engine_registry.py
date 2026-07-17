from __future__ import annotations

import pytest

from Runtime.ApplicationRegistry import Application, ApplicationRegistry
from Runtime.CapabilityRegistry import Capability, CapabilityRegistry
from Runtime.EngineRegistry import Engine, EngineRegistry
from Runtime.EventBus import Event, EventBus, Subscriber
from Runtime.PluginLoader import PluginLoader
from Runtime.ServiceRegistry import Service, ServiceRegistry
from Runtime.exceptions import (
    DependencyError,
    DuplicateRegistrationError,
    ObjectNotFoundError,
    RegistryError,
)


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
        provenance={"created_by": "test"},
        metadata={
            "lifecycle_state": "Registered",
            "transport": "in-process",
        },
    )


def build_application(i: int) -> Application:
    return Application(
        object_id=f"OBJ-{i:06d}",
        namespace="AXI-APP",
        object_type="Application",
        name=f"Application {i}",
        description=f"Application description {i}",
        version="1.0.0",
        status="Approved",
        owner="Platform",
        provenance={"created_by": "test"},
        metadata={
            "lifecycle_state": "Registered",
            "runtime": "local",
        },
    )


def build_engine(
    i: int,
    *,
    capabilities: list[str] | None = None,
    dependencies: list[str] | None = None,
    metadata: dict[str, object] | None = None,
) -> Engine:
    return Engine(
        object_id=f"OBJ-{i:06d}",
        namespace="AXI-ENG",
        object_type="Engine",
        name=f"Engine {i}",
        description=f"Engine description {i}",
        version="1.0.0",
        status="Approved",
        owner="Platform",
        capabilities=capabilities or [],
        dependencies=dependencies or [],
        provenance={"created_by": "test"},
        metadata=(
            metadata
            if metadata is not None
            else {
                "lifecycle_state": "Registered",
                "runtime": "local",
            }
        ),
    )


def build_manifest(plugin_id: str) -> dict[str, object]:
    return {
        "plugin_id": plugin_id,
        "name": f"Plugin {plugin_id}",
        "version": "1.0.0",
        "author": "AXI Platform",
        "description": f"Runtime plugin {plugin_id}",
        "capabilities": [],
        "dependencies": [],
        "lifecycle_state": "Discovered",
    }


def test_engine_registry_register_lookup_list_and_serialize() -> None:
    registry = EngineRegistry()
    engine = build_engine(1)

    registry.register_engine(engine)

    found = registry.lookup_engine(engine.engine_id)
    restored = Engine.from_dict(engine.to_dict())

    assert registry.count() == 1
    assert found is engine
    assert found is registry.lookup_engine(engine.engine_id)
    assert found is not None
    assert found.lifecycle_state == "Registered"
    assert found.metadata["runtime"] == "local"
    assert registry.list_engines() == [engine]
    assert restored.engine_id == engine.engine_id


def test_engine_registry_rejects_duplicates() -> None:
    registry = EngineRegistry()
    engine = build_engine(2)

    registry.register_engine(engine)

    with pytest.raises(DuplicateRegistrationError):
        registry.register_engine(build_engine(2))


def test_engine_registry_unregisters_and_clears_capabilities() -> None:
    capability_registry = CapabilityRegistry()
    capability = build_capability(1)
    capability_registry.register(capability)
    registry = EngineRegistry(
        capability_registry=capability_registry,
    )
    engine = build_engine(
        3,
        capabilities=[capability.capability_id],
    )

    registry.register_engine(engine)

    assert capability.implements == {engine.engine_id}

    registry.unregister_engine(engine.engine_id)
    registry.unregister_engine(engine.engine_id)

    assert registry.count() == 0
    assert registry.lookup_engine(engine.engine_id) is None
    assert capability.implements == set()


def test_engine_registry_updates_and_refreshes_capability_links() -> None:
    capability_registry = CapabilityRegistry()
    first_capability = build_capability(1)
    second_capability = build_capability(2)
    capability_registry.register(first_capability)
    capability_registry.register(second_capability)
    registry = EngineRegistry(
        capability_registry=capability_registry,
    )
    engine = build_engine(
        4,
        capabilities=[first_capability.capability_id],
    )

    registry.register_engine(engine)

    updated = build_engine(
        4,
        capabilities=[second_capability.capability_id],
        metadata={
            "lifecycle_state": "Running",
            "runtime": "distributed",
        },
    )
    updated.description = "Updated engine"

    registry.update_engine(updated)
    found = registry.lookup_engine(updated.engine_id)

    assert found is updated
    assert found is not None
    assert found.description == "Updated engine"
    assert found.lifecycle_state == "Running"
    assert first_capability.implements == set()
    assert second_capability.implements == {updated.engine_id}


def test_engine_registry_requires_existing_engine_for_updates() -> None:
    registry = EngineRegistry()

    with pytest.raises(ObjectNotFoundError):
        registry.update_engine(build_engine(5))


def test_engine_registry_supports_lifecycle_operations_and_events() -> None:
    event_bus = EventBus()
    plugin_loader = PluginLoader()
    plugin_loader.load_plugin(build_manifest("plugin-runtime"))
    application_registry = ApplicationRegistry()
    application_registry.register_application(build_application(600))
    registry = EngineRegistry(
        event_bus=event_bus,
        plugin_loader=plugin_loader,
        application_registry=application_registry,
    )
    engine = build_engine(6)
    received: list[Event] = []

    event_bus.subscribe(
        Subscriber(
            subscriber_id="SUB-ENG",
            event_types=(
                "engine.registered",
                "engine.started",
                "engine.stopped",
                "engine.restarted",
                "engine.unregistered",
            ),
            handler=lambda event: received.append(event),
        )
    )

    registry.register_engine(engine)
    started = registry.start_engine(engine.engine_id)
    assert started.lifecycle_state == "Running"
    stopped = registry.stop_engine(engine.engine_id)
    assert stopped.lifecycle_state == "Stopped"
    registry.start_engine(engine.engine_id)
    restarted = registry.restart_engine(engine.engine_id)
    assert restarted.lifecycle_state == "Running"
    registry.unregister_engine(engine.engine_id)

    assert [event.event_type for event in received] == [
        "engine.registered",
        "engine.started",
        "engine.stopped",
        "engine.started",
        "engine.restarted",
        "engine.unregistered",
    ]
    assert received[0].source == "Runtime.EngineRegistry"
    assert received[0].payload["engine_id"] == engine.engine_id
    assert received[0].payload["loaded_plugins"] == ("plugin-runtime",)
    assert received[0].payload["registered_applications"] == (
        "OBJ-000600",
    )


def test_engine_registry_rejects_invalid_lifecycle_transitions() -> None:
    registry = EngineRegistry()
    engine = build_engine(7)

    registry.register_engine(engine)

    with pytest.raises(RegistryError):
        registry.stop_engine(engine.engine_id)

    registry.start_engine(engine.engine_id)

    with pytest.raises(RegistryError):
        registry.start_engine(engine.engine_id)


def test_engine_registry_rejects_invalid_metadata() -> None:
    registry = EngineRegistry()
    engine = build_engine(8, metadata={})

    with pytest.raises(RegistryError):
        registry.register_engine(engine)


def test_engine_registry_rejects_invalid_schema_inputs() -> None:
    registry = EngineRegistry()
    engine = build_engine(9)
    engine.name = ""

    with pytest.raises(RegistryError):
        registry.register_engine(engine)


def test_engine_registry_validates_dependencies_against_service_and_application_registries(
) -> None:
    service_registry = ServiceRegistry()
    service = build_service(10)
    service_registry.register_service(service)
    application_registry = ApplicationRegistry()
    application = build_application(11)
    application_registry.register_application(application)
    registry = EngineRegistry(
        service_registry=service_registry,
        application_registry=application_registry,
    )
    engine = build_engine(
        12,
        dependencies=[service.service_id, application.application_id],
    )

    registry.register_engine(engine)

    found = registry.lookup_engine(engine.engine_id)

    assert found is engine
    assert found is not None
    assert found.dependencies == [service.service_id, application.application_id]


def test_engine_registry_rejects_unresolved_dependencies() -> None:
    registry = EngineRegistry()
    engine = build_engine(
        13,
        dependencies=["OBJ-999999"],
    )

    with pytest.raises(DependencyError):
        registry.register_engine(engine)


def test_engine_registry_rejects_circular_dependencies_on_update() -> None:
    registry = EngineRegistry()
    first = build_engine(14)
    second = build_engine(
        15,
        dependencies=[first.engine_id],
    )

    registry.register_engine(first)
    registry.register_engine(second)

    updated_first = build_engine(
        14,
        dependencies=[second.engine_id],
    )

    with pytest.raises(DependencyError):
        registry.update_engine(updated_first)
