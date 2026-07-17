"""
AXI Platform Runtime

Dependency

Immutable dependency relationship used by the AXI Dependency Resolver.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Any

from Runtime.CapabilityRegistry.capability import Capability
from Runtime.ObjectModel.platform_object import PlatformObject
from Runtime.exceptions import DependencyError


def _freeze_value(value: Any) -> Any:
    """
    Recursively freeze dependency metadata values.
    """
    if isinstance(value, Mapping):
        return MappingProxyType(
            {
                key: _freeze_value(nested_value)
                for key, nested_value in value.items()
            }
        )

    if isinstance(value, list | tuple):
        return tuple(_freeze_value(item) for item in value)

    if isinstance(value, set | frozenset):
        return frozenset(_freeze_value(item) for item in value)

    return value


@dataclass(frozen=True, slots=True)
class Dependency:
    """
    Immutable dependency relationship between two runtime identifiers.
    """

    source: str | PlatformObject | Capability
    target: str | PlatformObject | Capability
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Validate and normalize dependency fields.
        """
        normalized_source = self.normalize_reference(self.source)
        normalized_target = self.normalize_reference(self.target)

        if normalized_source == normalized_target:
            raise DependencyError(
                f"Circular dependency detected: '{normalized_source}'"
            )

        if not isinstance(self.metadata, Mapping):
            raise DependencyError(
                "Invalid dependency definition: metadata must be a mapping"
            )

        object.__setattr__(self, "source", normalized_source)
        object.__setattr__(self, "target", normalized_target)
        object.__setattr__(
            self,
            "metadata",
            _freeze_value(self.metadata),
        )

    @property
    def dependency_id(self) -> str:
        """
        Deterministic dependency identifier.
        """
        return f"{self.source}->{self.target}"

    @staticmethod
    def normalize_reference(
        value: str | PlatformObject | Capability,
    ) -> str:
        """
        Normalize a dependency reference to a stable identifier.
        """
        if isinstance(value, PlatformObject):
            return value.object_id

        if isinstance(value, Capability):
            return value.capability_id

        if isinstance(value, str) and value:
            return value

        raise DependencyError(
            "Invalid dependency definition: references must be identifiers"
        )
