# AXI Publication Register

**Publication ID:** `PUB-001`
**Publication Type:** `Register`
**Version:** `1.0.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Annual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Audit Date:** `2026-07-19`

---

# Purpose

Publish the canonical publication architecture baseline for AXI.

This register records the approved publication hierarchy, identifies the
published documentation artifacts that implement that hierarchy, and
preserves their governing relationships.

---

# Canonical Publication Hierarchy

| Publication Family | Publication Types | Role |
| --- | --- | --- |
| Constitutional Core | Constitution, Operating System | Defines the non-bypassable principles and platform operating model. |
| Architecture and Governance Core | ADR, Standard, Policy, Schema, Register | Defines architecture, normalization rules, governing controls, and canonical sets. |
| Operational Guidance | Operating Manual, Procedure (SOP), Workflow, Checklist, Guide, Reference | Explains how AXI operates without overriding constitutional or architectural authority. |
| Applied Practice | Field Manual, Playbook, Tutorial, Training Module | Converts governed methodology and expertise into practical operating patterns. |
| Visual Governance | Architecture Diagram, Flow Diagram, Decision Tree | Visualizes approved knowledge and remains synchronized with source publications. |

---

# Published Publication Baseline

| Publication ID | Title | Type | Path | Governing ADRs | Related Schemas | Related Capabilities | Review Cycle |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PUB-001` | AXI Publication Register | Register | `Governance/Publications/PUBLICATION_REGISTER.md` | `ADR-0017` | `AXI-SCH-022`, `AXI-SCH-023` | `CAP-018` | Annual and change-triggered |
| `PUB-002` | AXI Operating Manual Architecture | Operating Manual | `Governance/Publications/AXI_Operating_Manual_Architecture.md` | `ADR-0014`, `ADR-0015`, `ADR-0016`, `ADR-0017` | `AXI-SCH-006`, `AXI-SCH-015` through `AXI-SCH-023` | `CAP-003`, `CAP-010`, `CAP-018` | Semiannual and change-triggered |
| `PUB-003` | AXI Field Manual Architecture | Field Manual | `Governance/Publications/AXI_Field_Manual_Architecture.md` | `ADR-0014`, `ADR-0016`, `ADR-0017` | `AXI-SCH-006`, `AXI-SCH-021`, `AXI-SCH-022`, `AXI-SCH-023` | `CAP-001` through `CAP-010`, `CAP-017`, `CAP-018` | Semiannual and change-triggered |
| `PUB-004` | AXI Diagram Register | Register | `Governance/Publications/DIAGRAM_REGISTER.md` | `ADR-0017` | `AXI-SCH-022`, `AXI-SCH-023` | `CAP-018` | Annual and change-triggered |
| `PUB-005` | Documentation Visualization Standard | Standard | `Governance/Standards/DOCUMENTATION_VISUALIZATION_STANDARD.md` | `ADR-0017` | `AXI-SCH-022`, `AXI-SCH-023` | `CAP-018` | Annual and change-triggered |
| `PUB-006` | Documentation Quality Standard | Standard | `Governance/Standards/DOCUMENTATION_QUALITY_STANDARD.md` | `ADR-0015`, `ADR-0017` | `AXI-SCH-016`, `AXI-SCH-022`, `AXI-SCH-023` | `CAP-012`, `CAP-018` | Annual and change-triggered |

---

# Cross-Reference Rules

Every governed publication shall preserve, at minimum:

- publication identifier
- version
- status
- lifecycle state
- owner
- review cycle
- approval authority
- governing ADR references
- related schema references where applicable
- related capability references where applicable
- dependency and supersession references where applicable

Cross-reference integrity is part of the governed quality baseline and
shall be measured rather than assumed.

---

# Relationship Rules

- Publications shall not invent architecture that is absent from the
  governing ADRs and schemas they reference.
- Operating Manual and Field Manual artifacts shall cite the
  architectural and schema surfaces they operationalize.
- Diagrams shall be treated as governed publications with their own
  identifiers, version history, review history, and source publication
  references.
- Future publication families may be added only through approved
  architectural governance.

---

# Related

- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/Publications/DIAGRAM_REGISTER.md`
- `Governance/Publications/AXI_Operating_Manual_Architecture.md`
- `Governance/Publications/AXI_Field_Manual_Architecture.md`
- `Governance/Standards/DOCUMENTATION_VISUALIZATION_STANDARD.md`
- `Governance/Standards/DOCUMENTATION_QUALITY_STANDARD.md`
