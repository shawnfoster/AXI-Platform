# WQ-010 — Runtime CLI

**Work Item:** M17
**Title:** Runtime CLI
**Status:** Approved
**Priority:** High
**Owner:** AXI Platform

---

# Objective

Implement the AXI Runtime CLI.

The Runtime CLI shall expose governed local command access to the
published runtime foundation completed through `M16 Pipeline Runtime`
without replacing any existing runtime boundary.

---

# Background

The repository implements the runtime foundation through `M16`, but the
current runtime is exercised only through Python modules and runtime
tests.

Published repository evidence identifies a CLI as the next downstream
runtime capability:

- `Governance/DependencyMatrix.md` names future runtime CLI milestones
  as downstream consumers of `M16`
- `Governance/ADR/ADR-0011_Pipeline_Runtime_Boundary.md` excludes CLI
  execution surfaces from `M16`
- `Governance/Schemas/AXI-SCH-007_Platform_Object.json` publishes the
  `AXI-CLI` namespace and `CLI` object type

---

# Existing Components

Reuse existing runtime foundations.

Examples include:

- `Runtime/PluginLoader`
- `Runtime/ApplicationRegistry`
- `Runtime/EngineRegistry`
- `Runtime/Pipeline`
- `Runtime/Validation`
- `Runtime/EventBus`

Do not duplicate runtime orchestration or validation behavior.

---

# Scope

Implement a governed CLI surface in:

```text
Runtime/CLI/
```

Update package exports, documentation, and tests where required.

---

# Functional Requirements

The Runtime CLI shall:

- expose deterministic inspection of registered plugins, applications,
  engines, stages, and runtime state
- expose pipeline validation
- expose full pipeline execution
- expose targeted stage execution
- expose pause, resume, and stop lifecycle operations for active
  pipeline execution
- preserve published runtime ordering, validation, and lifecycle rules
- return deterministic command results and errors

The exact command vocabulary and command payload boundary are published
in:

- `Governance/Contracts/CLI_CONTRACT.md`
- `Governance/Schemas/AXI-SCH-013_CLI_Command.json`

---

# Dependencies

Integrate with published runtime boundaries only:

- `M13 Plugin Loader`
- `M14 Application Registry`
- `M15 Engine Registry`
- `M16 Pipeline Runtime`

No new dependency model or registry hierarchy may be introduced.

---

# Governance Requirements

Before runtime implementation begins, publish approved content for:

- `Governance/ADR/ADR-0012_Runtime_CLI_Surface_Boundary.md`
- `Governance/Contracts/CLI_CONTRACT.md`
- `Governance/Schemas/AXI-SCH-013_CLI_Command.json`

Placeholder files do not satisfy this gate.

---

# Validation Requirements

Reject:

- unsupported runtime operations
- invalid lifecycle transitions
- invalid pipeline inputs
- execution paths that bypass published validation or pipeline
  boundaries

Use existing platform exceptions whenever appropriate.

---

# Tests

Create or update automated tests covering:

- deterministic inspection output
- pipeline validation commands
- full pipeline execution commands
- targeted stage execution commands
- pause, resume, and stop behavior
- runtime error propagation

All existing runtime tests must continue to pass.

---

# Deliverables

Expected outputs:

- Runtime CLI implementation
- Documentation updates
- Automated tests

---

# Acceptance Criteria

Implementation is complete when:

✓ The CLI exposes governed runtime inspection

✓ The CLI can validate pipelines through published runtime boundaries

✓ The CLI can execute pipelines and individual stages deterministically

✓ Runtime lifecycle controls preserve published `M16` behavior

✓ Existing runtime tests pass

✓ New CLI tests pass

✓ Existing runtime architecture remains intact

---

# Definition of Done

Before completion:

- Compile successfully
- Execute all runtime tests
- Execute any CLI-specific tests
- Preserve governance
- Preserve contracts
- Preserve schemas
- Preserve provenance
- Preserve traceability
- Preserve reproducibility

Produce one logical Git commit.

Stop after completion.

---

# Suggested Commit Message

AI-028: Implement Runtime CLI
