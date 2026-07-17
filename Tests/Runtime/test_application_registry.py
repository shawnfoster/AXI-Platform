from __future__ import annotations

import pytest

from Runtime.ApplicationRegistry import Application, ApplicationRegistry
from Runtime.CapabilityRegistry import Capability, CapabilityRegistry
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


def build_application(
    i: int,
    *,
    capabilities: list[str] | None = None,
    dependencies: list[str] | None = None,
    services: list[str] | None = None,
    plugins: list[str] | None = None,
    metadata: dict[str, object] | None = None,
) -> Application:
    return Application(
        object_id=f"OBJ-{i:06d}",
        namespace="AXI-APP",
        object_type="Application",
        name=f"Application {i}",
        description=f"Application description {i}",
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
        services=services or [],
        plugins=plugins or [],
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


def test_application_registry_register_lookup_list_and_serialize() -> None:
    registry = ApplicationRegistry()
    application = build_application(1)

    registry.register_application(application)

    found = registry.lookup_application(application.application_id)
    restored = Application.from_dict(application.to_dict())

    assert registry.count() == 1
    assert found is application
    assert found is registry.lookup_application(application.application_id)
    assert found is not None
    assert found.lifecycle_state == "Registered"
    assert found.metadata["runtime"] == "local"
    assert registry.list_applications() == [application]
    assert restored.application_id == application.application_id
    assert restored.services == application.services
    assert restored.plugins == application.plugins


def test_application_registry_rejects_duplicates() -> None:
    registry = ApplicationRegistry()
    application = build_application(2)

    registry.register_application(application)

    with pytest.raises(DuplicateRegistrationError):
        registry.register_application(build_application(2))


def test_application_registry_unregisters_and_clears_capabilities() -> None:
    capability_registry = CapabilityRegistry()
    capability = build_capability(1)
    capability_registry.register(capability)
    registry = ApplicationRegistry(
        capability_registry=capability_registry,
    )
    application = build_application(
        3,
        capabilities=[capability.capability_id],
    )

    registry.register_application(application)

    assert capability.implements == {application.application_id}

    registry.unregister_application(application.application_id)
    registry.unregister_application(application.application_id)

    assert registry.count() == 0
    assert registry.lookup_application(application.application_id) is None
    assert capability.implements == set()


def test_application_registry_updates_and_refreshes_capability_links() -> None:
    capability_registry = CapabilityRegistry()
    first_capability = build_capability(1)
    second_capability = build_capability(2)
    capability_registry.register(first_capability)
    capability_registry.register(second_capability)
    registry = ApplicationRegistry(
        capability_registry=capability_registry,
    )
    application = build_application(
        4,
        capabilities=[first_capability.capability_id],
    )

    registry.register_application(application)

    updated = build_application(
        4,
        capabilities=[second_capability.capability_id],
        services=["OBJ-000401"],
        plugins=["plugin-updated"],
        metadata={
            "lifecycle_state": "Running",
            "runtime": "distributed",
        },
    )
    updated.description = "Updated application"

    registry.update_application(updated)
    found = registry.lookup_application(updated.application_id)

    assert found is updated
    assert found is not None
    assert found.description == "Updated application"
    assert found.lifecycle_state == "Running"
    assert found.services == ["OBJ-000401"]
    assert found.plugins == ["plugin-updated"]
    assert first_capability.implements == set()
    assert second_capability.implements == {updated.application_id}


def test_application_registry_requires_existing_application_for_updates() -> None:
    registry = ApplicationRegistry()

    with pytest.raises(ObjectNotFoundError):
        registry.update_application(build_application(5))


def test_application_registry_supports_lifecycle_operations_and_events() -> None:
    event_bus = EventBus()
    plugin_loader = PluginLoader()
    plugin_loader.load_plugin(build_manifest("plugin-runtime"))
    registry = ApplicationRegistry(
        event_bus=event_bus,
        plugin_loader=plugin_loader,
    )
    application = build_application(
        6,
        plugins=["plugin-runtime"],
    )
    received: list[Event] = []

    event_bus.subscribe(
        Subscriber(
            subscriber_id="SUB-APP",
            event_types=(
                "application.registered",
                "application.started",
                "application.stopped",
                "application.restarted",
                "application.unregistered",
            ),
            handler=lambda event: received.append(event),
        )
    )

    registry.register_application(application)
    started = registry.start_application(application.application_id)
    assert started.lifecycle_state == "Running"
    stopped = registry.stop_application(application.application_id)
    assert stopped.lifecycle_state == "Stopped"
    registry.start_application(application.application_id)
    restarted = registry.restart_application(application.application_id)
    assert restarted.lifecycle_state == "Running"
    registry.unregister_application(application.application_id)

    assert [event.event_type for event in received] == [
        "application.registered",
        "application.started",
        "application.stopped",
        "application.started",
        "application.restarted",
        "application.unregistered",
    ]
    assert received[0].source == "Runtime.ApplicationRegistry"
    assert received[0].payload["application_id"] == application.application_id
    assert received[0].payload["loaded_plugins"] == ("plugin-runtime",)


def test_application_registry_rejects_invalid_lifecycle_transitions() -> None:
    registry = ApplicationRegistry()
    application = build_application(7)

    registry.register_application(application)

    with pytest.raises(RegistryError):
        registry.stop_application(application.application_id)

    registry.start_application(application.application_id)

    with pytest.raises(RegistryError):
        registry.start_application(application.application_id)


def test_application_registry_rejects_invalid_metadata() -> None:
    registry = ApplicationRegistry()
    application = build_application(8, metadata={})

    with pytest.raises(RegistryError):
        registry.register_application(application)


def test_application_registry_rejects_invalid_schema_inputs() -> None:
    registry = ApplicationRegistry()
    application = build_application(9)
    application.name = ""

    with pytest.raises(RegistryError):
        registry.register_application(application)


def test_application_registry_validates_dependencies_against_service_registry() -> None:
    service_registry = ServiceRegistry()
    service = build_service(10)
    service_registry.register_service(service)
    registry = ApplicationRegistry(
        service_registry=service_registry,
    )
    application = build_application(
        11,
        dependencies=[service.service_id],
        services=[service.service_id],
        plugins=["plugin-runtime"],
    )

    registry.register_application(application)

    found = registry.lookup_application(application.application_id)

    assert found is application
    assert found is not None
    assert found.dependencies == [service.service_id]
    assert found.services == [service.service_id]


def test_application_registry_rejects_unresolved_dependencies() -> None:
    registry = ApplicationRegistry()
    application = build_application(
        12,
        dependencies=["OBJ-999999"],
    )

    with pytest.raises(DependencyError):
        registry.register_application(application)


def test_application_registry_rejects_circular_dependencies_on_update() -> None:
    registry = ApplicationRegistry()
    first = build_application(13)
    second = build_application(
        14,
        dependencies=[first.application_id],
    )

    registry.register_application(first)
    registry.register_application(second)

    updated_first = build_application(
        13,
        dependencies=[second.application_id],
    )

    with pytest.raises(DependencyError):
        registry.update_application(updated_first)
