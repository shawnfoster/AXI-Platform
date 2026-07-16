# Capability Registry

This package provides the AXI runtime capability model and capability
registry.

- `Capability` is the canonical runtime representation of an AXI
  capability governed by `AXI-SCH-008`.
- `CapabilityRegistry` is the `BaseRegistry` specialization that
  manages capability registration, lookup, update, removal, ordered
  enumeration, and serialization.
