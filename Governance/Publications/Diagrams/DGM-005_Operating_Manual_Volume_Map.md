# DGM-005 — Operating Manual Volume Map

**Diagram ID:** `DGM-005`
**Version:** `1.0.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Semiannual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Source Publication:** `PUB-002`
**Notation:** `Mermaid`
**Categories:** `Workflow Diagrams`, `Dependency Graphs`
**Related ADRs:** `ADR-0017`
**Related Schemas:** `AXI-SCH-022`, `AXI-SCH-023`
**Related Capabilities:** `CAP-018`

---

# Purpose

Provide the canonical visual baseline for the AXI Operating Manual
volume topology.

---

# Diagram

```mermaid
flowchart TD
    OM["AXI Operating Manual"] --> V1["I Foundations"]
    OM --> V2["II Platform Operations"]
    OM --> V3["III Decision Intelligence"]
    OM --> V4["IV Knowledge Management"]
    OM --> V5["V Repository Stewardship"]
    OM --> V6["VI Organization Intelligence"]
    OM --> V7["VII Expertise Engineering"]
    OM --> V8["VIII Governance"]
    OM --> V9["IX Administration"]
    OM --> V10["X Reference"]

    V1 --> V3
    V3 --> V4
    V4 --> V5
    V5 --> V6
    V6 --> V7
    V8 --> V2
    V8 --> V9
    V10 --> V1
    V10 --> V8
```

---

# Synchronization Requirements

- Review when volume boundaries or purposes change.
- Review when a new volume is introduced or removed.
- Review when the operating-manual relationship to governing
  publications changes materially.

---

# Revision History

| Version | Date | Summary | Authority |
| --- | --- | --- | --- |
| `1.0.0` | `2026-07-19` | Initial governed publication. | AXI Platform Governance |

---

# Review History

| Date | Reviewer | Outcome | Notes |
| --- | --- | --- | --- |
| `2026-07-19` | AXI Platform Governance | Approved | Published as the canonical diagram for the Operating Manual architecture baseline. |
