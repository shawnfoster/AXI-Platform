"""
AXI Platform Runtime

Subscriber

Subscriber definition used by the AXI Event Bus.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Any

from Runtime.EventBus.event import Event
from Runtime.exceptions import RegistryError


def _freeze_metadata(metadata: Mapping[str, Any]) -> Mapping[str, Any]:
    """
    Freeze subscriber metadata for deterministic runtime behavior.
    """
    return MappingProxyType(dict(metadata))


@dataclass(frozen=True, slots=True)
class Subscriber:
    """
    Immutable event subscriber.
    """

    subscriber_id: str
    event_types: tuple[str, ...]
    handler: Callable[[Event], None]
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Validate and normalize subscriber fields.
        """
        if not isinstance(self.subscriber_id, str) or not self.subscriber_id:
            raise RegistryError(
                "Invalid subscriber registration: subscriber_id is required"
            )

        if not self.event_types:
            raise RegistryError(
                "Invalid subscriber registration: event_types are required"
            )

        normalized_event_types = tuple(sorted(set(self.event_types)))

        if any(
            not isinstance(event_type, str) or not event_type
            for event_type in normalized_event_types
        ):
            raise RegistryError(
                "Invalid subscriber registration: event_types must be strings"
            )

        if not callable(self.handler):
            raise RegistryError(
                "Invalid subscriber registration: handler must be callable"
            )

        if not isinstance(self.metadata, Mapping):
            raise RegistryError(
                "Invalid subscriber metadata: metadata must be a mapping"
            )

        object.__setattr__(self, "event_types", normalized_event_types)
        object.__setattr__(self, "metadata", _freeze_metadata(self.metadata))

    def handles(self, event_type: str) -> bool:
        """
        Determine whether this subscriber handles an event type.
        """
        return event_type in self.event_types
