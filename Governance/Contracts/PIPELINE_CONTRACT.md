# AXI Pipeline Runtime Contract

**Version:** 1.0.0
**Status:** Approved
**Authority:** AXI Platform Governance

---

# Purpose

Define the minimum runtime contract required for `M16 Pipeline Runtime`.

This contract documents the minimum public API boundary, stage model
boundary, execution behavior, lifecycle behavior, dependency behavior,
validation behavior, and integration limits required by the published
work item.

---

# Repository Evidence

`Governance/WorkQueue/M16-Pipeline-Runtime.md` requires the following
public APIs:

- `register_stage()`
- `unregister_stage()`
- `execute()`
- `execute_stage()`
- `validate_pipeline()`
- `list_stages()`
- `pause()`
- `resume()`
- `stop()`

`M16` also requires the runtime to:

- preserve deterministic execution order
- support dependency-aware execution
- integrate validation before execution
- publish lifecycle events
- expose runtime status
- support future distributed execution

`M16` requires rejection of:

- circular pipeline graphs
- duplicate stages
- unresolved dependencies
- invalid execution order
- invalid lifecycle transitions

Existing repository evidence relevant to this contract includes:

- `ADR-0006` requires future runtime registries to inherit from
  `BaseRegistry` unless a documented exception is approved.
- `BaseRegistry.register()` rejects duplicate keys with
  `DuplicateRegistrationError`.
- `BaseRegistry.unregister()` ignores missing keys.
- `BaseRegistry.keys()` returns keys in deterministic sorted order.
- `DependencyResolver` validates dependency references and raises
  `DependencyError` for unresolved or circular dependencies.
- `ADR-0007` limits runtime validation to published governance artifacts
  and public validation interfaces.
- `ADR-0008`, `ADR-0009`, and `ADR-0010` define the published Plugin
  Loader, Application Registry, and Engine Registry boundaries used by
  `M16`.

---

# Scope

This contract applies to:

- the public Pipeline Runtime API
- stage registration and listing behavior
- pipeline execution and lifecycle behavior
- pipeline dependency and validation behavior

This contract does not define storage layouts, event names, payload
schemas, persistence rules, or distributed execution protocols.

---

# Public API Boundary

Exact Python signatures and concrete return container types are not
published by current repository evidence.

The public API names and behavior boundaries required by current
repository evidence are:

| API | Input Boundary | Output Boundary | Required Behavior |
| --- | --- | --- | --- |
| `register_stage()` | A stage input containing the fields required by `M16` | Successful completion leaves the stage registered by `stage_id` | Registration preserves stage metadata and status and does not succeed for duplicates, invalid stage definitions, or invalid engine references |
| `unregister_stage()` | A `stage_id` input | Successful completion removes the stage from runtime-managed stage state | Registry-style unregister behavior remains idempotent for missing identifiers |
| `execute()` | Runtime-managed stage state | Successful completion executes registered stages in deterministic dependency-safe order | Validation completes before execution begins |
| `execute_stage()` | An existing `stage_id` input | Successful completion executes the requested stage within the published dependency and validation boundary | Stage execution does not bypass validation or dependency requirements |
| `validate_pipeline()` | Runtime-managed stage state | A validation outcome compatible with the published validation boundary | Circular graphs, duplicates, unresolved dependencies, invalid execution order, and invalid lifecycle transitions are rejected |
| `list_stages()` | Runtime-managed stage state | Deterministic collection of registered stages | Listing is read-only and consistent with the published execution-order boundary |
| `pause()` | Runtime lifecycle state | Successful completion transitions the runtime into the published paused state | Invalid lifecycle transitions are rejected |
| `resume()` | Runtime lifecycle state | Successful completion transitions the runtime back into the published running state | Invalid lifecycle transitions are rejected |
| `stop()` | Runtime lifecycle state | Successful completion transitions the runtime into the published cancelled state | Invalid lifecycle transitions are rejected |

---

# Stage Model Boundary

The minimum published stage model required by `M16` contains:

- `stage_id`
- `name`
- `description`
- `execution_order`
- `dependencies`
- `engine`
- `status`
- `metadata`

Repository-backed stage expectations are:

- `stage_id` is the public registration key required by `M16`.
- Registered stage identifiers are unique within a runtime instance.
- `execution_order` shall be sortable into a deterministic total order.
- If multiple stages share the same `execution_order`, the runtime may
  use `stage_id` as the deterministic tie-breaker.
