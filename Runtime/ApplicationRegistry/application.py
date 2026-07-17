"""
AXI Platform Runtime

Application

Canonical runtime representation of an AXI application.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from Runtime.ObjectModel.platform_object import PlatformObject


@dataclass(slots=True)
class Application(PlatformObject):
    """
    Canonical runtime application.
    """

    services: list[str] = field(default_factory=list)
    plugins: list[str] = field(default_factory=list)

    @property
    def application_id(self) -> str:
        """
        Application identifier mapped to the platform object identifier.
        """
        return self.object_id

    @property
    def lifecycle_state(self) -> str:
        """
        Lifecycle state stored in application metadata.
        """
        value = self.metadata.get("lifecycle_state", "")
        return value if isinstance(value, str) else ""

    @lifecycle_state.setter
    def lifecycle_state(self, value: str) -> None:
        """
        Update the lifecycle state in application metadata.
        """
        self.metadata["lifecycle_state"] = value

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the runtime application.
        """
        data = PlatformObject.to_dict(self)
        data["application_id"] = self.application_id
        data["services"] = list(self.services)
        data["plugins"] = list(self.plugins)
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Application":
        """
        Deserialize a runtime application.
        """
        return cls(
            object_id=data.get("object_id", data["application_id"]),
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
            services=data.get("services", []),
            plugins=data.get("plugins", []),
        )
