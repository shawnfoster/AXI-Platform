# AXI Organization Register

**Publication ID:** `PUB-012`
**Publication Type:** `Register`
**Version:** `1.0.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Semiannual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Audit Date:** `2026-07-19`
**Related Diagram:** `DGM-008`

---

# Purpose

Publish the canonical registration baseline for governed `Organization`
objects in AXI.

No organization instances are published in this register yet.

This artifact defines the minimum metadata, lifecycle expectations,
validation rules, and traceability requirements that future governed
organization objects shall satisfy before they may be treated as
canonical Organization Intelligence evidence.

---

# Registration Boundary

The Organization Register governs the constitutional representation of
an organization as a durable governed system of:

- identity
- mission alignment
- ownership boundary
- governance
- relationships
- traceability

It does not register:

- operating context windows
- readiness assessments
- regulatory conclusions
- dashboards, widgets, or visualizations

Those remain separate governed domains.

---

# Register Entry Structure

Every governed organization record shall preserve at minimum the
structure published by:

- `Governance/Schemas/AXI-SCH-029_Organization.json`

The register therefore requires explicit preservation of:

- object identity
- namespace and object-type consistency
- status and lifecycle-state separation
- organization identity metadata
- governance metadata
- ownership metadata
- relationship references
- evidence-based traceability

---

# Required Metadata

| Metadata Group | Minimum Required Elements | Governing Basis |
| --- | --- | --- |
| Identity | `object_id`, `namespace`, `object_type`, `name`, canonical organization name, organization kind, mission alignment, ownership boundary | `ADR-0014`, `ADR-0019`, `AXI-SCH-029` |
| Governance | owner, approval authority, governing ADR references, governing publication references | `ADR-0017`, `ADR-0019`, `AXI-SCH-029` |
| Lifecycle | status, lifecycle state, created and updated timestamps, lifecycle-record linkage when governed transitions occur | `ADR-0015`, `AXI-SCH-015`, `AXI-SCH-029` |
| Ownership | accountable owner, steward role references, parent-organization reference when applicable | `ADR-0014`, `ADR-0019`, `AXI-SCH-029` |
| Relationships | related organization, person, role, policy, timeline, resource, dependency, and knowledge references | `ADR-0014`, `ADR-0019`, `AXI-SCH-029` |
| Traceability | evidence references, publication references, related decision references, lifecycle-record references | `ADR-0014`, `ADR-0015`, `ADR-0017`, `AXI-SCH-029` |

---

# Lifecycle And Stewardship Rules

- Organization registration shall preserve the distinction between
  publication status and lifecycle state.
- Lifecycle interpretation shall reuse the governed state model from
  `ADR-0015`.
- Transition of a governed organization record into `Review`,
  `Deprecated`, `Archive Candidate`, `Archived`, `Historical`, or
  `Eligible for Disposal` shall remain traceable through governed
  lifecycle evidence rather than narrative alone.
- No registered organization object may be removed from canon solely
  because a presentation artifact, report, or runtime view stops using
  it.

---

# Validation Rules

The register shall reject organization records that:

- omit required identity, governance, ownership, relationship, or
  traceability metadata
- use a namespace other than `AXI-PLT`
- use an object type other than `Organization`
- collapse operating context, regulatory knowledge, readiness, or
  presentation semantics into the organization record
- omit evidence references for organizational identity or boundary
  claims
- reference unresolved ADR, publication, decision, lifecycle, or
  related-object identifiers
- create self-referential parent-organization lineage

---

# Traceability Rules

- Every governed organization record shall preserve evidence-based
  support for its identity and ownership boundary.
- If organizational meaning changes because of a decision, outcome,
  lesson, or review, the related decision and lifecycle evidence shall
  remain traceable.
- If a publication, dashboard, or diagram renders organization-domain
  meaning, the organization record shall remain the authoritative
  upstream object rather than the rendered artifact.

---

# Related

- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/ADR/ADR-0019_Organization_Intelligence_and_Core_ODT_Schema_Governance.md`
- `Governance/Schemas/AXI-SCH-015_Information_Lifecycle_Record.json`
- `Governance/Schemas/AXI-SCH-029_Organization.json`
- `Governance/Publications/AXI_Organization_Intelligence_Architecture.md`
- `Governance/Publications/Diagrams/DGM-008_Organization_Intelligence_ODT_Foundation_Map.md`
