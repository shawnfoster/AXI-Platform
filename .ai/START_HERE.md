# AI-001 — START HERE

Version: 1.4.0
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

## Phase 5 — Assigned Objective

Read only the assigned governed objective.

For platform implementation work, this is typically a published
repository work item such as:

Governance/WorkQueue/M8-Capability-Registry.md

For `.ai/` maintenance work, this is the explicitly assigned AI
governance maintenance objective.

Complete only that objective.

Do not begin another task automatically.

---

## Phase 6 — AI Governance Maintenance

If the assigned objective modifies `.ai/`, read:

- `.ai/ARCHITECTURE.md`

This document is the primary maintenance reference for the AI
governance subsystem.

---

## Phase 7 — Workflow Selection

Read the published workflow that matches the assigned task.

For governed milestone or repository-advancement work, read:

- `.ai/workflows/milestone.md`

If a published workflow is empty or placeholder-only, treat it as not
yet published and continue using the approved governance that exists.

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

- Validation that follows the Validation Policy published in
  `.ai/governance/DEVELOPMENT_RULES.md`
- Deterministic behavior where practical

---

# Completion

When the assigned governed objective is complete:

1. Run the validation required by the Validation Policy in
   `.ai/governance/DEVELOPMENT_RULES.md` and any stricter published
   task-specific governance.
2. Produce one logical commit.
3. Summarize completed work.
4. Stop.

Never begin another work item automatically.
