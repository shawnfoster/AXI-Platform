# AXI Runtime CLI Contract

**Version:** 1.0.0
**Status:** Approved
**Authority:** AXI Platform Governance

---

# Purpose

Define the minimum local command contract required for `M17 Runtime
CLI`.

This contract documents the public command vocabulary, input boundary,
output boundary, lifecycle-control boundary, validation behavior, and
error behavior required by the published work item.

---

# Repository Evidence

`Governance/WorkQueue/M17-Runtime-CLI.md` requires a Runtime CLI that:

- exposes deterministic inspection of registered plugins,
  applications, engines, stages, and runtime state
- exposes pipeline validation
- exposes full pipeline execution
- exposes targeted stage execution
- exposes pause, resume, and stop lifecycle operations for active
  pipeline execution
- preserves published runtime ordering, validation, and lifecycle rules
- returns deterministic command results and errors

Existing repository evidence relevant to this contract includes:

- `Runtime/PluginLoader/loader.py` publishes `list_plugins()`.
- `Runtime/ApplicationRegistry/registry.py` publishes
  `list_applications()`.
- `Runtime/EngineRegistry/registry.py` publishes `list_engines()`.
- `Runtime/Pipeline/pipeline.py` publishes `list_stages()`,
  `validate_pipeline()`, `execute()`, `execute_stage()`, `pause()`,
  `resume()`, `stop()`, `runtime_state`, `to_dict()`, and
  `execution_history`.
- `Runtime/Pipeline/execution.py` publishes deterministic execution
  records through `StageExecution.to_dict()`.
- `Runtime/Validation/result.py` publishes deterministic validation
  result fields used by the current runtime.
- `ADR-0012` limits the CLI to a local in-process command surface over
  published runtime boundaries.

---

# Scope

This contract applies to:

- the logical Runtime CLI command vocabulary
- command input validation behavior
- deterministic command result behavior
- lifecycle control of a caller-managed active pipeline

This contract does not define shell packaging, installation, remote
execution, or cross-process session behavior.

---

# Command Boundary

Exact Python signatures and shell-flag spellings are not published by
current repository evidence.

The approved Runtime CLI command vocabulary and behavior boundaries are:

| Command | Input Boundary | Output Boundary | Required Behavior |
| --- | --- | --- | --- |
| `inspect` | A command input containing a required `target` of `plugins`, `applications`, `engines`, `stages`, or `runtime` | A deterministic result containing a serialized snapshot for the requested target | Inspection is read-only and does not mutate runtime state |
| `validate` | A command input targeting a published pipeline definition or caller-managed pipeline instance | A deterministic result containing validation results and the current pipeline snapshot | Validation uses the published pipeline and validation boundaries and does not bypass schema or dependency checks |
| `execute` | A command input targeting a published pipeline definition or caller-managed pipeline instance | A deterministic result containing ordered stage execution records and the resulting pipeline snapshot | Execution performs validation before stage execution begins |
| `execute-stage` | A command input containing a required `stage_id` plus a published pipeline definition or caller-managed pipeline instance | A deterministic result containing ordered execution records for the requested stage closure and the resulting pipeline snapshot | Targeted execution does not bypass validation or dependency requirements |
| `pause` | A command input targeting a caller-managed active pipeline instance | A deterministic result containing the resulting runtime state and pipeline snapshot | `pause` is valid only while the published pipeline runtime is `Running` |
| `resume` | A command input targeting a caller-managed paused pipeline instance | A deterministic result containing the resulting runtime state and pipeline snapshot | `resume` is valid only while the published pipeline runtime is `Paused` |
| `stop` | A command input targeting a caller-managed running or paused pipeline instance | A deterministic result containing the resulting runtime state and pipeline snapshot | `stop` is valid only while the published pipeline runtime is `Running` or `Paused` |

---

# Input Boundary

Runtime CLI command input shall validate against:

- `AXI-SCH-013 CLI Command`

The published command payload contains:

- `command`
- optional `target`
- optional `stage_id`
- optional `runtime_context`
- optional `metadata`

If `runtime_context` is supplied, it is limited to published upstream
payloads composed from:

- plugin manifest payloads compatible with `AXI-SCH-009`
- runtime application payloads compatible with
  `Application.to_dict()` and validated against `AXI-SCH-007` plus
  `AXI-SCH-010`
- runtime engine payloads compatible with `Engine.to_dict()` and
  validated against `AXI-SCH-007` plus `AXI-SCH-011`
- pipeline payloads compatible with `AXI-SCH-012`

This contract does not publish service bootstrap payloads, cross-process
session identifiers, or transport-specific metadata.

---

# Output Boundary

Successful command execution shall return a deterministic result object
containing:

- `command`
- `status`
- `payload`

Repository-backed payload expectations are:

- plugin inspection serializes loader-managed plugin records compatible
  with `Plugin.to_dict()`
- application inspection serializes registry-managed applications
  compatible with `Application.to_dict()`
- engine inspection serializes registry-managed engines compatible with
  `Engine.to_dict()`
- stage and runtime inspection serializes pipeline state compatible with
  `PipelineStage.to_dict()` and `Pipeline.to_dict()`
- validation returns serialized `ValidationResult` fields already
  published by the runtime validation framework
- execution returns serialized `StageExecution.to_dict()` records in the
  deterministic order produced by the pipeline runtime

This contract does not authorize unpublished result fields.

---

# Lifecycle Control Boundary

`pause`, `resume`, and `stop` are limited to a caller-managed active
pipeline instance within the current process.

This contract does not publish:

- persisted CLI sessions
- background pipeline workers
- cross-process runtime control
- remote lifecycle control

---

# Error Behavior

This contract does not require new CLI-specific exception classes.

Repository-backed error expectations are:

- unsupported commands shall fail validation before runtime dispatch
- unsupported `inspect` targets shall fail validation or command
  dispatch before runtime mutation
- missing `stage_id` for `execute-stage` shall fail validation or
  command dispatch before runtime mutation
- invalid lifecycle transitions shall fail with the published pipeline
  lifecycle error behavior
- invalid pipeline definitions, unresolved dependencies, and stage
  execution failures shall surface the existing published runtime
  exceptions

`M17` requires the CLI to reuse existing platform exceptions whenever
appropriate.

---

# Future Guidance

Future governance may publish:

- exact shell syntax and packaging details
- concrete exit-code values
- persisted session behavior
- remote command transport
- richer output formatting

Those items are not approved by this contract.

---

# Related

- `Governance/ADR/ADR-0012_Runtime_CLI_Surface_Boundary.md`
- `Governance/Contracts/PLUGIN_CONTRACT.md`
- `Governance/Contracts/APPLICATION_CONTRACT.md`
- `Governance/Contracts/ENGINE_CONTRACT.md`
- `Governance/Contracts/PIPELINE_CONTRACT.md`
- `Governance/Schemas/AXI-SCH-013_CLI_Command.json`
