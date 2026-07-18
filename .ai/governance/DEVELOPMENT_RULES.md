# AI-006 — Development Rules

**Version:** 1.2.0
**Status:** Approved

---

# Purpose

These rules govern how AI agents implement changes within the AXI repository.

They supplement the Constitution by defining implementation behavior.

---

# Rule 1 — One Work Item

Implement exactly one approved Work Queue item per development cycle.

Do not begin additional work automatically.

---

# Rule 2 — Governance First

Read, understand, and follow:

1. START_HERE
2. Constitution
3. Architecture Context
4. Commands
5. Work Queue
6. Applicable published workflow

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

---

# Rule 7 — ADR Required

Create or update an ADR before making architectural changes.

---

# Rule 8 — Stop Condition

When the assigned Work Queue item is complete:

- commit,
- tag if appropriate,
- stop.

Do not continue with the next task automatically.

---

**End of Document**
