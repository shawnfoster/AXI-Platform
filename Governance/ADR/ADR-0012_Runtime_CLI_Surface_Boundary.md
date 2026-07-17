# ADR-0012 — Runtime CLI Surface Boundary

## Status

Accepted

---

## Purpose

Define the minimum architectural policy required before implementing
`M17 Runtime CLI`.

---

## Repository Evidence

`Governance/WorkQueue/M17-Runtime-CLI.md` requires a local command
surface that:

- exposes deterministic inspection of registered plugins,
  applications, engines, stages, and runtime state
- exposes pipeline validation
- exposes full pipeline execution
- exposes targeted stage execution
- exposes pause, resume, and stop lifecycle operations for active
  pipeline execution
- preserves published runtime ordering, validation, and lifecycle rules
- returns deterministic command results and errors

`M17` requires integration with the published runtime boundaries from:

- `Runtime/PluginLoader`
- `Runtime/ApplicationRegistry`
- `Runtime/EngineRegistry`
- `Runtime/Pipeline`
- `Runtime/Validation`
- `Runtime/EventBus`

Before publication of this ADR, the repository already published the
following related governance and runtime evidence:

- `Governance/DependencyMatrix.md` records `M17` as the next runtime
  milestone after `M16`.
- `Governance/ADR/ADR-0011_Pipeline_Runtime_Boundary.md` explicitly
  excludes CLI execution surfaces from `M16`.
- `Governance/Contracts/PLUGIN_CONTRACT.md`,
  `APPLICATION_CONTRACT.md`, `ENGINE_CONTRACT.md`, and
  `PIPELINE_CONTRACT.md` publish the upstream runtime command targets.
- `Runtime/PluginLoader/loader.py`,
  `Runtime/ApplicationRegistry/registry.py`,
  `Runtime/EngineRegistry/registry.py`, and
  `Runtime/Pipeline/pipeline.py` already expose the runtime operations
  that `M17` must surface.
- `Governance/Schemas/AXI-SCH-007_Platform_Object.json` publishes the
  `AXI-CLI` namespace and `CLI` object type, but the repository does
  not publish a command schema for the CLI surface yet.
- `Runtime/CLI/` does not yet exist.

Before publication of this ADR, the repository did not publish:

- a Runtime CLI architectural boundary
- an approved CLI command vocabulary
- an approved CLI command schema
- an approved CLI execution-surface contract

---

## Architectural Policy

Adopt a dedicated Runtime CLI boundary for `M17` with the following
constraints:

- The Runtime CLI is a local runtime subsystem implemented in
  `Runtime/CLI/`.
- The Runtime CLI shall reuse published runtime foundations and shall
  not replace them.
- The Runtime CLI is not, by itself, a new registry hierarchy under
  `ADR-0006`.
- The Runtime CLI is an in-process command surface. This ADR does not
  authorize a daemon, remote transport, persisted session state, or
  cross-process orchestration channel.
- The CLI command boundary is limited to the published operations
  required by `M17`: inspection, pipeline validation, full pipeline
  execution, targeted stage execution, and pipeline lifecycle control
  through `pause`, `resume`, and `stop`.
- Inspection is limited to loader-managed plugins, registry-managed
  applications and engines, pipeline-managed stages, and pipeline
  runtime state already published by upstream runtime boundaries.
- The Runtime CLI may adapt command input into temporary runtime
  component instances built from published plugin, application, engine,
  and pipeline payloads. This does not authorize a new runtime domain
  model.
- Validation is limited to `AXI-SCH-013` for CLI command input plus the
  existing published runtime validation interfaces and schemas already
  approved for plugin, application, engine, and pipeline payloads.
- Command results are limited to deterministic serialization of
  published runtime objects, validation results, and execution records.
  This ADR does not authorize new business objects, new namespaces, or
  unpublished result models.
- Lifecycle control is limited to a caller-managed active
  `Runtime/Pipeline` instance in the current process. This ADR does not
  authorize cross-process pipeline control.
- Event integration is limited to the existing `EventBus` boundary where
  the caller provides one through the published runtime components.
  This ADR does not publish new CLI-specific event contracts.

---

## Future Guidance

Future governance may extend CLI behavior, but this ADR does not
define:

- remote or networked command execution
- persisted runtime sessions
- command authentication or authorization
- shell packaging or installation behavior
- API or GUI behavior assigned to later milestones
- runtime behavior beyond `M17 Runtime CLI`

---

## Non-Goals

This ADR does not approve:

- a new runtime orchestration layer
- a new dependency model
- a new validation model
- a new persistence layer
- a new event model
- any `M18 Runtime API` behavior

---

## Related

- `Governance/ADR/ADR-0011_Pipeline_Runtime_Boundary.md`
- `Governance/ADR/ADR-0010_Engine_Registry_Boundary.md`
- `Governance/ADR/ADR-0009_Application_Registry_Boundary.md`
- `Governance/ADR/ADR-0008_Plugin_Loader_Boundary.md`
- `Governance/ADR/ADR-0007_Runtime_Validation_Framework.md`
- `Governance/WorkQueue/M17-Runtime-CLI.md`
- `Governance/Contracts/CLI_CONTRACT.md`
- `Governance/Schemas/AXI-SCH-013_CLI_Command.json`
