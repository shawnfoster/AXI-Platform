# ADR-0022 — Establish Prompt Operations Manual Governance

## Status

Accepted

---

## Purpose

Define the architectural governance required to treat AXI prompt
operations as governed repository artifacts rather than conversational
memory, unpublished custom instructions, or ad hoc session habits.

This ADR publishes the governing architecture for:

- a Prompt Operations Manual as a first-class publication family
- governed prompt-route identifiers and category structure
- a canonical prompt index for startup, architecture, governance,
  milestone, operational-validation, executive, and emergency routes
- authority boundaries between prompt operations and repository
  governance
- synchronization rules between prompt routes, workflow surfaces,
  handoff state, and Constitutional Transition Gates

---

## Repository Evidence

The repository already publishes the following relevant evidence:

- `ADR-0017` establishes the canonical publication hierarchy,
  cross-reference rules, approval model, and manual-governance
  architecture for repository publications.
- `ADR-0021` establishes Constitutional Transition Gates as
  repository-evidence controls for major phase transitions.
- `.ai/START_HERE.md` publishes the mandatory AI startup sequence.
- `.ai/ARCHITECTURE.md` publishes the AI governance authority model and
  states that prompts are thin routing surfaces rather than rule
  sources.
- `.ai/workflows/milestone.md` publishes the only current approved AI
  workflow for governed milestone and repository-advancement work.
- `.ai/prompts/implement.md` publishes the only current prompt surface
  with approved content; other prompt and workflow placeholders remain
  non-authoritative.
- `README.md`, `Governance/Roadmap/AXI_Roadmap_v1.0.md`, and
  `CODEX_HANDOFF.md` publish repository state, active milestone,
  runtime boundary, and active transition-gate context for future
  sessions.

Before publication of this ADR, the repository does not publish:

- a governed publication family dedicated to prompt operations
- stable prompt identifiers that future sessions may reference by
  repository evidence rather than conversational recall
- a canonical prompt index that distinguishes published routes from
  placeholder prompt surfaces

---

## Architectural Policy

Adopt the following Prompt Operations Manual governance baseline.

### 1. First-Class Publication Family

Prompt Operations is a first-class AXI publication family.

Its purpose is to govern how future AXI AI-agent sessions are routed
into approved repository startup, architecture, governance, milestone,
validation, executive, and recovery surfaces.

Prompt-operations artifacts are governed publications and remain
subject to the publication-governance controls established by
`ADR-0017`.

### 2. Authority Boundary

Prompt-operations artifacts route execution into published repository
authority.

They do not replace or outrank:

- repository-root authority
- accepted ADRs
- approved schemas
- published work items
- approved AI governance
- approved workflows
- Constitutional Transition Gates

If a prompt-operations artifact conflicts with a higher-authority
repository artifact, the higher-authority artifact governs.

### 3. Location And Publication Model

Prompt-operations publications shall be published in:

`Governance/Publications/PromptOperations/`

The canonical baseline shall include:

- one Prompt Operations Manual publication
- one supporting prompt-operations index publication

The manual shall use the publication type
`Prompt Operations Manual`.

Supporting indexes may use existing governed publication types such as
`Register`.

### 4. Required Manual Content

Every Prompt Operations Manual shall preserve, at minimum:

- prompt category model
- prompt identifier model
- route-record structure
- governing-artifact references
- authorization boundaries
- placeholder-surface treatment
- transition-gate interaction rules

The manual may add further operational detail when needed, but it
shall not omit the fields above.

### 5. Identifier And Category Model

Prompt routes shall use stable repository identifiers.

The baseline identifier categories are:

- `POM-START-###`
- `POM-ARCH-###`
- `POM-GOV-###`
- `POM-M<milestone>-###`
- `POM-OVAL-###`
- `POM-EXEC-###`
- `POM-EMERG-###`

These categories govern prompt references for:

- startup
- architecture
- governance
- milestone execution
- operational validation
- executive briefing
- emergency recovery

### 6. Relationship To `.ai/`

The `.ai/` subsystem remains the repository-local execution layer for
AI startup, governance, workflows, and prompt surfaces.

Prompt-operations publications shall interpret and index those
published `.ai/` surfaces without turning placeholder files into
authority.

Prompt-operations publications may reference:

- published `.ai/` startup and governance artifacts
- published workflows
- published prompt surfaces
- published work items
- published transition gates
- repository status artifacts such as `README.md` and `CODEX_HANDOFF.md`

They shall not infer authority from empty or placeholder files.

### 7. Synchronization Rules

Prompt-operations artifacts shall be reviewed whenever any of the
following changes could affect route validity:

- startup sequence changes
- AI governance authority changes
- workflow publication changes
- active-milestone or roadmap-state changes
- work-queue publication changes
- transition-gate state changes
- repository handoff or status-surface changes

If a Constitutional Transition Gate remains closed, any prompt route
that depends on that gate shall remain marked closed or gated.

Prompt-operations artifacts shall never imply that a closed gate is
open.

### 8. Operational Boundary

Prompt-operations governance authorizes information architecture only.

It does not authorize:

- runtime execution changes
- connector implementation
- persistence
- prompt-engineering automation
- autonomous gate evaluation
- implementation beyond current repository authority

---

## Non-Goals

This ADR does not approve:

- new runtime capabilities
- automatic prompt generation
- replacement of `.ai/` startup or workflow artifacts
- replacement of repository work items with prompt documents
- transition authorization by conversation history

---

## Related

- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/ADR/ADR-0021_Constitutional_Transition_Gate_Governance.md`
- `Governance/Publications/PUBLICATION_REGISTER.md`
- `Governance/Publications/PromptOperations/AXI_Prompt_Operations_Manual.md`
- `Governance/Publications/PromptOperations/AXI_Prompt_Operations_Index.md`
- `Governance/Schemas/AXI-SCH-022_Publication.json`
- `.ai/START_HERE.md`
- `.ai/ARCHITECTURE.md`
- `.ai/workflows/milestone.md`
- `.ai/prompts/implement.md`
- `README.md`
- `CODEX_HANDOFF.md`
