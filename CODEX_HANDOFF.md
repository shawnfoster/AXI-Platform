# AXI Codex Handoff

Current Release

AXI-Platform-v2.1

---

Mission

Implement governed objectives while preserving AXI governance and the
Decision Intelligence architecture baseline.

---

Startup

Read:

1. AGENTS.md
2. .ai/START_HERE.md
3. `.ai/ARCHITECTURE.md` when the objective modifies `.ai/`
4. `.ai/workflows/milestone.md` for governed milestone or
   repository-advancement work

Complete the startup sequence exactly.

---

Repository Authority

The repository is the authoritative source of truth.

AI Governance Baseline

The AI governance subsystem is frozen at baseline `v1.0`.

Primary maintenance reference:

- `.ai/ARCHITECTURE.md`

Standard Codex Governor

For governed milestone and repository-advancement work, the repository-
controlled Codex governor is:

- `.ai/workflows/milestone.md`

Validation for that workflow is selected from the tiered Validation
Policy published in:

- `.ai/governance/DEVELOPMENT_RULES.md`

---

Current Repository State

- Runtime is implemented through `M18 Runtime API`.
- Implemented runtime foundation components:
  `PlatformObject`, Registry Foundation, `M8 Capability Registry`,
  `M9 Service Registry`, `M10 Event Bus`,
  `M11 Dependency Resolver`, `M12 Validation Framework`, and
  `M13 Plugin Loader`, `M14 Application Registry`, and
  `M15 Engine Registry`, `M16 Pipeline Runtime`,
  `M17 Runtime CLI`, and `M18 Runtime API`.
- Current runtime architecture:
  `PlatformObject` -> Registry Foundation -> `CapabilityRegistry` ->
  `ServiceRegistry`; `EventBus`, `DependencyResolver`,
  `Validation Framework`, `Plugin Loader`, and
  `Application Registry`, `Engine Registry`, and `Pipeline Runtime`
  integrate with those foundations without replacing them, and
  `Runtime CLI` exposes a local in-process command surface over those
  published runtime boundaries while `Runtime API` exposes a local
  in-process programmatic surface over the same governed runtime
  capabilities.
- Governance status:
  `ADR-0006`, `ADR-0007`, `ADR-0008`, `ADR-0009`, and `ADR-0010` are
  accepted, `ADR-0011` is accepted, `REGISTER_CONTRACT`,
  `SERVICE_CONTRACT`, `PLUGIN_CONTRACT`, `APPLICATION_CONTRACT`,
  `ENGINE_CONTRACT`, `PIPELINE_CONTRACT`, and `SCHEMA_REGISTRY` are
  published, `AXI-SCH-009 Plugin Manifest`, `AXI-SCH-010 Application`,
  `AXI-SCH-011 Engine`, `AXI-SCH-012 Pipeline`, and
  `AXI-SCH-013 CLI Command` are published, `ADR-0012` is accepted,
  `CLI_CONTRACT` is published, `ADR-0013` is accepted,
  `API_CONTRACT` is published, and `AXI-SCH-014 API Operation` is
  published,
  `M13 Plugin Loader`, `M14 Application Registry`,
  `M15 Engine Registry`, and `M16 Pipeline Runtime` are implemented and
  validated, `M17 Runtime CLI` is implemented and validated, and
  `M18 Runtime API` is implemented and validated, `ADR-0014` is
  accepted, `AXI-SCH-006 Decision` is published, `DECISION_REGISTER`
  and `CAPABILITY_REGISTER` are published, and
  `Governance/Roadmap/AXI_Roadmap_v1.0.md` sequences the post-`M18`
  Decision Intelligence architecture.
- Decision Intelligence architecture status:
  the Decision is now the primary governed object, the canonical
  decision lifecycle is published, the Organizational Digital Twin is a
  first-class architectural domain, and no decision-domain runtime
  implementation is yet claimed.
- Runtime freeze status:
  `Runtime-v1.2` is the accepted freeze tag through `M13`; current
  repository state extends beyond that freeze with `M14`, `M15`,
  `M16`, `M17`, and `M18` implemented.
- Next governed phase:
  No later runtime work item is published after
  `Governance/WorkQueue/M18-Runtime-API.md`; post-`M18` repository
  advancement is governed by
  `Governance/Roadmap/AXI_Roadmap_v1.0.md`.
- Runtime milestone progression:
  `M9` through `M18` are complete.

---

Implementation Rules

- One governed objective only.
- Preserve architecture.
- Preserve schemas.
- Preserve contracts.
- Preserve provenance.
- Follow the Validation Policy in
  `.ai/governance/DEVELOPMENT_RULES.md`.
- Produce one logical commit.
- Stop after completion.

---

Architecture Changes

Architecture changes require an ADR.

Do not modify approved architecture directly.

---

Governance Backlog

- Placeholder `ADR-0001_Manifest_Driven_Pipeline.md`
- Placeholder `ADR-0002_Service_vs_Engine.md`
- Placeholder `ADR-0003_Decision_Service.md`
- Placeholder `ADR-0004_Reconstruction_Freeze.md`
- Placeholder `ADR-0005_Platform_Refactor.md`

---

Success

A successful implementation leaves:

- Clean repository
- Required validation completed
- Updated documentation
- One logical commit
