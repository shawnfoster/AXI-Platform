from __future__ import annotations

from datetime import UTC, datetime

import pytest

from Runtime.EventBus import Event, EventBus, Subscriber
from Runtime.ServiceRegistry import Service
from Runtime.exceptions import AXIRuntimeError, DuplicateRegistrationError, RegistryError


def build_service(i: int) -> Service:
    return Service(
        object_id=f"OBJ-{i:06d}",
        namespace="AXI-SVC",
        object_type="Service",
        name=f"Service {i}",
        version="1.0",
        status="Approved",
        owner="Platform",
        metadata={
            "lifecycle_state": "Registered",
            "transport": "in-process",
        },
    )


def build_subscriber(
    subscriber_id: str,
    event_types: tuple[str, ...],
    handler,
) -> Subscriber:
    return Subscriber(
        subscriber_id=subscriber_id,
        event_types=event_types,
        handler=handler,
        metadata={"owner": "test"},
    )


def test_event_defaults_identifier_timestamp_and_source_normalization() -> None:
    service = build_service(1)
    event = Event(
        event_type="service.started",
        source=service,
        payload={"state": "running", "steps": [1, 2]},
        metadata={"attempt": 1},
    )

    assert event.event_id.startswith("EVT-")
    assert isinstance(event.timestamp, datetime)
    assert event.source == service.service_id
    assert event.payload["state"] == "running"
    assert event.payload["steps"] == (1, 2)
    assert dict(event.metadata) == {"attempt": 1}

    with pytest.raises(TypeError):
        event.metadata["attempt"] = 2


def test_event_bus_publish_and_dispatch_are_synchronous_and_deterministic() -> None:
    bus = EventBus()
    received: list[str] = []

    def second_handler(event: Event) -> None:
        received.append(f"second:{event.event_type}")

    def first_handler(event: Event) -> None:
        received.append(f"first:{event.event_type}")

    bus.subscribe(
        build_subscriber(
            "SUB-010",
            ("service.started",),
            second_handler,
        )
    )
    bus.subscribe(
        build_subscriber(
            "SUB-001",
            ("service.started",),
            first_handler,
        )
    )

    bus.publish(
        Event(
            event_type="service.started",
            source=build_service(2),
            payload={"state": "running"},
        )
    )

    assert received == [
        "first:service.started",
        "second:service.started",
    ]


def test_event_bus_unsubscribe_and_clear_remove_subscribers() -> None:
    bus = EventBus()
    received: list[str] = []

    def handler(event: Event) -> None:
        received.append(event.event_type)

    subscriber = build_subscriber(
        "SUB-100",
        ("service.started",),
        handler,
    )

    bus.subscribe(subscriber)
    assert bus.has_subscribers("service.started")

    bus.unsubscribe(subscriber.subscriber_id)
    assert not bus.has_subscribers("service.started")
    assert bus.list_subscribers("service.started") == []

    bus.subscribe(subscriber)
    bus.clear()
    bus.publish(
        Event(
            event_type="service.started",
            source="AXI-SVC",
            payload={"state": "running"},
        )
    )

    assert received == []
    assert bus.list_subscribers() == []


def test_event_bus_supports_multiple_event_types() -> None:
    bus = EventBus()
    received: list[str] = []

    def handler(event: Event) -> None:
        received.append(event.event_type)

    bus.subscribe(
        build_subscriber(
            "SUB-200",
            ("service.started", "service.stopped"),
            handler,
        )
    )

    bus.dispatch(
        Event(
            event_type="service.started",
            source="AXI-SVC",
            payload={"state": "running"},
        )
    )
    bus.publish(
        Event(
            event_type="service.stopped",
            source="AXI-SVC",
            payload={"state": "stopped"},
            timestamp=datetime.now(UTC),
        )
    )

    assert received == ["service.started", "service.stopped"]
    assert [subscriber.subscriber_id for subscriber in bus.list_subscribers()] == [
        "SUB-200"
    ]


def test_event_bus_rejects_invalid_event_definitions() -> None:
    with pytest.raises(AXIRuntimeError):
        Event(
            event_type="",
            source="AXI-SVC",
        )

    with pytest.raises(AXIRuntimeError):
        Event(
            event_type="service.started",
            source="AXI-SVC",
            payload={"handler": lambda event: event},
        )

    with pytest.raises(AXIRuntimeError):
        Event(
            event_type="service.started",
            source="",
        )


def test_event_bus_rejects_invalid_subscribers_and_duplicates() -> None:
    bus = EventBus()

    with pytest.raises(RegistryError):
        Subscriber(
            subscriber_id="SUB-300",
            event_types=(),
            handler=lambda event: None,
        )

    with pytest.raises(RegistryError):
        Subscriber(
            subscriber_id="SUB-301",
            event_types=("service.started",),
            handler="not-callable",
        )

    subscriber = build_subscriber(
        "SUB-302",
        ("service.started",),
        lambda event: None,
    )
    bus.subscribe(subscriber)

    with pytest.raises(DuplicateRegistrationError):
        bus.subscribe(subscriber)


def test_event_bus_reports_empty_subscriber_lists() -> None:
    bus = EventBus()

    assert not bus.has_subscribers("service.started")
    assert bus.list_subscribers() == []
    assert bus.list_subscribers("service.started") == []
