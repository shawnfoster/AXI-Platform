# AXI Runtime Dependency Matrix

**Version:** 1.6.0
**Status:** Approved
**Authority:** AXI Platform Governance
**Audit Date:** 2026-07-19

---

# Purpose

This document audits the AXI runtime work queue against the repository
state present on 2026-07-19 and records the governed Phase II runtime
state after implementation of `M18`.

The audit distinguishes between:

- work items defined in governance
- runtime modules implemented in code
- placeholders that do not satisfy dependencies
- downstream milestones that remain blocked

---

# Scope

This audit covers the runtime foundation sequence referenced by the
active work queue:

- Platform Object Model
- Registry Foundation
- Capability Registry
- Service Registry
- Event Bus
- Dependency Resolver
- Validation Framework
- Plugin Loader
- Application Registry
- Engine Registry
- Pipeline Runtime
- Runtime CLI
- Runtime API

---

# Findings

1. Work queue numbering has drifted from published references. `ADR-0006`
   cites `M6 Platform Object Model` and `M7 Capability Registry`, while
   the active runtime work queue begins at `M8`.
2. The repository now implements `M9 Service Registry` in addition to
   the runtime foundations it depends on: `PlatformObject`,
   `BaseRegistry`, `ObjectRegistry`, and `CapabilityRegistry`.
3. The repository now implements `M10 Event Bus`.
4. The repository now implements `M11 Dependency Resolver`.
5. The repository now implements `M12 Validation Framework`.
6. `Runtime/PluginLoader` is now implemented with runtime code,
   documentation, and tests.
7. `Runtime/ApplicationRegistry` is now implemented with runtime code,
   documentation, and tests.
8. `Runtime/EngineRegistry` is now implemented with runtime code,
   documentation, governance, and tests.
9. `M16 Pipeline Runtime` is now implemented with published pipeline
   governance, runtime code, documentation, and tests, completing the
   current runtime foundation sequence through `M16`.
10. `Runtime/API/` now exists with runtime code, documentation, runtime
    tests, and integration tests.
11. `AXI-SCH-007 Platform Object` publishes `AXI-CLI` / `CLI` and
    `AXI-API` / `API` object taxonomy, while `ADR-0011` explicitly
    defers CLI and API execution surfaces beyond `M16`.
12. `ADR-0012 Runtime CLI Surface Boundary`,
    `CLI_CONTRACT`, and `AXI-SCH-013 CLI Command` are now published,
    satisfying the M17 governance entry gate.
13. `Runtime/CLI/` is now implemented with runtime code, documentation,
    runtime tests, and integration tests, completing `M17`.
14. `ADR-0013 Runtime API Surface Boundary`, `API_CONTRACT`, and
    `AXI-SCH-014 API Operation` are now published, satisfying the M18
    governance entry gate.
15. `M18 Runtime API` is now implemented with published API
    governance, runtime code, documentation, runtime tests, and
    integration tests, completing `M18`.
16. `M21` now publishes dashboard, design-system, visualization, and
    artifact-specification governance as architecture-only repository
    evidence, but no GUI runtime milestone or implementation is
    published in this audit.

---

# Readiness States

- `Implemented`: required runtime modules and tests exist in the
  repository.
- `Planned`: a governed work item and placeholder milestone governance
  exist, but one or more milestone-specific ADR, contract, or schema
  artifacts remain placeholders and runtime implementation has not
  begun.
- `Ready`: the work item is defined and every prerequisite dependency is
  implemented, but the work item itself is not yet implemented.
- `Blocked`: one or more prerequisite dependencies are still placeholders
  or governance-only definitions.
- `Undocumented`: repository code exists, but no active work queue item
  currently records it as a milestone.

---

# Dependency Matrix

