# AXI Runtime Roadmap

**Version:** 1.0.0
**Status:** Approved
**Authority:** AXI Platform Governance
**Audit Date:** 2026-07-17

---

# Purpose

This roadmap converts the runtime work queue into a dependency-driven
execution order based on repository evidence.

The roadmap exists to prevent implementation from starting when a
required upstream module is only a placeholder.

---

# Current State

- `PlatformObject` is implemented.
- Registry foundation behavior is implemented through `BaseRegistry`
  and `ObjectRegistry`.
- Capability registry is implemented and tested.
- Service registry is implemented and tested.
- Event bus is implemented and tested.
- Dependency resolver is implemented and tested.
- Validation framework is implemented and tested.
- Plugin loader is implemented and tested.
- Application registry through pipeline runtime are defined in
  governance but not implemented in the runtime package.

---

# Dependency Graph

```mermaid
flowchart TD
    M6["Platform Object Model"] --> RF["Registry Foundation"]
    RF --> M8["Capability Registry"]
    M8 --> M9["Service Registry"]
    M9 --> M10["Event Bus"]
    M10 --> M11["Dependency Resolver"]
    M11 --> M12["Validation Framework"]
    M12 --> M13["Plugin Loader"]
    M13 --> M14["Application Registry"]
    M14 --> M15["Engine Registry"]
    M15 --> M16["Pipeline Runtime"]
```

This graph is intentionally conservative. Later milestones may depend on
multiple earlier milestones, but no milestone may begin before every
upstream dependency in the matrix is implemented and validated.

---

# Ordered Implementation Plan

| Order | Milestone | Current State | Entry Gate | Exit Gate |
| --- | --- | --- | --- | --- |
| 1 | Runtime dependency audit | Complete | Repository evidence collected | `Governance/DependencyMatrix.md` and this roadmap published |
| 2 | M9 Service Registry | Complete | Registry Foundation, Platform Object Model, and Capability Registry implemented | Runtime module, tests, and validation pass |
| 3 | M10 Event Bus | Complete | M9 complete | Runtime module, tests, and validation pass |
| 4 | M11 Dependency Resolver | Complete | M9 and M10 complete | Runtime module, tests, and validation pass |
| 5 | M12 Validation Framework | Complete | M9, M10, and M11 complete | Runtime module, tests, and validation pass |
| 6 | M13 Plugin Loader | Complete | M9 through M12 complete | Runtime module, tests, and validation pass |
| 7 | M14 Application Registry | Ready | M9 through M13 complete | Runtime module, tests, and validation pass |
| 8 | M15 Engine Registry | Blocked | M9 through M14 complete | Runtime module, tests, and validation pass |
| 9 | M16 Pipeline Runtime | Blocked | M9 through M15 complete | Runtime module, tests, and validation pass |

---

# Readiness Rules

1. A milestone is `Ready` only when every published prerequisite is
   backed by implemented runtime modules in this repository.
2. A placeholder directory or empty README file does not satisfy a
   runtime dependency.
3. Each milestone must compile and pass runtime tests before the next
   dependent milestone begins.
4. If numbering drift or missing prerequisite governance is discovered,
   stop implementation and update governance before resuming runtime
   development.

---

# Work Queue Maintenance Rules

Every runtime work item shall declare:

- what the milestone produces
- which published governance artifacts it depends on
- which runtime modules must already exist
- which downstream milestones consume its outputs
- what repository evidence marks the milestone as ready

Use `Governance/DependencyMatrix.md` as the authoritative readiness
check for the current runtime foundation sequence.

---

# Numbering Drift

This roadmap does not renumber existing work queue files.

Current repository evidence shows:

- `ADR-0006` references `M6 Platform Object Model`
- `ADR-0006` references `M7 Capability Registry`
- the active work queue begins at `M8`
- registry foundation is implemented but not represented by an active
  work queue item

Any renumbering or backfill of historical milestones shall occur only
through a separate governance update so file history and traceability
remain intact.
