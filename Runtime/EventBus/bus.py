"""
AXI Platform Runtime

Event Bus

Deterministic synchronous publish/subscribe event bus.
"""

from __future__ import annotations

from Runtime.EventBus.event import Event
from Runtime.EventBus.subscriber import Subscriber
from Runtime.Registry.base_registry import BaseRegistry
from Runtime.exceptions import AXIRuntimeError, RegistryError


class EventBus:
    """
    Deterministic synchronous runtime event bus.
    """

    def __init__(self) -> None:
        """Initialize an empty event bus."""
        self._subscribers = BaseRegistry[Subscriber]()
        self._event_subscribers: dict[str, list[str]] = {}

    def publish(self, event: Event) -> None:
        """
        Publish an event synchronously.
        """
        self._validate_event(event)
        self.dispatch(event)

    def subscribe(self, subscriber: Subscriber) -> None:
        """
        Register a subscriber for one or more event types.
        """
        if not isinstance(subscriber, Subscriber):
            raise RegistryError(
                "Invalid subscriber registration: expected Subscriber"
            )

        self._subscribers.register(subscriber.subscriber_id, subscriber)

        for event_type in subscriber.event_types:
            subscriber_ids = self._event_subscribers.setdefault(
                event_type,
                [],
            )
            subscriber_ids.append(subscriber.subscriber_id)
            subscriber_ids.sort()

    def unsubscribe(self, subscriber_id: str) -> None:
        """
        Remove a subscriber by identifier.
        """
        subscriber = self._subscribers.get(subscriber_id)

        if subscriber is None:
            return

        for event_type in subscriber.event_types:
            subscriber_ids = self._event_subscribers.get(event_type, [])

            if subscriber_id in subscriber_ids:
                subscriber_ids.remove(subscriber_id)

            if not subscriber_ids:
                self._event_subscribers.pop(event_type, None)

        self._subscribers.unregister(subscriber_id)

    def dispatch(self, event: Event) -> None:
        """
        Deliver an event to matching subscribers in deterministic order.
        """
        self._validate_event(event)

        for subscriber in self.list_subscribers(event.event_type):
            subscriber.handler(event)

    def has_subscribers(self, event_type: str) -> bool:
        """
        Determine whether any subscribers exist for an event type.
        """
        self._validate_event_type(event_type)
        return bool(self._event_subscribers.get(event_type))

    def list_subscribers(
        self,
        event_type: str | None = None,
    ) -> list[Subscriber]:
        """
        Return subscribers in deterministic order.
        """
        if event_type is None:
            return [
                self._require_subscriber(subscriber_id)
                for subscriber_id in self._subscribers.keys()
            ]

        self._validate_event_type(event_type)

        return [
            self._require_subscriber(subscriber_id)
            for subscriber_id in self._event_subscribers.get(event_type, [])
        ]

    def clear(self) -> None:
        """
        Remove every registered subscriber.
        """
        self._event_subscribers.clear()
        self._subscribers.clear()

    def _require_subscriber(self, subscriber_id: str) -> Subscriber:
        """
        Retrieve a registered subscriber.
        """
        subscriber = self._subscribers.get(subscriber_id)

        if subscriber is None:
            raise RegistryError(
                f"Subscriber registry is inconsistent: '{subscriber_id}'"
            )

        return subscriber

    @staticmethod
    def _validate_event(event: Event) -> None:
        """
        Validate an event instance before publication.
        """
        if not isinstance(event, Event):
            raise AXIRuntimeError(
                "Invalid event definition: expected Event"
            )

    @staticmethod
    def _validate_event_type(event_type: str) -> None:
        """
        Validate an event type identifier.
        """
        if not isinstance(event_type, str) or not event_type:
            raise AXIRuntimeError(
                "Invalid event definition: event_type is required"
            )
