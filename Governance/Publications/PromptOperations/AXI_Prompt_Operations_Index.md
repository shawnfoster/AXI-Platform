# AXI Prompt Operations Index

**Publication ID:** `PUB-017`
**Publication Type:** `Register`
**Version:** `1.1.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Annual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Audit Date:** `2026-07-19`

---

# Purpose

Publish the canonical route index for approved AXI prompt operations.

This register records prompt-route identifiers, the governing artifacts
they route into, and the current route state.

It distinguishes published routes from closed, planned, and absent
routes so future sessions do not infer authority that the repository
has not published.

---

# Core Prompt Routes

| Prompt ID | Category | Title | Governing Route | Current State | Authorization Boundary |
| --- | --- | --- | --- | --- | --- |
| `POM-START-001` | Startup | Repository Startup Sequence | `AGENTS.md`, `.ai/START_HERE.md` | Published | Mandatory before repository work begins. |
| `POM-ARCH-001` | Architecture | AI Governance Architecture Maintenance | `.ai/START_HERE.md`, `.ai/ARCHITECTURE.md`, repository governance | Published | Applies only when the objective modifies `.ai/` or requires AI-layer architecture review. |
| `POM-GOV-001` | Governance | Milestone Governance Execution | `.ai/workflows/milestone.md` plus assigned governed objective | Published | Governs repository-advancement and milestone work only. |
| `POM-GOV-002` | Governance | Constitutional Transition Gate Review | `.ai/workflows/milestone.md`, `ADR-0021`, active CTG artifact, roadmap, status surfaces | Published | Evaluates repository evidence only; does not authorize implementation beyond the gate boundary. |
| `POM-GOV-003` | Governance | Executive Architecture Review | `.ai/START_HERE.md`, `.ai/workflows/milestone.md`, repository governance corpus | Published | Review-only route; no repository changes unless a genuine constitutional deficiency is found. |
| `POM-OVAL-001` | Operational Validation | Post-M22 Validation Eligibility Review | `CTG-001`, `M22`, roadmap, repository status artifacts | Closed | Validation beyond `M22` remains unauthorized until `CTG-001` is satisfied by repository evidence. |
| `POM-EXEC-001` | Executive | Executive Operational Briefing | `CODEX_HANDOFF.md`, `README.md`, roadmap, dependency matrix, active CTGs | Published | Summarizes state only; live repository evidence remains authoritative. |
| `POM-EMERG-001` | Emergency | Repository Consistency Triage | `.ai/governance/DEVELOPMENT_RULES.md`, `.ai/governance/REVIEW_CHECKLIST.md`, repository status artifacts | Published | Supports validation failure or governance-conflict handling; does not authorize destructive changes. |

---

# Milestone Route Coverage

| Milestone | Prompt ID | Title | Governing Artifact | Current State | Authorization Boundary |
| --- | --- | --- | --- | --- | --- |
| `M8` | `POM-M8-001` | Capability Registry Milestone Route | `Governance/WorkQueue/M8-Capability-Registry.md` | Historical Complete | Historical reference only unless explicitly reassigned. |
| `M9` | `POM-M9-001` | Service Registry Milestone Route | `Governance/WorkQueue/M9-Service-Registry.md` | Historical Complete | Historical reference only unless explicitly reassigned. |
| `M10` | `POM-M10-001` | Event Bus Milestone Route | `Governance/WorkQueue/M10-Event-Bus.md` | Historical Complete | Historical reference only unless explicitly reassigned. |
| `M11` | `POM-M11-001` | Dependency Resolver Milestone Route | `Governance/WorkQueue/M11-Dependency-Resolver.md` | Historical Complete | Historical reference only unless explicitly reassigned. |
| `M12` | `POM-M12-001` | Validation Framework Milestone Route | `Governance/WorkQueue/M12-Validation-Framework.md` | Historical Complete | Historical reference only unless explicitly reassigned. |
| `M13` | `POM-M13-001` | Plugin Loader Milestone Route | `Governance/WorkQueue/M13-Plugin-Loader.md` | Historical Complete | Historical reference only unless explicitly reassigned. |
| `M14` | `POM-M14-001` | Application Registry Milestone Route | `Governance/WorkQueue/M14-Application-Registry.md` | Historical Complete | Historical reference only unless explicitly reassigned. |
| `M15` | `POM-M15-001` | Engine Registry Milestone Route | `Governance/WorkQueue/M15-Engine-Registry.md` | Historical Complete | Historical reference only unless explicitly reassigned. |
| `M16` | `POM-M16-001` | Pipeline Runtime Milestone Route | `Governance/WorkQueue/M16-Pipeline-Runtime.md` | Historical Complete | Historical reference only unless explicitly reassigned. |
| `M17` | `POM-M17-001` | Runtime CLI Milestone Route | `Governance/WorkQueue/M17-Runtime-CLI.md` | Historical Complete | Historical reference only unless explicitly reassigned. |
| `M18` | `POM-M18-001` | Runtime API Milestone Route | `Governance/WorkQueue/M18-Runtime-API.md` | Historical Complete | Historical reference only unless explicitly reassigned. |
| `M21` | `POM-M21-001` | Dashboard Design System And Visualization Services Route | `Governance/WorkQueue/M21-Dashboard-Design-System-Visualization-Services.md` | Historical Complete | Historical reference only unless explicitly reassigned. |
| `M22` | `POM-M22-001` | Core Organizational Digital Twin And Knowledge Object Schemas Route | `Governance/WorkQueue/M22-Core-Organizational-Digital-Twin-and-Knowledge-Object-Schemas.md` | Published Active | Governance-only continuation; no runtime implementation is authorized. |
| `M23` | `POM-M23-001` | Knowledge Expansion And Repository Operationalization Planning Route | `Governance/WorkQueue/M23-Knowledge-Expansion-and-Repository-Operationalization-Planning.md` | Published Planned | Planning-only route; it does not supersede active `M22` authority. |
| `M24` | `POM-M24-001` | Architecture Core Constitutional Foundation Route | `Governance/WorkQueue/M24-Architecture-Core.md` | Published Planned | Governance-only publication route; it does not supersede active `M22` authority or planned `M23` sequencing. |

---

# Explicitly Absent Milestone Routes

No governed milestone prompt route currently exists for:

- `M1` through `M7`
- `M19`
- `M20`

Those gaps remain explicit and non-authoritative until repository
evidence publishes the relevant milestone artifacts.

---

# Related

- `Governance/ADR/ADR-0022_Prompt_Operations_Manual_Governance.md`
- `Governance/Publications/PromptOperations/AXI_Prompt_Operations_Manual.md`
- `Governance/Publications/PUBLICATION_REGISTER.md`
- `.ai/START_HERE.md`
- `.ai/ARCHITECTURE.md`
- `.ai/workflows/milestone.md`
- `CODEX_HANDOFF.md`
