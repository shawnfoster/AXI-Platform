# AI-002 — AI Governance Architecture

**Version:** 1.0.0
**Status:** Approved
**Authority:** AXI Platform Governance

---

# Purpose

Document the architecture of the AXI AI governance layer in `.ai/`.

This document is the primary maintenance reference for future changes to
the AI governance subsystem.

It describes relationships, authority, and maintenance rules for the AI
layer. It does not replace repository governance, platform governance,
or the published startup entrypoint.

---

# Scope

This architecture governs the repository-local AI subsystem contained in
`.ai/`.

The AI subsystem exists to:

- route AI agents into the correct repository startup sequence
- define the AI governance rules that control repository work
- publish the current authoritative AI workflow entrypoints
- provide role overlays for common AI responsibilities
- reduce prompt dependence by moving execution protocol into the
  repository

The AI subsystem does not define platform runtime architecture.

The repository remains the sole architectural authority.

---

# Repository Authority Model

Authority flows downward through the repository.

## Tier 0 — Repository Authority

Primary authority comes from repository-root and platform-governance
documents, including:

- `AGENTS.md`
- `README.md`
- repository status and handoff documents
- `Governance/`
- the assigned `Governance/WorkQueue/` item when one exists

These sources determine what work is authorized.

## Tier 1 — AI Startup Entry

The published AI startup document defines the startup sequence for AI
agents.

It is the execution entrypoint for the AI layer.

## Tier 2 — AI Core Governance

The authoritative AI governance rules are the published constitution,
development rules, coding standard, and review checklist.

These documents define immutable principles, implementation rules,
validation policy, and pre-commit review expectations.

## Tier 3 — AI Architecture And Context

Descriptive and routing references are this architecture document plus
the published AI context documents.

These documents explain relationships and provide operational context.
They do not override Tier 0 through Tier 2 authority.

## Tier 4 — Published Workflows

Published workflows route execution for specific task classes.

Current repository evidence publishes one milestone workflow for
milestone and repository-advancement work.

## Tier 5 — Published Prompts

Prompts are thin routing surfaces, not rule sources.

Current repository evidence publishes one implementation prompt.

Prompts must defer to published workflows and governing documents.

## Tier 6 — Agent Role Overlays

Agent documents define role-specific overlays, not independent
authority.

They may specialize responsibilities, but they must not conflict with
the startup sequence, core governance, or published workflows.

---

# Published Vs. Placeholder Model

Only published `.ai` documents are authoritative.

Placeholder `.ai` files may exist to reserve future workflow or prompt
surfaces. Empty files are placeholders only.

Current repository evidence shows:

- published milestone workflow
- published implement prompt
- placeholder `bugfix`, `hotfix`, `release`, and `adr` workflows
- placeholder `review`, `refactor`, `test`, and `release` prompts
- placeholder `DOMAIN_MODEL`, `GLOSSARY`, and `PLATFORM_VISION`
  context files

Placeholder files do not create authority.

---

# Startup Flow

The AI startup flow is deterministic and stage-based:

1. Read repository authority instructions.
2. Read AI core governance in the published order.
3. Read published platform context needed for the task.
4. Determine the assigned governed objective.
5. For AI-layer maintenance tasks, read this architecture reference.
6. Read the applicable published workflow.
7. Execute only the assigned governed objective.

The startup entrypoint remains the published startup document.

---

# Governed Objective Model

The AI layer uses a single-objective model.

Two governed objective types currently exist:

## Platform Objective

A repository work item backed by published platform governance, usually
through `Governance/WorkQueue/`.

## AI Governance Maintenance Objective

A bounded repository-maintenance objective that modifies `.ai/` and is
governed by the published AI subsystem documents when no dedicated AI
work queue exists.

AI governance maintenance must still:

- remain one logical objective
- preserve repository authority
- follow published AI governance
- use the published Validation Policy
- stop when the assigned objective is complete

This model prevents `.ai/` maintenance from inventing an ungoverned
parallel process while allowing the AI subsystem to maintain itself.

---

# Workflow Relationships

Workflow selection is task-class based.

- milestone and repository-advancement work uses the single published
  milestone workflow
- placeholder workflows remain non-authoritative until published

Workflows may reference core governance and context, but they must not
replace them.

No published workflow may widen repository authority beyond Tier 0
through Tier 2.

---

# Prompt Hierarchy

Prompts are the thinnest layer in the AI subsystem.

Prompt rules:

- prompts route into published workflows
- prompts do not define architecture
- prompts do not define governance
- prompts do not define contracts or schemas
- prompts must defer to repository authority

Current repository evidence publishes one routing implementation prompt.

All other prompt surfaces remain placeholders.

---

# Agent Responsibilities

Agent documents are role overlays only.

- the Engineer executes governed implementation work
- the Architect protects platform and AI-layer structure
- the Reviewer verifies compliance and validation evidence
- the Release Manager verifies governed release readiness

Agent documents should reference governing documents rather than
restate shared startup, validation, or authority rules.

---

# Validation Policy Relationships

Validation authority is centralized.

- the published development rules document defines the Validation Policy
  and validation tiers
- the published command context document provides canonical commands
  that may be used to satisfy the selected tier
- the published review checklist verifies that the selected tier and any
  stricter task-specific validation were completed
- published workflows select the applicable validation tier and must
  not hardcode a conflicting fixed sequence

This relationship keeps validation policy centralized while allowing
task-class workflows to apply it.

---

# Maintenance Rules

Future `.ai/` maintenance should prefer consolidation over expansion.

Maintenance rules:

- prefer one authoritative source for each shared rule
- reference governing documents instead of restating them
- do not publish a new workflow or prompt without a distinct task class
- treat placeholders as non-authoritative until approved content exists
- update `.ai/VERSION.md` when published AI governance changes
- preserve the deterministic startup path

---

# Freeze Baseline

Repository evidence after this audit establishes an AI governance
baseline:

- startup is repository-governed
- milestone execution is repository-governed
- validation is repository-governed
- AI maintenance has a published architecture reference
- placeholders are explicitly non-authoritative

Future `.ai/` changes should be rare and should evolve from this
baseline rather than introducing a new framework.
