# AXI Plugin Loader Contract

**Version:** 1.0.0
**Status:** Approved
**Authority:** AXI Platform Governance

---

# Purpose

Define the minimum runtime contract required for `M13 Plugin Loader`.

This contract documents the approved public API boundary, lifecycle
boundary, registration boundary, dependency interaction, and error
behavior required by the published work item.

---

# Repository Evidence

`Governance/WorkQueue/M13-Plugin-Loader.md` requires the following public
APIs:

- `discover_plugins()`
- `load_plugin()`
- `unload_plugin()`
- `reload_plugin()`
- `validate_plugin()`
- `list_plugins()`

`M13` also requires the loader to:

- register plugins
- preserve plugin metadata
- expose lifecycle state
- support future hot reload
- support dependency resolution
- support validation before loading

`M13` requires rejection of:

- duplicate plugin identifiers
- invalid manifests
- missing metadata
- unresolved dependencies
- validation failures

Existing repository evidence relevant to this contract includes:

- `BaseRegistry.register()` rejects duplicate keys with
  `DuplicateRegistrationError`.
- `DependencyResolver` validates dependency references and raises
  `DependencyError` for unresolved or circular dependencies.
- `ADR-0007` limits runtime validation to published governance artifacts
  and public validation interfaces.
- `AXI-SCH-007 Platform Object` does not publish a plugin namespace or
  plugin object type.

---

# Scope

This contract applies to:

- the public Plugin Loader API
- plugin manifest validation at the loader boundary
- loader-managed plugin registration state

This contract does not define runtime algorithms or storage layouts.

---

# Public API Boundary

Exact Python signatures and concrete return container types are not
published by current repository evidence.

The approved public API names and behavior boundaries are:

| API | Approved Input Boundary | Approved Output Boundary | Required Behavior |
| --- | --- | --- | --- |
| `discover_plugins()` | Loader-managed discovery inputs only | Deterministic collection of discovered plugin records or manifests | Discovery only; no successful load or registration is implied |
| `validate_plugin()` | A discovered plugin input or plugin manifest | Validation outcome compatible with the published validation boundary | Invalid manifests, missing metadata, unresolved dependencies, and validation failures are rejected |
| `load_plugin()` | A plugin input that has satisfied manifest, dependency, and validation requirements | Successful completion leaves the plugin registered in loader-managed runtime state | Load must not succeed for duplicates, invalid manifests, unresolved dependencies, or validation failures |
| `unload_plugin()` | A plugin identifier already known to the loader | Successful completion leaves the plugin no longer loaded in loader-managed runtime state | Unload updates loader-managed lifecycle state |
| `reload_plugin()` | A plugin identifier already known to the loader | Successful completion reapplies the loader's unload and load boundaries | Reload does not authorize behavior beyond `unload_plugin()` plus `load_plugin()` |
| `list_plugins()` | Loader-managed runtime state | Deterministic collection of registered plugins | Listing is read-only |

---

# Lifecycle Boundary

The loader shall preserve and expose a `lifecycle_state` field because
`M13` requires lifecycle-state exposure and the plugin manifest requires
that field.

This contract approves lifecycle behavior only at the operation level:

- discover
- validate
- load
- unload
- reload

This contract does not publish a broader lifecycle state vocabulary or
state-transition algorithm.

---

# Registration Boundary

Successful plugin loading shall register the plugin inside loader-managed
runtime state.

This contract does not authorize:

- a new `PlatformObject` plugin type
- a new object namespace
- direct expansion of `ObjectRegistry` or `ServiceRegistry` semantics

If the implementation uses registry-style state to track plugins, it
shall preserve duplicate handling and deterministic ordering consistent
with `REGISTER_CONTRACT`.

---

# Dependency Interaction

Plugin dependencies are loader inputs that shall be interpreted through
the published `DependencyResolver` boundary.

Successful plugin loading requires dependency checks to complete before
registration succeeds.

This contract does not authorize an alternative dependency model outside
the existing `DependencyResolver`.

---

# Error Behavior

This contract does not require new plugin-specific exception classes.

Repository-backed error expectations are:

- duplicate plugin identifiers shall fail with existing duplicate
  registration behavior where registry-style registration applies
- unresolved dependencies shall fail with `DependencyError` or an
  equivalent published dependency validation failure
- invalid manifests and missing required metadata shall fail validation
  and shall not result in successful plugin loading
- validation failures shall prevent successful registration or loading

`M13` requires the loader to reuse existing platform exceptions whenever
appropriate.

---

# Future Guidance

Future governance may publish:

- exact method signatures
- concrete return types
- additional lifecycle states
- plugin packaging or transport rules
- plugin persistence behavior

Those items are not approved by this draft contract.

---

# Related

- `Governance/ADR/ADR-0008_Plugin_Loader_Boundary.md`
- `Governance/ADR/ADR-0006_Generic_Registry_Pattern.md`
- `Governance/ADR/ADR-0007_Runtime_Validation_Framework.md`
- `Governance/WorkQueue/M13-Plugin-Loader.md`
- `Governance/Contracts/REGISTER_CONTRACT.md`