| Node | Repository Artifact | Produces | Published Prerequisites | Required Implemented Modules | Repository Evidence | Downstream Consumers | Readiness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| M6 reference | No active work queue artifact | Platform Object Model | AXI-SCH-007 | `Runtime/ObjectModel/` | `platform_object.py` and `Tests/Runtime/test_object_model.py` exist | M9, M10, M11, M12, M13, M14, M15, M16 | Implemented |
| Registry Foundation | No active work queue artifact | Generic registry behavior and object registry | ADR-0006 | `Runtime/Registry/`, `Runtime/ObjectRegistry/` | `base_registry.py`, `registry.py`, and `Tests/Runtime/test_object_registry.py` exist | M8, M9, M10, M11, M12, M13, M14, M15, M16 | Implemented / Undocumented |
| M8 in current repository | `Governance/WorkQueue/M8-Capability-Registry.md` | Capability registry | Registry Foundation, Platform Object Model | `Runtime/CapabilityRegistry/` | `registry.py`, `capability.py`, and `Tests/Runtime/test_capability_registry.py` exist | M9, M10, M11, M12, M13, M14, M15, M16 | Implemented |
| M9 | `Governance/WorkQueue/M9-Service-Registry.md` | Service registry | Registry Foundation, Capability Registry, Platform Object Model | `Runtime/ServiceRegistry/` | `service.py`, `registry.py`, `__init__.py`, and `Tests/Runtime/test_service_registry.py` exist | M10, M11, M12, M13, M14, M15, M16 | Implemented |
| M10 | `Governance/WorkQueue/M10-Event-Bus.md` | Event bus | Registry Foundation, Capability Registry, Service Registry, Object Registry, Platform Object Model | `Runtime/EventBus/` | `event.py`, `subscriber.py`, `bus.py`, `__init__.py`, and `Tests/Runtime/test_event_bus.py` exist | M11, M12, M13, M14, M15, M16 | Implemented |
| M11 | `Governance/WorkQueue/M11-Dependency-Resolver.md` | Dependency resolver | Registry Foundation, Capability Registry, Service Registry, Event Bus, Object Model | `Runtime/DependencyResolver/` | `dependency.py`, `resolver.py`, `__init__.py`, and `Tests/Runtime/test_dependency_resolver.py` exist | M12, M13, M14, M15, M16 | Implemented |
| M12 | `Governance/WorkQueue/M12-Validation-Framework.md` | Validation framework | Registry Foundation, Capability Registry, Service Registry, Event Bus, Dependency Resolver, Object Model | `Runtime/Validation/` | `__init__.py`, `validator.py`, `rules.py`, `result.py`, `README.md`, and `Tests/Runtime/test_validation_framework.py` exist | M13, M14, M15, M16 | Implemented |
| M13 | `Governance/WorkQueue/M13-Plugin-Loader.md` | Plugin loader | Registry Foundation, Capability Registry, Service Registry, Event Bus, Dependency Resolver, Validation Framework, Object Model | `Runtime/PluginLoader/` | `__init__.py`, `loader.py`, `manifest.py`, `plugin.py`, `README.md`, and `Tests/Runtime/test_plugin_loader.py` exist | M14, M15, M16 | Implemented |
| M14 | `Governance/WorkQueue/M14-Application-Registry.md` | Application registry | Registry Foundation, Capability Registry, Service Registry, Event Bus, Dependency Resolver, Validation Framework, Plugin Loader, Platform Object Model | `Runtime/ApplicationRegistry/` | `__init__.py`, `application.py`, `lifecycle.py`, `registry.py`, `README.md`, and `Tests/Runtime/test_application_registry.py` exist | M15, M16 | Implemented |
| M15 | `Governance/WorkQueue/M15-Engine-Registry.md` | Engine registry | Registry Foundation, Capability Registry, Service Registry, Event Bus, Dependency Resolver, Validation Framework, Plugin Loader, Application Registry, Platform Object Model | `Runtime/EngineRegistry/` | `Governance/ADR/ADR-0010_Engine_Registry_Boundary.md`, `Governance/Contracts/ENGINE_CONTRACT.md`, and `Governance/Schemas/AXI-SCH-011_Engine.json` are published; `Runtime/EngineRegistry/` now contains `__init__.py`, `engine.py`, `lifecycle.py`, `registry.py`, `README.md`, and `Tests/Runtime/test_engine_registry.py` | M16 | Implemented |
| M16 | `Governance/WorkQueue/M16-Pipeline-Runtime.md` | Pipeline runtime | Registry Foundation, Capability Registry, Service Registry, Event Bus, Dependency Resolver, Validation Framework, Plugin Loader, Application Registry, Engine Registry, Platform Object Model | `Runtime/Pipeline/` | `Governance/ADR/ADR-0011_Pipeline_Runtime_Boundary.md`, `Governance/Contracts/PIPELINE_CONTRACT.md`, and `Governance/Schemas/AXI-SCH-012_Pipeline.json` are published; `Runtime/Pipeline/` now contains `__init__.py`, `pipeline.py`, `runtime.py`, `stage.py`, `execution.py`, `README.md`, and `Tests/Runtime/test_pipeline_runtime.py` | Future runtime CLI and API milestones | Implemented |
| M17 | `Governance/WorkQueue/M17-Runtime-CLI.md` | Runtime CLI surface | `M16 Pipeline Runtime`, `ADR-0011`, `AXI-SCH-007 Platform Object` | `Runtime/CLI/` | `AXI-SCH-007` publishes `AXI-CLI` / `CLI`; `M9 Service Registry` identifies the CLI as a runtime service consumer; `M16` names future runtime CLI milestones as downstream consumers; `ADR-0012`, `CLI_CONTRACT`, and `AXI-SCH-013` are published; `Runtime/CLI/` now contains `__init__.py`, `command.py`, `result.py`, `cli.py`, `__main__.py`, `README.md`; `Tests/Runtime/test_runtime_cli.py` and `Tests/Integration/test_runtime_cli_integration.py` exist | No later governed consumer published | Implemented |
| M18 | `Governance/WorkQueue/M18-Runtime-API.md` | Runtime API surface | `M16 Pipeline Runtime`, `ADR-0011`, `AXI-SCH-007 Platform Object` | `Runtime/API/` | `AXI-SCH-007` publishes `AXI-API` / `API`; `M9 Service Registry` identifies APIs as runtime service consumers; `M16` names future runtime API milestones as downstream consumers; `ADR-0013`, `API_CONTRACT`, and `AXI-SCH-014` are now published; `Runtime/API/` now contains `__init__.py`, `api.py`, `operation.py`, `result.py`, `README.md`; `Tests/Runtime/test_runtime_api.py` and `Tests/Integration/test_runtime_api_integration.py` exist | No later governed consumer published | Implemented |

