"""
AXI Platform Runtime

Platform Object

Every governed artifact within the AXI Platform derives from
PlatformObject.

AXI-SCH-007 governs the canonical metadata model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass(slots=True)
class PlatformObject:
    """
    Base runtime object for all governed AXI artifacts.
    """

    object_id: str
    namespace: str
    object_type: str

    name: str
    version: str

    status: str
    owner: str

    description: str = ""

    capabilities: list[str] = field(default_factory=list)

    contracts: list[str] = field(default_factory=list)

    schemas: list[str] = field(default_factory=list)

    adr_refs: list[str] = field(default_factory=list)

    dependencies: list[str] = field(default_factory=list)

    provenance: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def touch(self) -> None:
        """
        Update modification timestamp.
        """
        self.updated_at = datetime.now(UTC)

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize object.
        """

        return {
            "object_id": self.object_id,
            "namespace": self.namespace,
            "object_type": self.object_type,
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "status": self.status,
            "owner": self.owner,
            "capabilities": self.capabilities,
            "contracts": self.contracts,
            "schemas": self.schemas,
            "adr_refs": self.adr_refs,
            "dependencies": self.dependencies,
            "provenance": self.provenance,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PlatformObject":
        """
        Deserialize object.
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