- `dependencies` contains stage identifiers that shall resolve within
  the managed pipeline definition before execution succeeds.
- `engine` references an engine through the existing Engine Registry
  boundary and does not publish a new engine API.
- `status` shall remain within the published pipeline runtime state
  vocabulary defined by this contract.

This contract does not authorize unpublished stage fields.

---

# Execution Order Boundary

Pipelines execute in deterministic order while honoring stage
dependencies.

Repository-backed execution expectations are:

- dependency validation completes before execution begins
- a stage does not execute before its published stage dependencies are
  satisfied
- stage ordering remains deterministic across repeated executions of the
  same pipeline definition
- the runtime does not bypass the existing Engine Registry boundary when
  resolving stage engine references

This contract does not publish scheduling algorithms, concurrency
policies, or distributed execution behavior.

---

# Lifecycle Boundary

`M16` publishes the following runtime state vocabulary:

- `Initialized`
- `Validating`
- `Ready`
- `Running`
- `Paused`
- `Completed`
- `Failed`
- `Cancelled`

Repository-backed lifecycle expectations are:

- a new runtime begins in `Initialized`
- validation uses the `Validating` state before a successful `Ready`
  state
- execution uses validation before entering `Running`
- successful execution ends in `Completed`
- failed validation or execution ends in `Failed`
- `pause()` is valid only while `Running` and transitions to `Paused`
- `resume()` is valid only while `Paused` and transitions to `Running`
- `stop()` is valid only while `Running` or `Paused` and transitions to
  `Cancelled`

This contract does not publish a broader lifecycle algorithm beyond the
state vocabulary and operation-level rules above.

---

# Dependency Behavior

Pipeline stage dependencies shall be interpreted through the published
`DependencyResolver` boundary.

`M16` requires integration with `EngineRegistry`, `ApplicationRegistry`,
`PluginLoader`, `ServiceRegistry`, and existing runtime foundations, but
this contract does not publish additional dependency semantics for those
integrations beyond the published work item and approved upstream
boundaries.

This contract does not authorize an alternative dependency model.

---

# Validation and Schema Behavior

Pipeline inputs shall be validated through the published runtime
validation boundary governed by `ADR-0007`.

The minimum pipeline schema required by `M16` is:

- `AXI-SCH-012 Pipeline`

This schema contains the pipeline fields required by `M16`:

- `stages`
- `runtime_state`
- `metadata`

Each stage definition within that schema contains the stage fields
required by `M16`.

This contract does not authorize unpublished fields, unpublished
validation inputs, or unpublished state vocabularies.

---

# Error Behavior

This contract does not require new pipeline-specific exception classes.

Repository-backed error expectations are:

- duplicate stage identifiers shall fail with existing duplicate
  registration behavior where registry-style registration applies
- unresolved dependencies shall fail with `DependencyError` or an
  equivalent published dependency validation failure
- circular stage graphs shall fail with `DependencyError` or an
  equivalent published dependency validation failure
- invalid execution order and invalid lifecycle transitions shall fail
  validation and shall not result in successful stage registration or
  execution

`M16` requires the runtime to reuse existing platform exceptions
whenever appropriate.

---

# Future Guidance

Future governance may publish:

- exact method signatures
- concrete return types
- event contracts
- persistence behavior
- scheduling semantics
- distributed execution semantics
- CLI and API orchestration behavior

Those items are not approved by this contract.

---

# Related

- `Governance/ADR/ADR-0011_Pipeline_Runtime_Boundary.md`
- `Governance/ADR/ADR-0006_Generic_Registry_Pattern.md`
- `Governance/ADR/ADR-0007_Runtime_Validation_Framework.md`
- `Governance/ADR/ADR-0008_Plugin_Loader_Boundary.md`
- `Governance/ADR/ADR-0009_Application_Registry_Boundary.md`
- `Governance/ADR/ADR-0010_Engine_Registry_Boundary.md`
- `Governance/WorkQueue/M16-Pipeline-Runtime.md`
- `Governance/Contracts/REGISTER_CONTRACT.md`
- `Governance/Contracts/PLUGIN_CONTRACT.md`
- `Governance/Contracts/APPLICATION_CONTRACT.md`
- `Governance/Contracts/ENGINE_CONTRACT.md`