---

# Governance Decisions From This Audit

1. Treat placeholder directories and empty README files as missing
   implementations.
2. Use repository implementation evidence, not milestone intent, as the
   readiness gate for runtime work.
3. Treat `M15` as implemented only while its published engine-specific
   ADR, contract, and schema remain present alongside the runtime
   implementation and tests.
4. Treat `M16` as implemented only while its published pipeline-specific
   ADR, contract, and schema remain present alongside the runtime
   implementation and tests, and the upstream runtime foundations
   through `M15` remain validated and committed.
5. Preserve the current work queue filenames until a separate governance
   change explicitly resolves numbering drift.
6. Publish Phase II only where direct downstream runtime evidence exists
   in the repository; this audit supports CLI and API, but not GUI.
7. Treat `M18` as implemented only while `ADR-0013`, `API_CONTRACT`,
   and `AXI-SCH-014` remain published alongside the `Runtime/API/`
   implementation, documentation, and tests, and the upstream runtime
   foundations through `M16` remain validated.
8. Treat `M17` as implemented only while `ADR-0012`,
   `CLI_CONTRACT`, and `AXI-SCH-013` remain published alongside the
   `Runtime/CLI/` implementation, documentation, and tests, and the
   upstream runtime foundations through `M16` remain validated.
9. Do not claim runtime implementation beyond `M18` without new
   published work queue and milestone-specific governance.
10. Treat `M21` as architecture-only repository evidence that does not
    authorize GUI runtime implementation beyond `M18`.
