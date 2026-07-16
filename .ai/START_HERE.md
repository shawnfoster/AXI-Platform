# AI-001 — START HERE

**Version:** 1.0.0  
**Status:** Approved  
**Owner:** AXI Platform

---

# Purpose

This document defines the mandatory startup procedure for every AI agent
working within the AXI repository.

The repository—not the conversation—is the authoritative source of truth.

Do not implement features before completing this startup sequence.

---

# Startup Sequence

## Phase 1 — AI Governance

Read in this exact order:

1. `.ai/governance/CONSTITUTION.md`
2. `.ai/governance/DEVELOPMENT_RULES.md`
3. `.ai/governance/CODING_STANDARD.md`
4. `.ai/governance/REVIEW_CHECKLIST.md`

---

## Phase 2 — Platform Context

Read:

1. `.ai/context/ARCHITECTURE_CONTEXT.md`
2. `.ai/context/DOMAIN_MODEL.md`
3. `.ai/context/PLATFORM_VISION.md`
4. `.ai/context/GLOSSARY.md`
5. `.ai/context/COMMANDS.md`

---

## Phase 3 — Platform Governance

Review:

- `Governance/ADR/`
- `Governance/Contracts/`
- `Governance/Schemas/`
- `Governance/Standards/`
- `Governance/Freezes/`

---

## Phase 4 — Active Work

Open **exactly one** work item from:

`Governance/WorkQueue/`

Complete only that work item.

Do not begin another task automatically.

---

# Engineering Rules

Every implementation must preserve:

- Architecture
- Contracts
- Schemas
- Standards
- Provenance
- Traceability
- Reproducibility

Never bypass governance.

Never silently change approved architecture.

Never invent new platform rules without an ADR.

---

# Definition of Done

A work item is complete only when:

- Runtime compiles successfully.
- Relevant tests pass.
- Documentation is updated.
- Schemas are updated if necessary.
- ADRs are updated if architecture changes.
- A single logical commit is produced.
- The Work Queue is updated.

Stop after completing the assigned work item.

---

# Guiding Principle

AXI is a governed decision platform.

Software implements governance.

Governance defines architecture.

Architecture enables capability.

Every change should strengthen the platform as a whole.

---

**End of Document**