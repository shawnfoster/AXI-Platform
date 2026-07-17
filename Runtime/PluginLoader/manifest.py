"""
AXI Platform Runtime

Plugin Manifest

Immutable runtime representation of an AXI plugin manifest.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Any

from Runtime.exceptions import RegistryError


def _freeze_value(value: Any) -> Any:
    """
    Recursively freeze manifest metadata values.
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


def _thaw_value(value: Any) -> Any:
    """
    Recursively convert frozen manifest values to mutable structures.
    """
    if isinstance(value, Mapping):
        return {
            key: _thaw_value(nested_value)
            for key, nested_value in value.items()
        }

    if isinstance(value, tuple):
        return [_thaw_value(item) for item in value]

    if isinstance(value, frozenset):
        return [_thaw_value(item) for item in sorted(value)]

    return value


@dataclass(frozen=True, slots=True)
class PluginManifest:
    """
    Immutable plugin manifest payload.
    """

    data: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Validate and normalize manifest data.
        """
        if not isinstance(self.data, Mapping):
            raise RegistryError(
                "Invalid plugin manifest: manifest must be a mapping"
            )

        object.__setattr__(
            self,
            "data",
            _freeze_value(dict(self.data)),
        )

    @property
    def plugin_id(self) -> str:
        """
        Return the plugin identifier when present.
        """
        return self._string_field("plugin_id")

    @property
    def name(self) -> str:
        """
        Return the plugin name when present.
        """
        return self._string_field("name")

    @property
    def version(self) -> str:
        """
        Return the plugin version when present.
        """
        return self._string_field("version")

    @property
    def author(self) -> str:
        """
        Return the plugin author when present.
        """
        return self._string_field("author")

    @property
    def description(self) -> str:
        """
        Return the plugin description when present.
        """
        return self._string_field("description")

    @property
    def capabilities(self) -> tuple[str, ...]:
        """
        Return declared capability identifiers.
        """
        return self._string_sequence_field("capabilities")

    @property
    def dependencies(self) -> tuple[str, ...]:
        """
        Return declared dependency identifiers.
        """
        return self._string_sequence_field("dependencies")

    @property
    def lifecycle_state(self) -> str:
        """
        Return the manifest lifecycle state when present.
        """
        return self._string_field("lifecycle_state")

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the manifest payload.
        """
        return _thaw_value(self.data)

    @classmethod
    def from_dict(
        cls,
        data: Mapping[str, Any],
    ) -> "PluginManifest":
        """
        Build a manifest from mapping-shaped data.
        """
        return cls(dict(data))

    def _string_field(self, field_name: str) -> str:
        """
        Read a string field from the manifest payload.
        """
        value = self.data.get(field_name)
        return value if isinstance(value, str) else ""

    def _string_sequence_field(self, field_name: str) -> tuple[str, ...]:
        """
        Read a string sequence field from the manifest payload.
        """
        value = self.data.get(field_name, ())

        if not isinstance(value, Sequence) or isinstance(value, str):
            return ()

        if any(not isinstance(item, str) for item in value):
            return ()

        return tuple(value)
