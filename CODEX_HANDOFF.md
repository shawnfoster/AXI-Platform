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
  Decision Intelligence architecture, `ADR-0015` and `ADR-0016` are
  accepted, `ADR-0017` is accepted, `AXI-SCH-015` through
  `AXI-SCH-023` are published, and publication and diagram governance
  artifacts are published through `PUBLICATION_REGISTER`,
  `DIAGRAM_REGISTER`, the Operating Manual architecture, the Field
  Manual architecture, and the documentation standards, `M21` is
  approved, `ADR-0018` is accepted, `AXI-SCH-024` through
  `AXI-SCH-028` are published, and presentation-services governance is
  published through `PUB-007` through `PUB-010` and `DGM-007`,
  `ADR-0019` is accepted, `M22` is approved as the governance-only
  milestone for Organization Intelligence and the core `ODT` schema
  baseline, `PUB-011` now publishes the Organization Intelligence
  architecture baseline, `AXI-SCH-029` and `AXI-SCH-030` are
  published, `PUB-012`, `PUB-013`, and `PUB-014` are published, and
  `DGM-008` now publishes the first canonical Organization
  Intelligence / `ODT` foundation diagram.
- Decision Intelligence architecture status:
  the Decision is now the primary governed object, the canonical
  decision lifecycle is published, the Organizational Digital Twin is a
  first-class architectural domain, repository stewardship governance
  is published, imported-content review and quarantine governance is
  published, operating context, regulatory knowledge, and readiness
  governance are published, publication hierarchy and diagram
  governance are published, dashboards, widgets, design-system assets,
  artifact specifications, and visualizations are now governed as
  first-class presentation services, Organization Intelligence
  architecture is now published through `PUB-011`, Organization and
  Knowledge governance artifacts are now published through
  `AXI-SCH-029`, `AXI-SCH-030`, `PUB-012`, and `PUB-013`, the
  Organization Profile and Decision Context foundation is now
  published through `PUB-014`, governed canonical diagrams now exist
  for every current major architectural domain, and no
  decision-domain runtime implementation is yet claimed.
- Runtime freeze status:
  `Runtime-v1.2` is the accepted freeze tag through `M13`; current
  repository state extends beyond that freeze with `M14`, `M15`,
  `M16`, `M17`, and `M18` implemented.
- Next governed phase:
  `M22` remains the active governance-only milestone. Its
  architecture plus first Organization and Knowledge schema, register,
  diagram, and profile-model outputs are now published, while the
  remaining core Organizational Digital Twin schemas and registers
  remain pending. No runtime implementation is yet authorized beyond
  `M18`.
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
