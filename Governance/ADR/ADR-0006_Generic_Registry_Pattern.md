# ADR-0006 — Adopt Generic Registry Pattern

## Status

Accepted

---

## Context

The AXI Runtime requires multiple registries:

- Object Registry
- Capability Registry
- Engine Registry
- Service Registry
- Application Registry

Each registry originally duplicated common behaviors:

- register
- unregister
- exists
- get
- list
- count
- clear

---

## Decision

Introduce a generic `BaseRegistry` that owns common registry behavior.

Specialized registries inherit from `BaseRegistry` and implement only domain-specific behavior.

Example:

BaseRegistry
↓
ObjectRegistry
CapabilityRegistry
ServiceRegistry
EngineRegistry
ApplicationRegistry

---

## Rationale

Benefits include:

- Reduced duplication
- Consistent runtime API
- Easier testing
- Improved maintainability
- Cleaner separation of concerns

---

## Consequences

Future runtime registries SHALL inherit from `BaseRegistry` unless a documented exception is approved through the ADR process.

---

## Related

- ADR-0002
- ADR-0005
- M6 Platform Object Model
- M7 Capability Registry