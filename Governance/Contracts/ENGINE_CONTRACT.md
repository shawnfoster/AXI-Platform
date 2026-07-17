# AXI Engine Registry Contract

**Version:** 1.0.0
**Status:** Approved
**Authority:** AXI Platform Governance

---

# Purpose

Define the minimum runtime contract required for `M15 Engine Registry`.

This contract documents the minimum public API boundary, registration
behavior, lookup behavior, lifecycle behavior, dependency behavior,
validation behavior, and integration limits required by the published
work item.

---

# Repository Evidence

`Governance/WorkQueue/M15-Engine-Registry.md` requires the following
public APIs:

- `register_engine()`
- `unregister_engine()`
- `lookup_engine()`
- `list_engines()`
- `update_engine()`
- `start_engine()`
- `stop_engine()`
- `restart_engine()`

`M15` also requires the registry to:

- preserve engine metadata
- preserve lifecycle state
- expose capabilities
- integrate with dependency resolution
- integrate with validation
- support future scheduling

`M15` requires rejection of:

- duplicate engine identifiers
- invalid metadata
- invalid lifecycle transitions
- unresolved dependencies

Existing repository evidence relevant to this contract includes:

- `ADR-0006` requires future runtime registries to inherit from
  `BaseRegistry` unless a documented exception is approved.
- `BaseRegistry.register()` rejects duplicate keys with
  `DuplicateRegistrationError`.
- `BaseRegistry.unregister()` ignores missing keys.
- `BaseRegistry.update()` raises `KeyError` for a missing key.
- `DependencyResolver` validates dependency references and raises
  `DependencyError` for unresolved or circular dependencies.
- `ADR-0007` limits runtime validation to published governance artifacts
  and public validation interfaces.
- `ADR-0008` and `PLUGIN_CONTRACT` define the published Plugin Loader
  boundary used by `M15`.
- `ADR-0009` and `APPLICATION_CONTRACT` define the published Application
  Registry boundary used by `M15`.
- `AXI-SCH-007 Platform Object` publishes the shared object fields and
  the `AXI-ENG` namespace with the `Engine` object type.

---

# Scope

This contract applies to:

- the public Engine Registry API
- engine registration and lookup behavior
- engine lifecycle behavior
- engine dependency and validation behavior

This contract does not define runtime algorithms or storage layouts.

---

# Public API Boundary

Exact Python signatures and concrete return container types are not
published by current repository evidence.

The public API names and behavior boundaries required by current
repository evidence are:

| API | Input Boundary | Output Boundary | Required Behavior |
| --- | --- | --- | --- |
| `register_engine()` | An engine input containing the fields required by `M15` | Successful completion leaves the engine registered by `engine_id` | Registration preserves metadata and lifecycle state and does not succeed for duplicates, invalid metadata, or unresolved dependencies |
| `unregister_engine()` | An `engine_id` input | Successful completion removes the engine from registry-managed runtime state | Registry-style unregister behavior remains idempotent for missing identifiers |
| `lookup_engine()` | An `engine_id` input | A read-only lookup result compatible with the registry boundary | Lookup does not mutate runtime state |
| `list_engines()` | Registry-managed runtime state | Deterministic collection of registered engines | Listing is read-only |
| `update_engine()` | An existing `engine_id` plus updated engine data | Successful completion updates an existing engine record | Missing keys fail with existing registry update behavior |
| `start_engine()` | An existing `engine_id` input | Successful completion performs the engine start lifecycle operation | Invalid lifecycle transitions are rejected |
| `stop_engine()` | An existing `engine_id` input | Successful completion performs the engine stop lifecycle operation | Invalid lifecycle transitions are rejected |
| `restart_engine()` | An existing `engine_id` input | Successful completion performs the engine restart lifecycle operation | Invalid lifecycle transitions are rejected |

---

# Registration Behavior

Under `ADR-0006`, the Engine Registry shall preserve shared registry
behavior governed by `REGISTER_CONTRACT` where that behavior applies to
the domain-specific engine APIs.

