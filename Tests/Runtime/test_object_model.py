from Runtime.ObjectModel.platform_object import PlatformObject


def test_platform_object_creation():
    obj = PlatformObject(
        object_id="OBJ-000001",
        namespace="AXI-ENG",
        object_type="Engine",
        name="Reconstruction Engine",
        version="2.0",
        status="Approved",
        owner="Platform",
    )

    assert obj.object_id == "OBJ-000001"
    assert obj.namespace == "AXI-ENG"
    assert obj.object_type == "Engine"
    assert obj.name == "Reconstruction Engine"
    assert obj.version == "2.0"


def test_platform_object_serialization():
    obj = PlatformObject(
        object_id="OBJ-000002",
        namespace="AXI-SVC",
        object_type="Service",
        name="Decision Service",
        version="1.0",
        status="Draft",
        owner="Platform",
    )

    data = obj.to_dict()

    restored = PlatformObject.from_dict(data)

    assert restored.object_id == obj.object_id
    assert restored.name == obj.name
    assert restored.namespace == obj.namespace