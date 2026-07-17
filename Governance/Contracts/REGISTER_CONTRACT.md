# AXI Register Contract

**Version:** 1.0.0
**Status:** Approved
**Authority:** AXI Platform Governance

---

# Purpose

Define the runtime contract shared by the AXI Registry Foundation and
specialized registries that build on it.

This contract is derived from the implemented repository behavior in:

- `Runtime/Registry/base_registry.py`
- `Runtime/ObjectRegistry/registry.py`
- `Governance/ADR/ADR-0006_Generic_Registry_Pattern.md`

---

# Repository Evidence

The repository currently publishes the following registry-foundation
evidence:

- `BaseRegistry` exposes `register(key, item)`, `unregister(key)`,
  `get(key)`, `update(key, item)`, `exists(key)`, `keys()`, `values()`,
  `items()`, `count()`, `clear()`, and `load(...)`.
- `BaseRegistry.register()` rejects duplicate keys with
  `DuplicateRegistrationError`.
- `BaseRegistry.unregister()` ignores missing keys.
- `BaseRegistry.update()` raises `KeyError` for a missing key.
- `BaseRegistry.keys()` returns keys in sorted order.
- `BaseRegistry.load()` delegates duplicate handling to
  `BaseRegistry.register()`.
- `ObjectRegistry`, `CapabilityRegistry`, and `ServiceRegistry` reuse
  `BaseRegistry` while exposing domain-specific public methods.
- `ADR-0006` requires future runtime registries to inherit from
  `BaseRegistry` unless a documented exception is approved.

---

# Scope

This contract applies to:

- `BaseRegistry`
- `ObjectRegistry`
- `CapabilityRegistry`
- `ServiceRegistry`

If later registries inherit from `BaseRegistry` under `ADR-0006`, this
contract is the shared contract baseline for them.

---

# Contract Statements

A conforming AXI runtime registry shall preserve the shared foundation
behaviors evidenced in `BaseRegistry`:

- Registration keys are unique within a registry instance.
- Duplicate registration raises `DuplicateRegistrationError`.
- `unregister()` is idempotent for missing keys.
- `update()` requires an existing key and raises `KeyError` if absent.
- `keys()` returns keys in deterministic sorted order.
- `load(...)` applies the same duplicate protection as `register(...)`.

Specialized registries may expose domain-specific registration methods
instead of the raw `register(key, item)` signature, but they shall
preserve the shared behaviors above.

---

# Implementation Guidance

If the validation framework validates this contract, the
repository-backed shared checks include:

- duplicate registration behavior
- missing-key update behavior
- deterministic key ordering
- use of `BaseRegistry` as the shared registry foundation where
  `ADR-0006` applies

# Related

- `ADR-0006`
- `Runtime/Registry/base_registry.py`
- `Runtime/ObjectRegistry/registry.py`
