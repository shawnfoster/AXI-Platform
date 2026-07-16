# AGENTS.md

Repository: AXI Platform

---

# Repository Authority

This repository is the authoritative source of truth.

Repository artifacts supersede conversational memory whenever they conflict.

Always prefer approved repository documentation.

---

# Required Startup

Before writing code, execute the startup sequence defined in:

.ai/START_HERE.md

Do not skip startup.

---

# Governance

All implementation shall comply with:

- AI Constitution
- Development Rules
- Coding Standard
- Review Checklist

These documents are binding.

---

# Published vs. Placeholder Documents

The repository may intentionally contain placeholder governance publications.

Definitions:

## Published

A document containing approved governance content.

Published documents are authoritative.

## Placeholder

A file that exists but contains no approved content.

Examples include:

- empty files
- template headers
- TODO placeholders
- draft stubs

Placeholder documents are **not** authoritative.

Do not infer missing governance from placeholders.

---

# Missing Governance Policy

If startup encounters unpublished governance:

Continue startup.

Record the missing publication mentally for context.

Do not invent:

- architecture
- contracts
- schemas
- standards
- policy

Only block implementation when the active work item explicitly depends upon unpublished governance.

Otherwise continue using the approved governance that exists.

---

# Architecture Rules

Reuse existing architecture.

Reuse existing runtime components.

Avoid duplication.

Architectural changes require an ADR.

---

# Implementation Rules

Implement only the assigned work item.

Do not perform unrelated cleanup.

Do not refactor unrelated systems.

Do not introduce speculative improvements.

---

# Validation

Before completion:

- compile successfully
- run required tests
- validate behavior
- preserve determinism where practical

---

# Git

Produce:

- one logical commit
- clear commit message

Do not create multiple commits for one work item.

---

# Completion

When the assigned work item is complete:

- summarize completed work
- summarize validation
- stop

Do not begin another task unless explicitly instructed.