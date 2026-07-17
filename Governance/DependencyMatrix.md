# AXI Runtime Dependency Matrix

**Version:** 1.0.0
**Status:** Approved
**Authority:** AXI Platform Governance
**Audit Date:** 2026-07-17

---

# Purpose

This document audits the AXI runtime work queue against the repository
state present on 2026-07-17.

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
9. `M16 Pipeline Runtime` is now ready because the upstream runtime
   foundations through `M15` are implemented and validated, while
   `Runtime/Pipeline/` remains a placeholder pending implementation.

---

# Readiness States

- `Implemented`: required runtime modules and tests exist in the
  repository.
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
| M16 | `Governance/WorkQueue/M16-Pipeline-Runtime.md` | Pipeline runtime | Registry Foundation, Capability Registry, Service Registry, Event Bus, Dependency Resolver, Validation Framework, Plugin Loader, Application Registry, Engine Registry, Platform Object Model | `Runtime/Pipeline/` | Directory exists with empty `README.md` only; upstream `M9` through `M15` runtime foundations are implemented and validated | Future runtime CLI and API milestones | Ready |

---

# Governance Decisions From This Audit

1. Treat placeholder directories and empty README files as missing
   implementations.
2. Use repository implementation evidence, not milestone intent, as the
   readiness gate for runtime work.
3. Treat `M15` as implemented only while its published engine-specific
   ADR, contract, and schema remain present alongside the runtime
   implementation and tests.
4. Treat `M16` as ready only while the implemented upstream runtime
   foundations through `M15` remain validated and committed.
5. Preserve the current work queue filenames until a separate governance
   change explicitly resolves numbering drift.
