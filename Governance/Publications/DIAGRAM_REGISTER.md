# AXI Diagram Register

**Publication ID:** `PUB-004`
**Publication Type:** `Register`
**Version:** `1.6.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Annual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Audit Date:** `2026-07-19`

---

# Purpose

Publish the governed diagram baseline for AXI.

This register records the canonical diagrams that count toward visual
completeness of major architectural domains and preserves the source
publication relationships required to keep those diagrams authoritative.

---

# Published Canonical Diagrams

| Diagram ID | Title | Source Publication | Categories | Path | Related ADRs | Related Schemas |
| --- | --- | --- | --- | --- | --- | --- |
| `DGM-001` | Decision Intelligence Baseline Map | `ADR-0014` | Decision Lifecycle, Capability Maps, Engine Layering | `Governance/Publications/Diagrams/DGM-001_Decision_Intelligence_Baseline_Map.md` | `ADR-0014`, `ADR-0017` | `AXI-SCH-006`, `AXI-SCH-007`, `AXI-SCH-008`, `AXI-SCH-023` |
| `DGM-002` | Repository Stewardship Lifecycle Map | `ADR-0015` | Repository Lifecycle, Information Lifecycle, Archive Lifecycle, Review and Quarantine Workflow | `Governance/Publications/Diagrams/DGM-002_Repository_Stewardship_Lifecycle_Map.md` | `ADR-0015`, `ADR-0017` | `AXI-SCH-015`, `AXI-SCH-016`, `AXI-SCH-017`, `AXI-SCH-018`, `AXI-SCH-023` |
| `DGM-003` | Decision Support Context Integration Map | `ADR-0016` | Organizational Operating Context, Readiness Framework, Knowledge Architecture | `Governance/Publications/Diagrams/DGM-003_Decision_Support_Context_Integration_Map.md` | `ADR-0016`, `ADR-0017` | `AXI-SCH-019`, `AXI-SCH-020`, `AXI-SCH-021`, `AXI-SCH-023` |
| `DGM-004` | Publication Governance Topology | `ADR-0017` | Platform Architecture, Object Relationships, Dependency Graphs | `Governance/Publications/Diagrams/DGM-004_Publication_Governance_Topology.md` | `ADR-0017`, `ADR-0018`, `ADR-0021`, `ADR-0022` | `AXI-SCH-022`, `AXI-SCH-023`, `AXI-SCH-027` |
| `DGM-005` | Operating Manual Volume Map | `PUB-002` | Workflow Diagrams, Dependency Graphs | `Governance/Publications/Diagrams/DGM-005_Operating_Manual_Volume_Map.md` | `ADR-0017` | `AXI-SCH-022`, `AXI-SCH-023` |
| `DGM-006` | Field Manual Integration Map | `PUB-003` | Workflow Diagrams, Object Relationships | `Governance/Publications/Diagrams/DGM-006_Field_Manual_Integration_Map.md` | `ADR-0014`, `ADR-0016`, `ADR-0017` | `AXI-SCH-006`, `AXI-SCH-021`, `AXI-SCH-022`, `AXI-SCH-023` |
| `DGM-007` | Presentation Services Topology | `ADR-0018` | Presentation Architecture, Dashboard Architecture, Design System Architecture, Visualization Standards, Dependency Graphs | `Governance/Publications/Diagrams/DGM-007_Presentation_Services_Topology.md` | `ADR-0014`, `ADR-0017`, `ADR-0018` | `AXI-SCH-007`, `AXI-SCH-022`, `AXI-SCH-023`, `AXI-SCH-024`, `AXI-SCH-025`, `AXI-SCH-026`, `AXI-SCH-027`, `AXI-SCH-028` |
| `DGM-008` | Organization Intelligence ODT Foundation Map | `PUB-011` | Organizational Digital Twin, Knowledge Architecture, Object Relationships, Dependency Graphs | `Governance/Publications/Diagrams/DGM-008_Organization_Intelligence_ODT_Foundation_Map.md` | `ADR-0014`, `ADR-0017`, `ADR-0018`, `ADR-0019` | `AXI-SCH-006`, `AXI-SCH-007`, `AXI-SCH-023`, `AXI-SCH-029`, `AXI-SCH-030` |
| `DGM-009` | Knowledge Expansion And Operationalization Topology | `ADR-0020` | Knowledge Architecture, Workflow Diagrams, Dependency Graphs, Object Relationships | `Governance/Publications/Diagrams/DGM-009_Knowledge_Expansion_and_Operationalization_Topology.md` | `ADR-0014`, `ADR-0015`, `ADR-0017`, `ADR-0018`, `ADR-0019`, `ADR-0020` | `AXI-SCH-006`, `AXI-SCH-007`, `AXI-SCH-015`, `AXI-SCH-018`, `AXI-SCH-019`, `AXI-SCH-020`, `AXI-SCH-021`, `AXI-SCH-023`, `AXI-SCH-029`, `AXI-SCH-030` |
| `DGM-010` | Architecture Core Constitutional Topology | `PUB-019` | Platform Architecture, Object Relationships, Workflow Diagrams, Dependency Graphs | `Governance/Publications/Diagrams/DGM-010_Architecture_Core_Constitutional_Topology.md` | `ADR-0014`, `ADR-0015`, `ADR-0017`, `ADR-0018`, `ADR-0019`, `ADR-0020`, `ADR-0021`, `ADR-0022`, `ADR-0023`, `ADR-0024` | `AXI-SCH-006`, `AXI-SCH-007`, `AXI-SCH-015`, `AXI-SCH-018`, `AXI-SCH-022`, `AXI-SCH-023`, `AXI-SCH-029`, `AXI-SCH-030`, `AXI-SCH-031` |

---

# Canonical Coverage Matrix

| Major Domain | Canonical Diagram | Coverage State |
| --- | --- | --- |
| Decision Intelligence Architecture Baseline | `DGM-001` | Published |
| Repository Stewardship Governance | `DGM-002` | Published |
| Decision Support Context Governance | `DGM-003` | Published |
| Publication and Documentation Governance | `DGM-004` | Published |
| Operating Manual Architecture | `DGM-005` | Published |
| Field Manual Architecture | `DGM-006` | Published |
| Presentation Services Governance | `DGM-007` | Published |
| Organization Intelligence Architecture | `DGM-008` | Published |
| Knowledge Expansion And Repository Operationalization Governance | `DGM-009` | Published |
| Architecture Core Constitutional Foundation | `DGM-010` | Published |

A new major published architectural domain shall not be considered
diagram-complete until this register records at least one approved
canonical diagram for that domain.

---

# Synchronization Rules

- If a source publication changes architectural meaning, its canonical
  diagrams shall be reviewed in the same governed change cycle.
- If a related schema changes a visualized structure, diagrams that
  depend on that structure shall be reviewed before the repository
  claims visual completeness for the domain.
- Diagram review history and revision history shall be preserved in the
  diagram artifact, not inferred from narrative alone.

---

# Related

- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/ADR/ADR-0018_Presentation_Services_Governance.md`
- `Governance/ADR/ADR-0021_Constitutional_Transition_Gate_Governance.md`
- `Governance/ADR/ADR-0022_Prompt_Operations_Manual_Governance.md`
- `Governance/ADR/ADR-0024_Architecture_Core_Constitutional_Foundation.md`
- `Governance/Publications/PUBLICATION_REGISTER.md`
- `Governance/Publications/AXI_Organization_Intelligence_Architecture.md`
- `Governance/Publications/AXI_Architecture_Core_Operating_System.md`
- `Governance/Standards/DOCUMENTATION_VISUALIZATION_STANDARD.md`
