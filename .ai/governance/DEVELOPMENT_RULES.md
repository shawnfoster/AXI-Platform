# AI-006 — Development Rules

**Version:** 1.4.0
**Status:** Approved

---

# Purpose

These rules govern how AI agents implement changes within the AXI repository.

They supplement the Constitution by defining implementation behavior.

---

# Rule 1 — One Governed Objective

Implement exactly one governed objective per development cycle.

For platform work, the governed objective is normally an approved Work
Queue item.

For `.ai/` maintenance, the governed objective may be one explicitly
assigned AI governance maintenance objective when no dedicated AI work
queue exists.

Do not begin additional work automatically.

---

# Rule 2 — Governance First

Read, understand, and follow:

1. START_HERE
2. Constitution
3. Architecture Context
4. Commands
5. Assigned governed objective
6. Applicable published workflow
7. `.ai/ARCHITECTURE.md` when the objective modifies `.ai/`

before modifying code.

---

# Rule 3 — Preserve Architecture

Do not:

- introduce competing architectures,
- duplicate existing platform services,
- bypass approved runtime components.

---

# Rule 4 — Small Commits

Each commit should represent one logical change.

Avoid mixing refactoring, new features, and governance updates.

---

# Rule 5 — Validation Policy

Before completing work:

- select validation proportional to repository impact,
- run the highest applicable validation tier,
- run any stricter task-specific or milestone-specific validation
  required by published repository governance,
- resolve failures,
- leave the repository clean.

Validation tiers:

## Tier 1 — Documentation-Only Changes

Use for changes limited to documentation, comments, prompts, or other
non-executable repository text.

Required validation:

- `git diff --check`
- markdown validation, if available
- link or reference validation, if available

## Tier 2 — Governance And AI Workflow Changes

Use for changes to AI governance, startup instructions, workflows,
handoff instructions, prompts, or related repository-control documents.

Required validation:

- all Tier 1 validation
- startup consistency review
- AI workflow consistency review

## Tier 3 — Runtime Implementation Changes

Use for governed runtime implementation work that does not alter the
broader runtime framework boundary.

Required validation:

- compile affected runtime modules
- milestone-specific tests
- runtime tests

## Tier 4 — Architectural Or Runtime Framework Changes

Use for architecture-affecting runtime changes and other changes to the
runtime framework boundary.

Required validation:

- all Tier 3 validation
- integration tests
- full repository test suite

Validation selection rules:

- if a change spans multiple tiers, run the highest applicable tier
- if published governance requires more than the selected tier, run the
  stricter validation
- if an optional validation tool is unavailable, record that condition
  and run the remaining required validation

---

# Rule 6 — Documentation

Update documentation whenever implementation changes affect:

- architecture,
- schemas,
- contracts,
- workflows,
- public interfaces.

When repository documentation requires temporal evidence:

- prefer immutable repository evidence such as commit IDs, version
  identifiers, ADR numbers, milestone numbers, publication identifiers,
  status, and lifecycle state over conversational or relative dates
- use the execution-environment date consistently when an `Audit Date`
  or equivalent timestamp is required by published governance
- do not infer repository dates from chat conversation timing
- do not rewrite historical repository timestamps solely because the
  conversation references a different clock; note the discrepancy in
  the completion summary when it is relevant

---

# Rule 7 — ADR Required

Create or update an ADR before making architectural changes.

---

# Rule 8 — Stop Condition

When the assigned governed objective is complete:

- commit,
- tag if appropriate,
- stop.

Do not continue with the next task automatically.

---

**End of Document**
