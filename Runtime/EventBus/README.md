# Event Bus

This package provides the AXI runtime event model and deterministic
synchronous event bus.

- `Event` is an immutable runtime event with identifiers, timestamps,
  source, payload, and metadata.
- `Subscriber` defines a handler and one or more named event types.
- `EventBus` manages subscriber registration and synchronous event
  delivery without introducing dependency resolution, orchestration, or
  persistence concerns.
