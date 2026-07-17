# ADR-0008 — Adopt Plugin Loader Boundary

## Status

Accepted

---

## Purpose

Define the minimum architectural policy required before implementing
`M13 Plugin Loader`.

---

## Repository Evidence

`Governance/WorkQueue/M13-Plugin-Loader.md` requires a runtime subsystem
that:

- discovers plugins
- validates plugins
- loads plugins
- unloads plugins
- reloads plugins
- preserves plugin metadata
- exposes lifecycle state
- resolves dependencies
- validates before loading

`M13` requires integration with:

- `BaseRegistry`
- `PlatformObject`
- `CapabilityRegistry`
- `ServiceRegistry`
- `EventBus`
- `DependencyResolver`
- `Validation Framework`

Before publication of this ADR, the repository published the following
related governance:

- `ADR-0006` governs generic runtime registries.
- `ADR-0007` governs the runtime validation framework.
- `REGISTER_CONTRACT` governs shared registry behavior.
- `SERVICE_CONTRACT` governs services and the service registry.
- `SCHEMA_REGISTRY` published only `AXI-SCH-007` and
  `AXI-SCH-008`.

`AXI-SCH-007 Platform Object` does not define a plugin namespace or a
plugin object type.

No approved ADR defined plugin discovery, plugin lifecycle, plugin
registration, or plugin manifest validation.

`Runtime/PluginLoader/` currently contains only a placeholder
`README.md`.

---

## Architectural Policy

Adopt a dedicated Plugin Loader boundary for `M13` with the following
constraints:

- The Plugin Loader is a runtime subsystem implemented in
  `Runtime/PluginLoader/`.
- The Plugin Loader reuses existing runtime foundations and does not
  replace them.
- The Plugin Loader is not, by itself, a new registry hierarchy under
  `ADR-0006`.
- If the implementation uses registry-style state internally, that state
  shall preserve `REGISTER_CONTRACT` behavior where applicable.
- Plugin discovery is limited to loader-manageable plugin candidates and
  their manifests.
- This ADR does not authorize remote, distributed, or cross-process
  plugin discovery.
- Plugin lifecycle is limited to discover, validate, load, unload,
  reload, and lifecycle-state exposure.
- Plugin registration is limited to the Plugin Loader's managed runtime
  state and its governed interactions with existing runtime foundations.
- This ADR does not authorize introducing a new `PlatformObject` plugin
  type, a new namespace, or unpublished registry semantics.
- Plugin validation is limited to published governance artifacts and the
  public runtime validation interfaces governed by `ADR-0007`.

---

## Future Guidance

Future governance may extend plugin behavior, but this ADR does not
define:

- plugin packaging or distribution
- plugin persistence or replay
- asynchronous loading
- cross-process or distributed execution
- application or engine orchestration responsibilities assigned to `M14`
  and `M15`
- hot-reload semantics beyond preserving the `reload` boundary required
  by `M13`

---

## Non-Goals

This ADR does not approve:

- a new runtime messaging framework
- a new dependency model
- a new validation model
- a new registry inheritance pattern
- runtime behavior beyond `M13 Plugin Loader`

---

## Related

- `ADR-0006`
- `ADR-0007`
- `Governance/WorkQueue/M13-Plugin-Loader.md`
- `Governance/Contracts/REGISTER_CONTRACT.md`
- `Governance/Contracts/SERVICE_CONTRACT.md`
- `Governance/Schemas/SCHEMA_REGISTRY.md`
