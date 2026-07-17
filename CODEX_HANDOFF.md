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

- Runtime is implemented through `M12 Validation Framework`.
- Implemented runtime foundation components:
  `PlatformObject`, Registry Foundation, `M8 Capability Registry`,
  `M9 Service Registry`, `M10 Event Bus`,
  `M11 Dependency Resolver`, and `M12 Validation Framework`.
- Current runtime architecture:
  `PlatformObject` -> Registry Foundation -> `CapabilityRegistry` ->
  `ServiceRegistry`; `EventBus`, `DependencyResolver`, and
  `Validation Framework` integrate with those foundations without
  replacing them.
- Governance status:
  `ADR-0006`, `ADR-0007`, and `ADR-0008` are accepted,
  `REGISTER_CONTRACT`, `SERVICE_CONTRACT`, `PLUGIN_CONTRACT`, and
  `SCHEMA_REGISTRY` are published, `AXI-SCH-009 Plugin Manifest` is
  published, `M12 Validation Framework` is implemented and validated,
  `M13 Plugin Loader` implementation has not begun, and `M14` through
  `M16` remain blocked by published prerequisites.
- Runtime freeze status:
  `Runtime-v1.1` remains the accepted freeze tag for the runtime
  foundation baseline before `M12`.
- Next governed milestone:
  `Governance/WorkQueue/M13-Plugin-Loader.md`.
- `M13 Plugin Loader` implementation has not begun.
- A fresh M13 readiness assessment is required before implementation.

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
