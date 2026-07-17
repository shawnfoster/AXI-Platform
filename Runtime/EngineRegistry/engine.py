"""
AXI Platform Runtime

Engine

Canonical runtime representation of an AXI engine.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from Runtime.ObjectModel.platform_object import PlatformObject


@dataclass(slots=True)
class Engine(PlatformObject):
    """
    Canonical runtime engine.
    """

    @property
    def engine_id(self) -> str:
        """
        Engine identifier mapped to the platform object identifier.
        """
        return self.object_id

    @property
    def lifecycle_state(self) -> str:
        """
        Lifecycle state stored in engine metadata.
        """
        value = self.metadata.get("lifecycle_state", "")
        return value if isinstance(value, str) else ""

    @lifecycle_state.setter
    def lifecycle_state(self, value: str) -> None:
        """
        Update the lifecycle state in engine metadata.
        """
        self.metadata["lifecycle_state"] = value

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the runtime engine.
        """
        data = PlatformObject.to_dict(self)
        data["engine_id"] = self.engine_id
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Engine":
        """
        Deserialize a runtime engine.
        """
        return cls(
            object_id=data.get("object_id", data["engine_id"]),
            namespace=data["namespace"],
            object_type=data["object_type"],
            name=data["name"],
            description=data.get("description", ""),
            version=data["version"],
            status=data["status"],
            owner=data["owner"],
            capabilities=data.get("capabilities", []),
            contracts=data.get("contracts", []),
            schemas=data.get("schemas", []),
            adr_refs=data.get("adr_refs", []),
            dependencies=data.get("dependencies", []),
            provenance=data.get("provenance", {}),
            metadata=data.get("metadata", {}),
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )
