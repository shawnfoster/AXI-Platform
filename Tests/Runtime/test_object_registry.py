from Runtime.ObjectModel.platform_object import PlatformObject
from Runtime.ObjectRegistry.registry import ObjectRegistry


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


def test_registry_register():
    registry = ObjectRegistry()

    obj = build_object(1)

    registry.register(obj)

    assert registry.count() == 1
    assert registry.exists(obj.object_id)


def test_registry_lookup():
    registry = ObjectRegistry()

    obj = build_object(2)

    registry.register(obj)

    found = registry.get(obj.object_id)

    assert found is obj


def test_registry_remove():
    registry = ObjectRegistry()

    obj = build_object(3)

    registry.register(obj)

    registry.unregister(obj.object_id)

    assert registry.count() == 0