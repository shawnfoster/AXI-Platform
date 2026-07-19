# DGM-008 — Organization Intelligence ODT Foundation Map

**Diagram ID:** `DGM-008`
**Version:** `1.1.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Annual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Source Publication:** `PUB-011`
**Notation:** `Mermaid`
**Categories:** `Organizational Digital Twin`, `Knowledge Architecture`, `Object Relationships`, `Dependency Graphs`
**Related ADRs:** `ADR-0014`, `ADR-0017`, `ADR-0018`, `ADR-0019`
**Related Schemas:** `AXI-SCH-006`, `AXI-SCH-007`, `AXI-SCH-023`, `AXI-SCH-029`, `AXI-SCH-030`, `AXI-SCH-031`, `AXI-SCH-032`, `AXI-SCH-033`, `AXI-SCH-034`, `AXI-SCH-035`, `AXI-SCH-036`, `AXI-SCH-037`, `AXI-SCH-038`
**Related Capabilities:** `CAP-002`, `CAP-003`, `CAP-010`, `CAP-018`, `CAP-019`, `CAP-021`

---

# Purpose

Provide the canonical visual baseline for how the completed first core
`ODT` schema-and-register set connects durable organization,
supporting-object, and knowledge meaning to decision use, presentation
use, and future runtime consumers without authorizing implementation
behavior.

---

# Diagram

```mermaid
flowchart TD
    subgraph OI["Organization Intelligence / Core ODT Baseline"]
        ORG["Organization"]
        PER["Person"]
        ROLE["Role"]
        KNO["Knowledge"]
        EXP["Expertise"]
        POL["Policy"]
        TIM["Timeline"]
        RES["Resource"]
        DEP["Dependency"]
    end

    EVI["Evidence"] -. provenance / justification .-> ORG
    EVI -. provenance / justification .-> KNO
    EVI -. provenance / justification .-> EXP

    ORG --> PER
    ORG --> ROLE
    ORG --> KNO
    ORG --> POL
    ORG --> TIM
    ORG --> RES
    ORG --> DEP
    KNO --> EXP
    ROLE -. stewardship / accountability .-> PER
    POL -. constraints .-> ROLE
    TIM -. sequencing .-> DEP
    RES -. allocable means .-> DEP

    OI --> DI["Decision Intelligence"]
    DI --> PS["Presentation Services"]
    PS --> FR["Future Runtime<br/>(Downstream / Not Yet Authorized)"]
    PS -. governed rendered consumption only .-> FR
```

---

# Synchronization Requirements

- Review when `PUB-011` changes the constitutional role or domain
  boundary of Organization Intelligence.
- Review when `ADR-0019` changes object-family responsibilities or
  cross-domain reference rules.
- Review when `AXI-SCH-029` through `AXI-SCH-038` change the published
  `ODT` object-family set or the meaning of those governed structures.
- Review when presentation-governance boundaries change the downstream
  relationship between governed objects and rendered artifacts.

---

# Revision History

| Version | Date | Summary | Authority |
| --- | --- | --- | --- |
| `1.0.0` | `2026-07-19` | Initial governed publication. | AXI Platform Governance |
| `1.1.0` | `2026-07-19` | Expanded coverage to the completed first core `ODT` schema baseline. | AXI Platform Governance |

---

# Review History

| Date | Reviewer | Outcome | Notes |
| --- | --- | --- | --- |
| `2026-07-19` | AXI Platform Governance | Approved | Published as the first canonical diagram for the Organization Intelligence architecture baseline. |
