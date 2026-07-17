# Service Registry

This package provides the AXI runtime service model and service
registry.

- `Service` extends `PlatformObject` and preserves service lifecycle
  state in metadata while keeping the platform object schema intact.
- `ServiceRegistry` is the `BaseRegistry` specialization that manages
  service registration, lookup, update, removal, metadata validation,
  and capability-registry integration.
