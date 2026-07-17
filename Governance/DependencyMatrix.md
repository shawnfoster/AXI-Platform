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
4. `Runtime/DependencyResolver`, `Runtime/Validation`,
   `Runtime/PluginLoader`, `Runtime/ApplicationRegistry`,
   `Runtime/EngineRegistry`, and `Runtime/Pipeline` remain placeholders.
5. `M11 Dependency Resolver` is now the first governed runtime milestone
   that is defined but not yet implemented.
6. `M16 Pipeline Runtime` remains blocked by the absence of implemented
   and validated upstream runtime subsystems from `M11` through `M15`.

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
| M11 | `Governance/WorkQueue/M11-Dependency-Resolver.md` | Dependency resolver | Registry Foundation, Capability Registry, Service Registry, Event Bus, Object Model | `Runtime/DependencyResolver/` | Directory exists with empty `README.md` only | M12, M13, M14, M15, M16 | Ready |
| M12 | `Governance/WorkQueue/M12-Validation-Framework.md` | Validation framework | Registry Foundation, Capability Registry, Service Registry, Event Bus, Dependency Resolver, Object Model | `Runtime/Validation/` | Directory exists with empty `README.md` only | M13, M14, M15, M16 | Blocked by M11 |
| M13 | `Governance/WorkQueue/M13-Plugin-Loader.md` | Plugin loader | Registry Foundation, Capability Registry, Service Registry, Event Bus, Dependency Resolver, Validation Framework, Object Model | `Runtime/PluginLoader/` | Directory exists with empty `README.md` only | M14, M15, M16 | Blocked by M11 and M12 |
| M14 | `Governance/WorkQueue/M14-Application-Registry.md` | Application registry | Registry Foundation, Capability Registry, Service Registry, Event Bus, Dependency Resolver, Validation Framework, Plugin Loader, Platform Object Model | `Runtime/ApplicationRegistry/` | Directory exists with empty `README.md` only | M15, M16 | Blocked by M11, M12, and M13 |
| M15 | `Governance/WorkQueue/M15-Engine-Registry.md` | Engine registry | Registry Foundation, Capability Registry, Service Registry, Event Bus, Dependency Resolver, Validation Framework, Plugin Loader, Application Registry, Platform Object Model | `Runtime/EngineRegistry/` | Directory exists with empty `README.md` only | M16 | Blocked by M11, M12, M13, and M14 |
| M16 | `Governance/WorkQueue/M16-Pipeline-Runtime.md` | Pipeline runtime | Registry Foundation, Capability Registry, Service Registry, Event Bus, Dependency Resolver, Validation Framework, Plugin Loader, Application Registry, Engine Registry, Platform Object Model | `Runtime/Pipeline/` | Directory exists with empty `README.md` only | Future runtime CLI and API milestones | Blocked by M11 through M15 |

---

# Governance Decisions From This Audit

1. Treat placeholder directories and empty README files as missing
   implementations.
2. Use repository implementation evidence, not milestone intent, as the
   readiness gate for runtime work.
3. Keep `M16` unchanged until every upstream runtime dependency is
   implemented, validated, and committed.
4. Preserve the current work queue filenames until a separate governance
   change explicitly resolves numbering drift.
