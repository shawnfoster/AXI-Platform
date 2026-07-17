"""
AXI Platform Runtime

Event

Immutable runtime event representation used by the AXI Event Bus.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from datetime import UTC, datetime
from types import MappingProxyType
from typing import Any
from uuid import uuid4

from Runtime.ObjectModel.platform_object import PlatformObject
from Runtime.exceptions import AXIRuntimeError


def _freeze_value(value: Any) -> Any:
    """
    Recursively freeze event payload and metadata values.
    """
    if callable(value):
        raise AXIRuntimeError(
            "Invalid event payload: callable values are not supported"
        )

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
class Event:
    """
    Immutable runtime event.
    """

    event_type: str
    source: str | PlatformObject
    payload: Any = None
    metadata: Mapping[str, Any] = field(default_factory=dict)
    event_id: str = field(default_factory=lambda: f"EVT-{uuid4().hex}")
    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def __post_init__(self) -> None:
        """
        Validate and normalize immutable event fields.
        """
        if not isinstance(self.event_type, str) or not self.event_type:
            raise AXIRuntimeError(
                "Invalid event definition: event_type is required"
            )

        normalized_source = self._normalize_source(self.source)

        if not isinstance(self.event_id, str) or not self.event_id:
            raise AXIRuntimeError(
                "Invalid event definition: event_id is required"
            )

        if not isinstance(self.timestamp, datetime):
            raise AXIRuntimeError(
                "Invalid event definition: timestamp must be datetime"
            )

        if not isinstance(self.metadata, Mapping):
            raise AXIRuntimeError(
                "Invalid event metadata: metadata must be a mapping"
            )

        object.__setattr__(self, "source", normalized_source)
        object.__setattr__(self, "payload", _freeze_value(self.payload))
        object.__setattr__(
            self,
            "metadata",
            _freeze_value(self.metadata),
        )

    @staticmethod
    def _normalize_source(source: str | PlatformObject) -> str:
        """
        Normalize an event source to a stable string identifier.
        """
        if isinstance(source, PlatformObject):
            return source.object_id

        if isinstance(source, str) and source:
            return source

        raise AXIRuntimeError(
            "Invalid event definition: source is required"
        )
