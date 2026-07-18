# ADR-0013 — Runtime API Surface Boundary

## Status

Accepted

---

## Purpose

Define the minimum architectural policy required before implementing
`M18 Runtime API`.

---

## Repository Evidence

`Governance/WorkQueue/M18-Runtime-API.md` requires a programmatic API
surface that:

- exposes deterministic inspection of registered plugins,
  applications, engines, stages, and runtime state
- exposes pipeline validation
- exposes full pipeline execution
- exposes targeted stage execution
- exposes pause, resume, and stop lifecycle operations for active
  pipeline execution
- preserves published runtime ordering, validation, and lifecycle rules
- returns deterministic machine-readable results and errors

`M18` requires integration with the published runtime boundaries from:

- `Runtime/PluginLoader`
- `Runtime/ApplicationRegistry`
- `Runtime/EngineRegistry`
- `Runtime/Pipeline`
- `Runtime/Validation`
- `Runtime/EventBus`

Before publication of this ADR, the repository already published the
following related governance and runtime evidence:

- `Governance/DependencyMatrix.md` records `M18` as the next runtime
  API milestone after `M17`.
- `Governance/ADR/ADR-0011_Pipeline_Runtime_Boundary.md` explicitly
  excludes API execution surfaces from `M16`.
- `Governance/Contracts/PLUGIN_CONTRACT.md`,
  `APPLICATION_CONTRACT.md`, `ENGINE_CONTRACT.md`, and
  `PIPELINE_CONTRACT.md` publish the upstream runtime operation
  targets.
- `Runtime/PluginLoader/loader.py`,
  `Runtime/ApplicationRegistry/registry.py`,
  `Runtime/EngineRegistry/registry.py`, and
  `Runtime/Pipeline/pipeline.py` already expose the runtime operations
  that `M18` must surface.
- `Governance/Schemas/AXI-SCH-007_Platform_Object.json` publishes the
  `AXI-API` namespace and `API` object type, but the repository does
  not publish an operation schema for the API surface yet.
- `Runtime/CLI/cli.py` already demonstrates a local, in-process adapter
  over the same published runtime boundaries, though `M18` does not
  require the API to share the CLI surface as its public contract.
- `Runtime/API/` does not yet exist.

Before publication of this ADR, the repository did not publish:

- a Runtime API architectural boundary
- an approved API operation vocabulary
- an approved API operation schema
- an approved API surface contract

---

## Architectural Policy

Adopt a dedicated Runtime API boundary for `M18` with the following
constraints:

- The Runtime API is a local runtime subsystem implemented in
  `Runtime/API/`.
- The Runtime API shall reuse published runtime foundations and shall
  not replace them.
- The Runtime API is not, by itself, a new registry hierarchy under
  `ADR-0006`.
- The Runtime API is an in-process programmatic surface. This ADR does
  not authorize a server, network transport, persisted session state,
  or cross-process orchestration channel.
- The API operation boundary is limited to the published operations
  required by `M18`: inspection, pipeline validation, full pipeline
  execution, targeted stage execution, and pipeline lifecycle control
  through `pause`, `resume`, and `stop`.
- Inspection is limited to loader-managed plugins, registry-managed
  applications and engines, pipeline-managed stages, and pipeline
  runtime state already published by upstream runtime boundaries.
- The Runtime API may adapt operation input into temporary runtime
  component instances built from published plugin, application, engine,
  and pipeline payloads. This does not authorize a new runtime domain
  model.
- The Runtime API may internally reuse the governed Runtime CLI or
  other published runtime components where that reuse remains
  in-process and does not widen the published API contract.
- Validation is limited to `AXI-SCH-014` for API operation input plus
  the existing published runtime validation interfaces and schemas
  already approved for plugin, application, engine, and pipeline
  payloads.
- API results are limited to deterministic serialization of published
  runtime objects, validation results, and execution records. This ADR
  does not authorize new business objects, new namespaces, or
  unpublished result models.
- Lifecycle control is limited to a caller-managed active
  `Runtime/Pipeline` instance in the current process. This ADR does not
  authorize cross-process pipeline control.
- Event integration is limited to the existing `EventBus` boundary
  where the caller provides one through the published runtime
  components. This ADR does not publish new API-specific event
  contracts.

---

## Future Guidance

Future governance may extend API behavior, but this ADR does not
define:

- networked or remote API execution
- persisted runtime sessions
- API authentication or authorization
- HTTP, RPC, or route design
- GUI or orchestration behavior assigned to later milestones
- runtime behavior beyond `M18 Runtime API`

---

## Non-Goals

This ADR does not approve:

- a new runtime orchestration layer
- a new dependency model
- a new validation model
- a new persistence layer
- a new event model
- any post-`M18` functionality

---

## Related

- `Governance/ADR/ADR-0011_Pipeline_Runtime_Boundary.md`
- `Governance/ADR/ADR-0012_Runtime_CLI_Surface_Boundary.md`
- `Governance/ADR/ADR-0010_Engine_Registry_Boundary.md`
- `Governance/ADR/ADR-0009_Application_Registry_Boundary.md`
- `Governance/ADR/ADR-0008_Plugin_Loader_Boundary.md`
- `Governance/ADR/ADR-0007_Runtime_Validation_Framework.md`
- `Governance/WorkQueue/M18-Runtime-API.md`
- `Governance/Contracts/API_CONTRACT.md`
- `Governance/Schemas/AXI-SCH-014_API_Operation.json`
