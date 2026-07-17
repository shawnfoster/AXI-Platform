# ADR-0011 — Adopt Pipeline Runtime Boundary

## Status

Accepted

---

## Purpose

Define the minimum architectural policy required before implementing
`M16 Pipeline Runtime`.

---

## Repository Evidence

`Governance/WorkQueue/M16-Pipeline-Runtime.md` requires a runtime
subsystem that:

- registers stages
- unregisters stages
- executes pipelines
- executes individual stages
- validates pipeline definitions
- lists stages
- pauses execution
- resumes execution
- stops execution
- preserves deterministic execution order
- supports dependency-aware execution
- integrates validation before execution
- publishes lifecycle events
- exposes runtime status
- preserves compatibility with future distributed execution

`M16` requires integration with:

- `BaseRegistry`
- `PlatformObject`
- `CapabilityRegistry`
- `ServiceRegistry`
- `EventBus`
- `DependencyResolver`
- `Validation Framework`
- `PluginLoader`
- `ApplicationRegistry`
- `EngineRegistry`

Before publication of this ADR, the repository already published the
following related governance and runtime evidence:

- `ADR-0006` governs generic runtime registries.
- `ADR-0007` governs the runtime validation framework.
- `ADR-0008` governs the Plugin Loader boundary.
- `ADR-0009` governs the Application Registry boundary.
- `ADR-0010` governs the Engine Registry boundary.
- `REGISTER_CONTRACT` governs shared registry behavior.
- `PLUGIN_CONTRACT` governs the Plugin Loader public boundary.
- `APPLICATION_CONTRACT` governs the Application Registry public
  boundary.
- `ENGINE_CONTRACT` governs the Engine Registry public boundary.
- `SCHEMA_REGISTRY` publishes `AXI-SCH-007` through `AXI-SCH-011`.
- `Runtime/Pipeline/README.md` is a placeholder and no approved
  Pipeline Runtime implementation currently exists.

Before publication of this ADR, the repository did not publish:

- a Pipeline Runtime architectural boundary
- an approved stage registration boundary
- an approved pipeline lifecycle boundary
- an approved pipeline execution boundary
- an approved pipeline validation boundary

---

## Architectural Policy

Adopt a dedicated Pipeline Runtime boundary for `M16` with the following
constraints:

- The Pipeline Runtime is a runtime subsystem implemented in
  `Runtime/Pipeline/`.
- The Pipeline Runtime shall reuse published runtime foundations and
  shall not replace them.
- The Pipeline Runtime is not, by itself, a new registry hierarchy under
  `ADR-0006`.
- If the implementation uses registry-style state to track stages or
  execution records, that state shall preserve shared duplicate-handling
  and deterministic-ordering behavior compatible with
  `REGISTER_CONTRACT` where applicable.
- The public stage registration boundary is limited to stage records
  governed by the `stage_id` field required by `M16`.
- The Pipeline Runtime may coordinate registered engines, services,
  applications, and plugins only through their existing published
  boundaries. This ADR does not authorize new cross-registry APIs.
- The Pipeline Runtime shall not introduce a new `PlatformObject` type,
  a new namespace, or a new object taxonomy for pipeline stages or
  runtime state.
- Validation is limited to published governance artifacts and the public
  runtime validation interfaces governed by `ADR-0007`.
- Event integration is limited to the existing `EventBus` boundary.
  This ADR does not publish event names, payload schemas, or delivery
  policies for pipeline lifecycle events.
- Dependency handling is limited to the published `DependencyResolver`
  boundary. The Pipeline Runtime may adapt that boundary to managed
  stage identifiers and engine references, but it does not authorize a
  new dependency model.
- Lifecycle management is limited to the public operations and runtime
  states required by `M16`.
- Future distributed execution support is limited to preserving stage
  metadata and runtime state in a way that later governance can extend.
  This ADR does not publish distributed execution protocols, queues,
  workers, persistence, or replay behavior.

---

## Future Guidance

Future governance may extend pipeline behavior, but this ADR does not
define:

- distributed or cross-process execution
- persistence or replay semantics
- scheduling policies
- pipeline manifests or packaging
- CLI or API execution surfaces
- event contracts for pipeline lifecycle notifications
- runtime behavior beyond `M16 Pipeline Runtime`

---

## Non-Goals

This ADR does not approve:

- a new registry inheritance pattern
- a new object model
- a new dependency model
- a new validation model
- new service, plugin, application, or engine schemas
- orchestration behavior assigned to future milestones

---

## Related

- `ADR-0006`
- `ADR-0007`
- `ADR-0008`
- `ADR-0009`
- `ADR-0010`
- `Governance/WorkQueue/M16-Pipeline-Runtime.md`
- `Governance/Contracts/REGISTER_CONTRACT.md`
- `Governance/Contracts/PLUGIN_CONTRACT.md`
- `Governance/Contracts/APPLICATION_CONTRACT.md`
- `Governance/Contracts/ENGINE_CONTRACT.md`
- `Governance/Schemas/SCHEMA_REGISTRY.md`
