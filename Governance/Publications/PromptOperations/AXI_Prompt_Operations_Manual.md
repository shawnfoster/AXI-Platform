# AXI Prompt Operations Manual

**Publication ID:** `PUB-016`
**Publication Type:** `Prompt Operations Manual`
**Version:** `1.1.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Semiannual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Audit Date:** `2026-07-19`

---

# Purpose

Publish the constitutional baseline for how AXI governs prompt
operations across future AI-agent sessions.

This manual is the canonical prompt-routing and prompt-library
interpretation layer for repository startup, architecture review,
governance work, milestone execution, operational-validation gating,
executive briefing, and emergency recovery.

It complements repository governance.

It never supersedes repository evidence.

---

# Repository Evidence

The repository already publishes the following relevant evidence:

- `ADR-0017` governs publication hierarchy, traceability, and manual
  relationships.
- `ADR-0021` governs Constitutional Transition Gates and closed-by-
  default phase transitions.
- `ADR-0022` governs the Prompt Operations publication family and
  prompt-route identifier model.
- `.ai/START_HERE.md` publishes the mandatory AI startup sequence.
- `.ai/ARCHITECTURE.md` publishes the AI governance authority model and
  prompt hierarchy.
- `.ai/workflows/milestone.md` publishes the repository-governed
  workflow for milestone and repository-advancement work.
- `.ai/prompts/implement.md` is the only current prompt surface with
  approved content; other prompt and workflow placeholders remain
  non-authoritative.
- `README.md`, `Governance/Roadmap/AXI_Roadmap_v1.0.md`,
  `Governance/DependencyMatrix.md`, and `CODEX_HANDOFF.md` publish the
  status evidence that prompt routes must reflect.

Before publication of this manual, the repository did not publish a
governed prompt category model or canonical prompt index for future
sessions.

---

# Constitutional Role

The Prompt Operations Manual exists to make AI-session execution
reviewable, stable, and repository-driven.

It routes future sessions into the correct published authority instead
of relying on conversational recall.

It does not authorize runtime behavior, reasoning algorithms,
implementation workflows, or transition outcomes beyond the
authorization boundaries of the artifacts it references.

---

# Prompt Category Model

| Category | Identifier Prefix | Constitutional Role | Current Baseline Source |
| --- | --- | --- | --- |
| Startup | `POM-START-###` | Route every session into the mandatory repository startup sequence. | `AGENTS.md`, `.ai/START_HERE.md` |
| Architecture | `POM-ARCH-###` | Route architecture maintenance and architecture-review work into the correct repository authority model. | `.ai/ARCHITECTURE.md`, repository governance |
| Governance | `POM-GOV-###` | Route governance execution, publication review, and transition-gate review into approved workflow and evidence surfaces. | `.ai/workflows/milestone.md`, ADRs, registers, CTGs |
| Milestones | `POM-M<milestone>-###` | Route milestone-specific work into the published work item that authorizes it. | `Governance/WorkQueue/` |
| Operational Validation | `POM-OVAL-###` | Route validation posture reviews only when repository evidence authorizes them. | CTGs, roadmap, status artifacts |
| Executive | `POM-EXEC-###` | Route executive briefings and repository-state summaries into governed status surfaces. | `CODEX_HANDOFF.md`, `README.md`, roadmap, dependency matrix |
| Emergency | `POM-EMERG-###` | Route recovery, inconsistency triage, and validation failure response into approved safeguards. | `.ai/governance/DEVELOPMENT_RULES.md`, `.ai/governance/REVIEW_CHECKLIST.md` |

---

# Route Record Requirements

Every governed prompt-route record shall preserve, at minimum:

- prompt identifier
- category
- route title
- objective
- governing artifacts
- current route state
- authorization boundary
- validation expectation when applicable

Prompt routes may reference a dedicated prompt surface, a published
workflow, or a composite repository route.

If the route is composite, the governing artifacts shall be explicit.

---

# Current Baseline Rules

- Prompt routes shall defer to repository evidence rather than
  conversation history.
- Placeholder prompt or workflow files remain non-authoritative and
  shall not receive governed route identifiers until approved content
  exists.
- Milestone-route coverage exists only for published work items:
  `M8` through `M18`, `M21`, `M22`, `M23`, and `M24`.
- No governed milestone prompt route currently exists for `M1` through
  `M7`, `M19`, or `M20`; those gaps remain explicit rather than
  inferred.
- Operational-validation routes that depend on Post-`M22` transition
  authority remain gated while `CTG-001` is closed.
- Executive routes may summarize repository state, but they shall not
  override live repository evidence.

---

# Relationship Rules

- Startup routes are mandatory before any other route is executed.
- Governance and milestone routes shall use the published milestone
  workflow unless later repository evidence publishes a narrower
  approved alternative.
- Milestone prompt routes shall remain subordinate to their governing
  work item, roadmap state, and dependency evidence.
- Executive routes shall remain synchronized with the active milestone,
  active transition gates, and runtime boundary.
- Emergency routes may stop work, escalate inconsistencies, or direct
  validation review, but they shall not authorize undocumented repair
  actions.

---

# Index Relationship

`PUB-017` is the canonical prompt index for this manual.

It records the currently approved prompt-route identifiers, the
governing artifacts they route into, and the current route state.

The index does not replace the manual.

The manual defines the interpretation rules the index operationalizes.

---

# Related

- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/ADR/ADR-0021_Constitutional_Transition_Gate_Governance.md`
- `Governance/ADR/ADR-0022_Prompt_Operations_Manual_Governance.md`
- `Governance/Publications/PromptOperations/AXI_Prompt_Operations_Index.md`
- `Governance/Publications/PUBLICATION_REGISTER.md`
- `Governance/Schemas/AXI-SCH-022_Publication.json`
- `.ai/START_HERE.md`
- `.ai/ARCHITECTURE.md`
- `.ai/workflows/milestone.md`
- `.ai/prompts/implement.md`
- `README.md`
- `CODEX_HANDOFF.md`
