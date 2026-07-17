# AXI Application Registry Contract

**Version:** 1.0.0
**Status:** Approved
**Authority:** AXI Platform Governance

---

# Purpose

Define the minimum runtime contract required for `M14 Application
Registry`.

This contract documents the minimum public API boundary, registration
behavior, lookup behavior, lifecycle behavior, dependency behavior, and
error behavior required by the published work item.

---

# Repository Evidence

`Governance/WorkQueue/M14-Application-Registry.md` requires the
following public APIs:

- `register_application()`
- `unregister_application()`
- `lookup_application()`
- `list_applications()`
- `update_application()`
- `start_application()`
- `stop_application()`
- `restart_application()`

`M14` also requires the registry to:

- preserve application metadata
- preserve lifecycle state
- expose application capabilities
- integrate with dependency resolution
- integrate with validation

`M14` requires rejection of:

- duplicate application identifiers
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
  boundary used by `M14`.
- `AXI-SCH-007 Platform Object` publishes common field semantics used by
  existing runtime objects.

---

# Scope

This contract applies to:

- the public Application Registry API
- application registration and lookup behavior
- application lifecycle behavior
- application dependency and validation behavior

This contract does not define runtime algorithms or storage layouts.

---

# Public API Boundary

Exact Python signatures and concrete return container types are not
published by current repository evidence.

The public API names and behavior boundaries required by current
repository evidence are:

| API | Input Boundary | Output Boundary | Required Behavior |
| --- | --- | --- | --- |
| `register_application()` | An application input containing the fields required by `M14` | Successful completion leaves the application registered by `application_id` | Registration preserves metadata and lifecycle state and does not succeed for duplicates, invalid metadata, or unresolved dependencies |
| `unregister_application()` | An `application_id` input | Successful completion removes the application from registry-managed runtime state | Registry-style unregister behavior remains idempotent for missing identifiers |
| `lookup_application()` | An `application_id` input | A read-only lookup result compatible with the registry boundary | Lookup does not mutate runtime state |
| `list_applications()` | Registry-managed runtime state | Deterministic collection of registered applications | Listing is read-only |
| `update_application()` | An existing `application_id` plus updated application data | Successful completion updates an existing application record | Missing keys fail with existing registry update behavior |
| `start_application()` | An existing `application_id` input | Successful completion performs the application start lifecycle operation | Invalid lifecycle transitions are rejected |
| `stop_application()` | An existing `application_id` input | Successful completion performs the application stop lifecycle operation | Invalid lifecycle transitions are rejected |
| `restart_application()` | An existing `application_id` input | Successful completion performs the application restart lifecycle operation | Invalid lifecycle transitions are rejected |

---

# Registration Behavior

Under `ADR-0006`, the Application Registry shall preserve shared
registry behavior governed by `REGISTER_CONTRACT` where that behavior
applies to the domain-specific application APIs.

Repository-backed registration expectations are:

- `application_id` is the public registration key required by `M14`.
- Registered application identifiers are unique within a registry
  instance.
- Duplicate registration fails with existing duplicate registration
  behavior.
- Successful registration preserves the application metadata and
  `lifecycle_state` required by `M14`.
- Shared application fields such as `name`, `version`, `description`,
  `owner`, `capabilities`, `dependencies`, and `metadata` shall remain
  compatible with the published `PlatformObject` field meanings where
  `PlatformObject` is reused.

---

# Lookup Behavior

Repository-backed lookup expectations are:

- Application lookup is keyed by `application_id`.
- Application listing is deterministic.
- Lookup and listing are read-only operations.
- `update_application()` applies only to an existing registered
  application key.

This contract does not publish a specific missing-result representation
for unsuccessful lookups.

---

# Lifecycle Behavior

`M14` requires applications to preserve lifecycle state and requires
invalid lifecycle transitions to be rejected.

This contract does not publish:

- a lifecycle state vocabulary
- a lifecycle transition table
- a lifecycle algorithm beyond the public lifecycle API names required
  by `M14`

---

# Dependency Behavior

Application dependencies shall be interpreted through the published
`DependencyResolver` boundary.

`M14` requires integration with `ServiceRegistry` and `PluginLoader`,
but this contract does not publish additional dependency semantics for the
`services` or `plugins` fields beyond the published work item.

This contract does not authorize an alternative dependency model.

---

# Validation and Schema Behavior

Application inputs shall be validated through the published runtime
validation boundary governed by `ADR-0007`.

The minimum application schema required by `M14` is:

- `AXI-SCH-010 Application`

This schema contains the application fields required by `M14`:

- `application_id`
- `name`
- `version`
- `description`
- `owner`
- `capabilities`
- `dependencies`
- `services`
- `plugins`
- `lifecycle_state`
- `metadata`

This contract does not authorize unpublished fields or unpublished
validation inputs.

---

# Error Behavior

This contract does not require new application-specific exception
classes.

Repository-backed error expectations are:

- duplicate application identifiers shall fail with existing duplicate
  registration behavior where registry-style registration applies
- missing-key updates shall fail with `KeyError` or the equivalent
  existing registry update behavior
- unresolved dependencies shall fail with `DependencyError` or an
  equivalent published dependency validation failure
- invalid metadata and invalid lifecycle transitions shall fail
  validation and shall not result in successful registration, update,
  or lifecycle operations

`M14` requires the registry to reuse existing platform exceptions
whenever appropriate.

---

# Future Guidance

Future governance may publish:

- exact method signatures
- concrete return types
- additional lifecycle states
- event contracts
- persistence behavior
- orchestration behavior

Those items are not approved by this contract.

---

# Related

- `Governance/ADR/ADR-0009_Application_Registry_Boundary.md`
- `Governance/ADR/ADR-0006_Generic_Registry_Pattern.md`
- `Governance/ADR/ADR-0007_Runtime_Validation_Framework.md`
- `Governance/ADR/ADR-0008_Plugin_Loader_Boundary.md`
- `Governance/WorkQueue/M14-Application-Registry.md`
- `Governance/Contracts/REGISTER_CONTRACT.md`
- `Governance/Contracts/SERVICE_CONTRACT.md`
- `Governance/Contracts/PLUGIN_CONTRACT.md`
