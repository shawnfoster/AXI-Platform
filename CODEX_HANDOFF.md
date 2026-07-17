# AXI Codex Handoff

Current Release

AXI-Platform-v2.1

---

Mission

Implement approved Work Queue items while preserving AXI governance.

---

Startup

Read:

1. AGENTS.md
2. .ai/START_HERE.md

Complete the startup sequence exactly.

---

Repository Authority

The repository is the authoritative source of truth.

---

Current Repository State

- Runtime is implemented through `M17 Runtime CLI`.
- Implemented runtime foundation components:
  `PlatformObject`, Registry Foundation, `M8 Capability Registry`,
  `M9 Service Registry`, `M10 Event Bus`,
  `M11 Dependency Resolver`, `M12 Validation Framework`, and
  `M13 Plugin Loader`, `M14 Application Registry`, and
  `M15 Engine Registry`, `M16 Pipeline Runtime`, and
  `M17 Runtime CLI`.
- Current runtime architecture:
  `PlatformObject` -> Registry Foundation -> `CapabilityRegistry` ->
  `ServiceRegistry`; `EventBus`, `DependencyResolver`,
  `Validation Framework`, `Plugin Loader`, and
  `Application Registry`, `Engine Registry`, and `Pipeline Runtime`
  integrate with those foundations without replacing them, and
  `Runtime CLI` exposes a local in-process command surface over those
  published runtime boundaries.
- Governance status:
  `ADR-0006`, `ADR-0007`, `ADR-0008`, `ADR-0009`, and `ADR-0010` are
  accepted, `ADR-0011` is accepted, `REGISTER_CONTRACT`,
  `SERVICE_CONTRACT`, `PLUGIN_CONTRACT`, `APPLICATION_CONTRACT`,
  `ENGINE_CONTRACT`, `PIPELINE_CONTRACT`, and `SCHEMA_REGISTRY` are
  published, `AXI-SCH-009 Plugin Manifest`, `AXI-SCH-010 Application`,
  `AXI-SCH-011 Engine`, `AXI-SCH-012 Pipeline`, and
  `AXI-SCH-013 CLI Command` are published, `ADR-0012` is accepted,
  `CLI_CONTRACT` is published,
  `M13 Plugin Loader`, `M14 Application Registry`,
  `M15 Engine Registry`, and `M16 Pipeline Runtime` are implemented and
  validated, and `M17 Runtime CLI` is now implemented and validated.
- Runtime freeze status:
  `Runtime-v1.2` is the accepted freeze tag through `M13`; current
  repository state extends beyond that freeze with `M14`, `M15`,
  `M16`, and `M17` implemented.
- Next governed phase:
  `Governance/WorkQueue/M18-Runtime-API.md` remains published as the
  next planning-only milestone and still requires milestone-specific
  governance publication before implementation.
- Runtime milestone progression:
  `M9` through `M17` are complete; `M18` is planned.

---

Implementation Rules

- One work item only.
- Preserve architecture.
- Preserve schemas.
- Preserve contracts.
- Preserve provenance.
- Run validation.
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
- Placeholder `ADR-0013_Runtime_API_Surface_Boundary.md`
- Placeholder `Governance/Contracts/API_CONTRACT.md`
- Placeholder `AXI-SCH-014_API_Operation.json`

---

Success

A successful implementation leaves:

- Clean repository
- Passing tests
- Updated documentation
- One logical commit
