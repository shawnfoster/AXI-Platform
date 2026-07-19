# DGM-004 — Publication Governance Topology

**Diagram ID:** `DGM-004`
**Version:** `1.0.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Annual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Source Publication:** `ADR-0017`
**Notation:** `Mermaid`
**Categories:** `Platform Architecture`, `Object Relationships`, `Dependency Graphs`
**Related ADRs:** `ADR-0017`
**Related Schemas:** `AXI-SCH-022`, `AXI-SCH-023`
**Related Capabilities:** `CAP-018`

---

# Purpose

Provide the canonical visual baseline for AXI's publication hierarchy
and the governed relationship between textual publications and diagrams.

---

# Diagram

```mermaid
flowchart TD
    CC["Constitutional Core"] --> AG["Architecture and Governance Core"]
    AG --> OG["Operational Guidance"]
    OG --> AP["Applied Practice"]

    CC --> VG["Visual Governance"]
    AG --> VG
    OG --> VG
    AP --> VG

    AG --> OM["Operating Manual"]
    AG --> FM["Field Manual"]
    AG --> STD["Standards Schemas Registers"]

    OM --> REF["Operational References and Workflows"]
    FM --> PB["Playbooks Tutorials Training"]

    VG --> DR["Diagram Register and Canonical Coverage"]
```

---

# Synchronization Requirements

- Review when the publication hierarchy changes.
- Review when approval authority or cross-reference rules change.
- Review when new publication families are approved.

---

# Revision History

| Version | Date | Summary | Authority |
| --- | --- | --- | --- |
| `1.0.0` | `2026-07-19` | Initial governed publication. | AXI Platform Governance |

---

# Review History

| Date | Reviewer | Outcome | Notes |
| --- | --- | --- | --- |
| `2026-07-19` | AXI Platform Governance | Approved | Published as the canonical diagram for publication and documentation governance. |
