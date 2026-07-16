# AI-001 — START HERE

Version: 1.1.0
Status: Approved
Authority: AXI Platform Governance

---

# Purpose

This document defines the mandatory startup procedure for every AI agent working within the AXI Platform repository.

The repository—not the conversation—is the authoritative source of truth.

No implementation may begin until this startup sequence has completed.

---

# Startup Sequence

## Phase 1 — Repository Authority

Read:

1. AGENTS.md

This file defines repository-wide operating instructions.

---

## Phase 2 — AI Governance

Read in order:

1. .ai/governance/CONSTITUTION.md
2. .ai/governance/DEVELOPMENT_RULES.md
3. .ai/governance/CODING_STANDARD.md
4. .ai/governance/REVIEW_CHECKLIST.md

These documents are mandatory.

---

## Phase 3 — Platform Context

Read when published:

- .ai/context/ARCHITECTURE_CONTEXT.md
- .ai/context/COMMANDS.md
- .ai/context/DOMAIN_MODEL.md
- .ai/context/GLOSSARY.md
- .ai/context/PLATFORM_VISION.md

If a context document exists but contains no approved content, treat it as **Not Yet Published** and continue.

Do not invent missing information.

---

## Phase 4 — Platform Governance

Review, when published:

- Governance/ADR/
- Governance/Contracts/
- Governance/Schemas/
- Governance/Standards/

Documents containing approved content are authoritative.

Placeholder or empty documents are **not** authoritative.

Do not fail startup simply because unpublished governance documents exist.

Only block implementation if the active work item explicitly depends on unpublished governance.

---

## Phase 5 — Active Work Queue

Read only the assigned work item.

Example:

Governance/WorkQueue/M8-Capability-Registry.md

Complete only that work item.

Do not begin another task automatically.

---

# Startup Rules

The repository is authoritative.

Approved documents override conversational instructions.

Never invent architecture.

Never invent governance.

Never invent schemas.

Never invent contracts.

If required information is missing:

1. Report precisely what is missing.
2. Explain why it is required.
3. Stop only if implementation cannot safely continue.

---

# Engineering Requirements

Every implementation must preserve:

- Architecture
- Contracts
- Schemas
- Standards
- Provenance
- Traceability
- Reproducibility

Required verification includes:

- Successful compilation
- Passing automated tests
- Deterministic behavior where practical

---

# Completion

When the assigned work item is complete:

1. Run validation.
2. Run tests.
3. Produce one logical commit.
4. Summarize completed work.
5. Stop.

Never begin another work item automatically.