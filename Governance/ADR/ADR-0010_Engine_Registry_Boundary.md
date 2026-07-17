# ADR-0010 — Adopt Engine Registry Boundary

## Status

Accepted

---

## Purpose

Define the minimum architectural policy required before implementing
`M15 Engine Registry`.

---

## Repository Evidence

`Governance/WorkQueue/M15-Engine-Registry.md` requires a runtime
subsystem that:

- registers engines
- unregisters engines
- looks up engines
- lists engines
- updates engines
- starts engines
- stops engines
- restarts engines
- preserves engine metadata
- preserves lifecycle state
- exposes capabilities
- integrates with dependency resolution
- integrates with validation
- supports future scheduling

`M15` requires integration with:

- `BaseRegistry`
- `PlatformObject`
- `CapabilityRegistry`
- `ServiceRegistry`
- `EventBus`
- `DependencyResolver`
- `Validation Framework`
- `PluginLoader`
- `ApplicationRegistry`

Before publication of this ADR, the repository already published the
following related governance and runtime evidence:

- `ADR-0006` governs generic runtime registries.
- `ADR-0007` governs the runtime validation framework.
- `ADR-0008` governs the Plugin Loader boundary.
- `ADR-0009` governs the Application Registry boundary.
- `REGISTER_CONTRACT` governs shared registry behavior.
- `SERVICE_CONTRACT` governs services and the service registry.
- `PLUGIN_CONTRACT` governs the Plugin Loader public boundary.
- `APPLICATION_CONTRACT` governs the Application Registry public
  boundary.
- `AXI-SCH-007 Platform Object` publishes the `AXI-ENG` namespace and
  the `Engine` object type.
- `Runtime/ObjectModel/platform_object.py` publishes the shared object
  model reused by existing runtime components.
- `Runtime/EngineRegistry/README.md` is a placeholder and no approved
  Engine Registry implementation currently exists.

Before publication of this ADR, the repository did not publish:

- an Engine Registry architectural boundary
- an approved engine lifecycle boundary
- an approved engine registration boundary
- an approved engine validation boundary

---

## Architectural Policy

Adopt a dedicated Engine Registry boundary for `M15` with the following
constraints:

- The Engine Registry is a runtime subsystem implemented in
  `Runtime/EngineRegistry/`.
- Under `ADR-0006`, the Engine Registry shall reuse `BaseRegistry` as
  its registry foundation unless a later approved ADR documents an
  exception.
- The Engine Registry shall reuse the published `PlatformObject` model
  for shared object fields where appropriate and shall not replace the
  existing object model.
- The public registration boundary is limited to engine records governed
  by the `engine_id` field required by `M15`.
- The Engine Registry reuses the existing `AXI-ENG` namespace and
  `Engine` object type already published by `AXI-SCH-007`; this ADR does
  not authorize a new namespace or object taxonomy.
- Lifecycle management is limited to the `register`, `update`,
  `unregister`, `start`, `stop`, and `restart` boundaries required by
  `M15`.
- Validation is limited to published governance artifacts and the public
  runtime validation interfaces governed by `ADR-0007`.
- Service integration is limited to the existing `ServiceRegistry`
  boundary where engine validation or dependency resolution requires it.
- Plugin integration is limited to the existing Plugin Loader boundary
  where engine validation or dependency resolution requires it.
- Application integration is limited to the existing Application
  Registry boundary where engine validation or dependency resolution
  requires it.
- This ADR does not publish new service, plugin, or application fields
  for engine records and does not publish new cross-registry APIs.
- Event integration is limited to the existing `EventBus` boundary.
  This ADR does not publish event names, payload schemas, or delivery
  policies for engines.
- Dependency handling is limited to the published `DependencyResolver`
  boundary and does not authorize a new dependency model.
- Future scheduling support required by `M15` is limited to preserving
  engine metadata compatible with later scheduling governance. This ADR
  does not publish scheduling algorithms, queues, triggers, or runtime
  orchestration policies.

---

## Future Guidance

Future governance may extend engine behavior, but this ADR does not
define:

- process orchestration or scheduling algorithms
- pipeline execution semantics assigned to `M16`
- deployment or distribution behavior
- cross-process or remote engine management
- persistence or replay semantics
- event contracts for engine lifecycle notifications
- runtime behavior beyond `M15 Engine Registry`

---

## Non-Goals

This ADR does not approve:

- a new registry inheritance pattern
- a new object model
- a new dependency model
- a new validation model
- plugin discovery, packaging, or marketplace behavior
- application orchestration behavior beyond the published
  `ApplicationRegistry` boundary
- workflow or pipeline orchestration responsibilities assigned to later
  milestones

---

## Related

- `ADR-0006`
- `ADR-0007`
- `ADR-0008`
- `ADR-0009`
- `Governance/WorkQueue/M15-Engine-Registry.md`
- `Governance/Contracts/REGISTER_CONTRACT.md`
- `Governance/Contracts/SERVICE_CONTRACT.md`
- `Governance/Contracts/PLUGIN_CONTRACT.md`
- `Governance/Contracts/APPLICATION_CONTRACT.md`
- `Governance/Schemas/AXI-SCH-007_Platform_Object.json`
