"""
AXI Platform Runtime

Capability Registry

Registry of AXI capabilities.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from Runtime.CapabilityRegistry.capability import Capability
from Runtime.ObjectModel.platform_object import PlatformObject
from Runtime.Registry.base_registry import BaseRegistry
from Runtime.exceptions import CapabilityNotFoundError


class CapabilityRegistry(BaseRegistry[Capability]):
    """
    Registry of capabilities keyed by capability_id.
    """

    def register(self, capability: Capability) -> None:
        """
        Register a capability using its capability_id.
        """
        super().register(capability.capability_id, capability)

    def update(self, capability: Capability) -> None:
        """
        Replace an existing capability definition.
        """
        try:
            super().update(capability.capability_id, capability)
        except KeyError as exc:
            raise CapabilityNotFoundError(
                f"Capability not found: '{capability.capability_id}'"
            ) from exc

    def remove(self, capability_id: str) -> None:
        """
        Remove a capability by identifier.
        """
        self.unregister(capability_id)

    def load(self, capabilities: Iterable[Capability]) -> None:
        """
        Bulk load capabilities.
        """
        for capability in capabilities:
            self.register(capability)

    def require(self, capability_id: str) -> Capability:
        """
        Retrieve a capability or raise if it is missing.
        """
        capability = self.get(capability_id)

        if capability is None:
            raise CapabilityNotFoundError(
                f"Capability not found: '{capability_id}'"
            )

        return capability

    def list_capabilities(self) -> list[Capability]:
        """
        Return capabilities in deterministic identifier order.
        """
        return [self.require(capability_id) for capability_id in self.keys()]

    def add_implementation(
        self,
        capability_id: str,
        obj: PlatformObject,
    ) -> None:
        """
        Associate a PlatformObject implementation to a capability.
        """
        self.require(capability_id).add_implementation(obj)

    def remove_implementation(
        self,
        capability_id: str,
        obj: PlatformObject,
    ) -> None:
        """
        Remove a PlatformObject implementation from a capability.
        """
        self.require(capability_id).remove_implementation(obj)

    def to_dict(self) -> list[dict[str, Any]]:
        """
        Serialize the registry to ordered capability dictionaries.
        """
        return [
            capability.to_dict()
            for capability in self.list_capabilities()
        ]

    @classmethod
    def from_dict(
        cls,
        data: Iterable[dict[str, Any]],
    ) -> "CapabilityRegistry":
        """
        Build a registry from serialized capability dictionaries.
        """
        registry = cls()
        registry.load(
            Capability.from_dict(capability_data)
            for capability_data in data
        )
        return registry
