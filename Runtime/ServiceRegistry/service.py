"""
AXI Platform Runtime

Service

Canonical runtime representation of an AXI service.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from Runtime.ObjectModel.platform_object import PlatformObject


@dataclass(slots=True)
class Service(PlatformObject):
    """
    Canonical runtime service.
    """

    @property
    def service_id(self) -> str:
        """
        Service identifier mapped to the platform object identifier.
        """
        return self.object_id

    @property
    def lifecycle_state(self) -> str:
        """
        Lifecycle state stored in service metadata.
        """
        value = self.metadata.get("lifecycle_state", "")
        return value if isinstance(value, str) else ""

    @lifecycle_state.setter
    def lifecycle_state(self, value: str) -> None:
        """
        Update the lifecycle state in service metadata.
        """
        self.metadata["lifecycle_state"] = value

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Service":
        """
        Deserialize a runtime service.
        """
        return cls(
            object_id=data["object_id"],
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
