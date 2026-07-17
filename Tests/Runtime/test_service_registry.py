from __future__ import annotations

import pytest

from Runtime.CapabilityRegistry import Capability, CapabilityRegistry
from Runtime.ServiceRegistry import Service, ServiceRegistry
from Runtime.exceptions import (
    CapabilityNotFoundError,
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
        provenance={"created_by": "test"},
        metadata=(
            metadata
            if metadata is not None
            else {
                "lifecycle_state": "Registered",
                "transport": "in-process",
            }
        ),
    )


def test_service_registry_register_and_lookup() -> None:
    registry = ServiceRegistry()
    service = build_service(1)

    registry.register_service(service)

    found = registry.resolve_service(service.service_id)

    assert registry.count() == 1
    assert registry.has_service(service.service_id)
    assert found is service
    assert found.provenance == {"created_by": "test"}
    assert found.lifecycle_state == "Registered"
    assert registry.list_services() == [service]


def test_service_registry_rejects_duplicates() -> None:
    registry = ServiceRegistry()
    service = build_service(2)

    registry.register_service(service)

    with pytest.raises(DuplicateRegistrationError):
        registry.register_service(build_service(2))


def test_service_registry_unregisters_services_and_capabilities() -> None:
    capability_registry = CapabilityRegistry()
    capability = build_capability(1)
    capability_registry.register(capability)
    registry = ServiceRegistry(capability_registry)
    service = build_service(3, capabilities=[capability.capability_id])

    registry.register_service(service)

    assert capability.implements == {service.service_id}

    registry.unregister_service(service.service_id)

    assert registry.count() == 0
    assert capability.implements == set()


def test_service_registry_updates_services_and_capability_links() -> None:
    capability_registry = CapabilityRegistry()
    first_capability = build_capability(1)
    second_capability = build_capability(2)
    capability_registry.register(first_capability)
    capability_registry.register(second_capability)
    registry = ServiceRegistry(capability_registry)
    service = build_service(4, capabilities=[first_capability.capability_id])

    registry.register_service(service)

    updated = build_service(
        4,
        capabilities=[second_capability.capability_id],
        metadata={
            "lifecycle_state": "Running",
            "transport": "remote",
        },
    )
    updated.description = "Updated service"

    registry.update_service(updated)

    found = registry.resolve_service(updated.service_id)

    assert found.description == "Updated service"
    assert found.lifecycle_state == "Running"
    assert first_capability.implements == set()
    assert second_capability.implements == {updated.service_id}


def test_service_registry_requires_existing_service_for_updates() -> None:
    registry = ServiceRegistry()

    with pytest.raises(ObjectNotFoundError):
        registry.update_service(build_service(5))


def test_service_registry_rejects_missing_metadata() -> None:
    registry = ServiceRegistry()
    service = build_service(6, metadata={})

    with pytest.raises(RegistryError):
        registry.register_service(service)


def test_service_registry_rejects_missing_lifecycle_state() -> None:
    registry = ServiceRegistry()
    service = build_service(7, metadata={"transport": "in-process"})

    with pytest.raises(RegistryError):
        registry.register_service(service)


def test_service_registry_rejects_missing_capabilities() -> None:
    registry = ServiceRegistry(CapabilityRegistry())
    service = build_service(8, capabilities=["CAP-404"])

    with pytest.raises(CapabilityNotFoundError):
        registry.register_service(service)


def test_service_registry_serializes_services() -> None:
    service = build_service(9)

    restored = Service.from_dict(service.to_dict())

    assert restored.service_id == service.service_id
    assert restored.lifecycle_state == service.lifecycle_state
    assert restored.provenance == service.provenance
