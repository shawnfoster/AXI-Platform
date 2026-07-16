"""
AXI Platform Runtime

Capability

Canonical runtime representation of an AXI capability.

A capability represents a stable business concept that may be
implemented by one or more PlatformObjects.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Capability:
    """
    Canonical runtime capability.
    """

    capability_id: str

    name: str

    description: str = ""

    version: str = "1.0"

    status: str = "Draft"

    implements: set[str] = field(default_factory=set)

    depends_on: set[str] = field(default_factory=set)

    metadata: dict[str, object] = field(default_factory=dict)

    def add_object(self, object_id: str) -> None:
        """
        Register a PlatformObject implementation.
        """
        self.implements.add(object_id)

    def remove_object(self, object_id: str) -> None:
        """
        Remove a PlatformObject implementation.
        """
        self.implements.discard(object_id)

    def add_dependency(self, capability_id: str) -> None:
        """
        Register a dependency.
        """
        self.depends_on.add(capability_id)

    def remove_dependency(self, capability_id: str) -> None:
        """
        Remove a dependency.
        """
        self.depends_on.discard(capability_id)

    def to_dict(self) -> dict[str, object]:
        """
        Serialize the capability.
        """
        return {
            "capability_id": self.capability_id,
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "status": self.status,
            "implements": sorted(self.implements),
            "depends_on": sorted(self.depends_on),
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Capability":
        """
        Deserialize a capability.
        """
        return cls(
            capability_id=data["capability_id"],
            name=data["name"],
            description=data.get("description", ""),
            version=data.get("version", "1.0"),
            status=data.get("status", "Draft"),
            implements=set(data.get("implements", [])),
            depends_on=set(data.get("depends_on", [])),
            metadata=dict(data.get("metadata", {})),
        )