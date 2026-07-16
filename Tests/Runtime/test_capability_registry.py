from __future__ import annotations

import pytest

from Runtime.CapabilityRegistry import Capability, CapabilityRegistry
from Runtime.ObjectModel.platform_object import PlatformObject
from Runtime.exceptions import (
    CapabilityNotFoundError,
    DuplicateRegistrationError,
)


def build_capability(i: int) -> Capability:
    return Capability(
        capability_id=f"CAP-{i:03d}",
        name=f"Capability {i}",
        description=f"Capability description {i}",
        version="1.0",
        status="Approved",
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


def test_capability_registry_register_and_lookup() -> None:
    registry = CapabilityRegistry()
    capability = build_capability(1)

    registry.register(capability)

    assert registry.count() == 1
    assert registry.exists(capability.capability_id)
    assert registry.get(capability.capability_id) is capability


def test_capability_registry_rejects_duplicates() -> None:
    registry = CapabilityRegistry()
    capability = build_capability(2)

    registry.register(capability)

    with pytest.raises(DuplicateRegistrationError):
        registry.register(build_capability(2))


def test_capability_registry_update_replaces_existing_capability() -> None:
    registry = CapabilityRegistry()
    capability = build_capability(3)

    registry.register(capability)

    updated = Capability(
        capability_id=capability.capability_id,
        name=capability.name,
        description="Updated description",
        version="2.0",
        status="Frozen",
    )

    registry.update(updated)

    found = registry.require(capability.capability_id)

    assert found.description == "Updated description"
    assert found.version == "2.0"
    assert found.status == "Frozen"


def test_capability_registry_update_requires_existing_capability() -> None:
    registry = CapabilityRegistry()

    with pytest.raises(CapabilityNotFoundError):
        registry.update(build_capability(4))


def test_capability_registry_remove_and_enumerate() -> None:
    registry = CapabilityRegistry()
    capability_a = build_capability(10)
    capability_b = build_capability(2)

    registry.register(capability_a)
    registry.register(capability_b)

    listed = registry.list_capabilities()

    assert [capability.capability_id for capability in listed] == [
        "CAP-002",
        "CAP-010",
    ]

    registry.remove(capability_a.capability_id)

    assert not registry.exists(capability_a.capability_id)
    assert registry.count() == 1


def test_capability_registry_tracks_platform_object_implementations() -> None:
    registry = CapabilityRegistry()
    capability = build_capability(5)
    obj = build_object(1)

    registry.register(capability)
    registry.add_implementation(capability.capability_id, obj)

    assert capability.implements == {obj.object_id}

    registry.remove_implementation(capability.capability_id, obj)

    assert capability.implements == set()


def test_capability_registry_serialization_round_trip() -> None:
    registry = CapabilityRegistry()
    capability = build_capability(6)
    obj = build_object(2)

    capability.add_implementation(obj)
    capability.add_dependency("CAP-001")
    capability.metadata["source"] = "test"

    registry.register(capability)

    restored = CapabilityRegistry.from_dict(registry.to_dict())
    restored_capability = restored.require(capability.capability_id)

    assert restored.count() == 1
    assert restored_capability.to_dict() == capability.to_dict()
