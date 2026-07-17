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

- Runtime is implemented through `M15 Engine Registry`.
- Implemented runtime foundation components:
  `PlatformObject`, Registry Foundation, `M8 Capability Registry`,
  `M9 Service Registry`, `M10 Event Bus`,
  `M11 Dependency Resolver`, `M12 Validation Framework`, and
  `M13 Plugin Loader`, `M14 Application Registry`, and
  `M15 Engine Registry`.
- Current runtime architecture:
  `PlatformObject` -> Registry Foundation -> `CapabilityRegistry` ->
  `ServiceRegistry`; `EventBus`, `DependencyResolver`,
  `Validation Framework`, `Plugin Loader`, and
  `Application Registry`, and `Engine Registry` integrate with those
  foundations without replacing them.
- Governance status:
  `ADR-0006`, `ADR-0007`, `ADR-0008`, `ADR-0009`, and `ADR-0010` are
  accepted, `REGISTER_CONTRACT`, `SERVICE_CONTRACT`, `PLUGIN_CONTRACT`,
  `APPLICATION_CONTRACT`, `ENGINE_CONTRACT`, and `SCHEMA_REGISTRY` are
  published, `AXI-SCH-009 Plugin Manifest`, `AXI-SCH-010 Application`,
  and `AXI-SCH-011 Engine` are published, `M13 Plugin Loader`,
  `M14 Application Registry`, and `M15 Engine Registry` are implemented
  and validated, and `M16` is now ready.
- Runtime freeze status:
  `Runtime-v1.2` is the accepted freeze tag through `M13`; current
  repository state extends beyond that freeze with `M14` and `M15`
  implemented.
- Next governed milestone:
  `Governance/WorkQueue/M16-Pipeline-Runtime.md`.
- Runtime milestone progression:
  `M9` through `M15` are complete and `M16` is ready.

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

---

Success

A successful implementation leaves:

- Clean repository
- Passing tests
- Updated documentation
- One logical commit