Repository-backed registration expectations are:

- `engine_id` is the public registration key required by `M15`.
- Registered engine identifiers are unique within a registry instance.
- Duplicate registration fails with existing duplicate registration
  behavior.
- Successful registration preserves the engine metadata and
  `lifecycle_state` required by `M15`.
- Shared engine fields such as `name`, `version`, `description`,
  `owner`, `capabilities`, `dependencies`, `status`, and `metadata`
  shall remain compatible with the published `PlatformObject` field
  meanings where `PlatformObject` is reused.

---

# Lookup Behavior

Repository-backed lookup expectations are:

- Engine lookup is keyed by `engine_id`.
- Engine listing is deterministic.
- Lookup and listing are read-only operations.
- `update_engine()` applies only to an existing registered engine key.

This contract does not publish a specific missing-result representation
for unsuccessful lookups.

---

# Lifecycle Behavior

`M15` requires engines to preserve lifecycle state and requires invalid
lifecycle transitions to be rejected.

This contract does not publish:

- a lifecycle state vocabulary
- a lifecycle transition table
- a lifecycle algorithm beyond the public lifecycle API names required
  by `M15`

---

# Dependency Behavior

Engine dependencies shall be interpreted through the published
`DependencyResolver` boundary.

`M15` requires integration with `ServiceRegistry`, `PluginLoader`, and
`ApplicationRegistry`, but this contract does not publish additional
dependency semantics for those integrations beyond the published work
item and approved upstream boundaries.

This contract does not authorize an alternative dependency model.

---

# Validation and Schema Behavior

Engine inputs shall be validated through the published runtime
validation boundary governed by `ADR-0007`.

The minimum engine schema required by `M15` is:

- `AXI-SCH-011 Engine`

This schema contains the engine fields required by `M15`:

- `engine_id`
- `name`
- `version`
- `description`
- `owner`
- `capabilities`
- `dependencies`
- `lifecycle_state`
- `status`
- `metadata`

This contract does not authorize unpublished fields or unpublished
validation inputs.

---

# Scheduling Boundary

`M15` requires the registry to support future scheduling.

Repository-backed support for that requirement is limited to preserving
engine metadata and runtime state in a way that later governance can
reuse.

This contract does not publish:

- scheduling APIs
- scheduling metadata keys
- queue semantics
- timers or triggers
- orchestration policies

---

# Error Behavior

This contract does not require new engine-specific exception classes.

Repository-backed error expectations are:

- duplicate engine identifiers shall fail with existing duplicate
  registration behavior where registry-style registration applies
- missing-key updates shall fail with `KeyError` or the equivalent
  existing registry update behavior
- unresolved dependencies shall fail with `DependencyError` or an
  equivalent published dependency validation failure
- invalid metadata and invalid lifecycle transitions shall fail
  validation and shall not result in successful registration, update,
  or lifecycle operations

`M15` requires the registry to reuse existing platform exceptions
whenever appropriate.

---

# Future Guidance

Future governance may publish:

- exact method signatures
- concrete return types
- additional lifecycle states
- event contracts
- persistence behavior
- scheduling semantics
- orchestration behavior

Those items are not approved by this contract.

---

# Related

- `Governance/ADR/ADR-0010_Engine_Registry_Boundary.md`
- `Governance/ADR/ADR-0006_Generic_Registry_Pattern.md`
- `Governance/ADR/ADR-0007_Runtime_Validation_Framework.md`
- `Governance/ADR/ADR-0008_Plugin_Loader_Boundary.md`
- `Governance/ADR/ADR-0009_Application_Registry_Boundary.md`
- `Governance/WorkQueue/M15-Engine-Registry.md`
- `Governance/Contracts/REGISTER_CONTRACT.md`
- `Governance/Contracts/SERVICE_CONTRACT.md`
- `Governance/Contracts/PLUGIN_CONTRACT.md`
- `Governance/Contracts/APPLICATION_CONTRACT.md`
- `Governance/Schemas/AXI-SCH-007_Platform_Object.json`
