# AI-006 — Development Rules

**Version:** 1.1.0
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

# Rule 5 — Testing

Before completing work:

- compile affected modules,
- run applicable tests,
- resolve failures,
- leave the repository clean.

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
