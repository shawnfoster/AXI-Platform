# AI-010 — Governed Milestone Workflow

**Version:** 1.0.0
**Status:** Approved
**Authority:** AXI Platform Governance

---

# Purpose

Define the standard Codex governor workflow for governed milestone and
repository-advancement work inside the AXI Platform repository.

This workflow captures the governance-first implementation methodology
established by the repository through the current published milestone
sequence while preserving the repository, not the prompt, as the sole
authority.

---

# Applicability

Use this workflow when the assigned task requires one or more of the
following:

- implementing an approved work queue milestone
- auditing repository readiness before milestone work
- publishing missing milestone-specific governance
- updating repository status after governed implementation

Do not use this workflow as architectural authority.

Do not use this workflow to bypass a more specific published workflow
for another task class.

---

# Governing Principles

The repository governs the AI.

Evidence overrides assumptions.

Governance precedes implementation.

Implementation precedes validation.

Validation precedes repository updates.

Repository updates precede commit.

If repository evidence disagrees with a user prompt, handoff note, or
conversational memory, trust the repository.

---

# Repository State Rule

Do not hardcode the current platform milestone in task execution logic.

Derive the current repository state from published repository evidence,
including:

- `README.md`
- `CODEX_HANDOFF.md`
- the applicable roadmap or dependency audit for the task domain
- the assigned work queue item
- published ADRs, contracts, and schemas

If those sources differ, update your understanding from the repository
before continuing.

---

# Workflow Sequence

## Phase 0 — Mandatory Startup

Execute repository startup exactly as documented in:

- `.ai/START_HERE.md`

Read every mandatory governance document referenced by startup.

Read every required workflow document referenced by startup or required
by the assigned task.

Do not begin implementation until startup completes.

---

## Phase 1 — Repository Audit

Audit the repository evidence relevant to the assigned milestone.

Review at minimum:

- `README.md`
- `CODEX_HANDOFF.md`
- the assigned work queue item
- the applicable roadmap and dependency matrix if published
- applicable `Governance/ADR/`
- applicable `Governance/Contracts/`
- applicable `Governance/Schemas/`
- affected implementation directories
- affected tests

Determine from repository evidence:

- completed milestones
- current governed phase
- reusable foundations
- dependency order
- applicable governance state
- implementation readiness
- architectural gaps

Do not assume work exists beyond published repository evidence.

---

## Phase 2 — Readiness Decision

Implementation is authorized only when all required repository evidence
for the assigned milestone is published and complete.

At minimum verify:

- a published work queue item exists
- required ADRs are approved
- required contracts are published
- required schemas are published
- the applicable roadmap authorizes implementation
- the applicable dependency matrix marks the milestone ready or
  implemented as appropriate
- upstream milestones are complete
- acceptance criteria are published

If any required item is missing or still placeholder-only:

1. Stop implementation.
2. Publish only the missing governance justified by repository
   evidence.
3. Review and revise that governance.
4. Re-run readiness from repository evidence.

Repeat until the repository authorizes implementation or until the
missing repository evidence cannot be derived safely.

---

## Phase 3 — Implementation

Implement only the assigned milestone.

Reuse published architecture and existing runtime abstractions.

Do not:

- invent architecture
- invent governance
- widen milestone scope
- implement future milestones
- duplicate existing functionality
- bypass published runtime boundaries

Every implementation change must trace directly to repository evidence.

---

## Phase 4 — Validation

Run the validation required by repository governance and the assigned
milestone.

At minimum, when applicable:

- compile affected modules
- run milestone-specific tests
- run runtime tests
- run integration tests
- run the full repository test suite

Repair failures before continuing.

Do not update repository status while validation is failing.

---

## Phase 5 — Self Audit

Verify:

- ADR boundaries respected
- contracts satisfied
- schemas satisfied
- existing abstractions reused
- no duplicate architecture introduced
- no speculative implementation added
- no placeholder implementation shipped
- no unpublished APIs exposed
- acceptance criteria satisfied
- current architecture preserved

---

## Phase 6 — Repository Updates

Only after successful validation:

- update repository status documents affected by the milestone
- update roadmap or dependency documentation when repository state has
  changed
- update handoff or README material when public repository state has
  changed

Do not claim implementation that the repository cannot evidence.

---

## Phase 7 — Commit

Create one logical commit for the assigned governed change.

Before stopping:

- confirm the repository reflects the completed state
- confirm validation is complete
- confirm documentation is updated
- confirm the work remains within one logical objective

Then stop.

Do not begin another work item automatically.
