# AXI Knowledge Register

**Publication ID:** `PUB-013`
**Publication Type:** `Register`
**Version:** `1.1.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Semiannual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Audit Date:** `2026-07-19`
**Related Diagram:** `DGM-008`

---

# Purpose

Publish the canonical registration baseline for governed `Knowledge`
objects in AXI.

No knowledge instances are published in this register yet.

This artifact defines the minimum metadata, provenance, lifecycle,
authority, information-governance, dependency, publication, and
traceability expectations that future governed knowledge objects shall
satisfy before they may be treated as canonical Organization
Intelligence knowledge.

---

# Knowledge Boundary

The Knowledge Register governs durable knowledge holdings while
preserving the knowledge-domain separation required by `ADR-0014`.

It therefore governs registration of:

- AXI Methodology knowledge
- External Knowledge
- Organizational Knowledge
- Learned Knowledge

It does not register:

- Regulatory Knowledge as a substitute for organizational knowledge
- Governed Expertise as a substitute for knowledge
- dashboards, diagrams, or reports as canonical knowledge objects

---

# Register Entry Structure

Every governed knowledge record shall preserve at minimum the structure
published by:

- `Governance/Schemas/AXI-SCH-030_Knowledge.json`

The register therefore requires explicit preservation of:

- object identity
- status and lifecycle-state separation
- knowledge-domain designation
- authority metadata
- provenance metadata
- information-governance metadata
- dependency references
- publication references

---

# Required Metadata

| Metadata Group | Minimum Required Elements | Governing Basis |
| --- | --- | --- |
| Identity | `object_id`, `namespace`, `object_type`, `name`, `knowledge_domain`, version, owner | `ADR-0014`, `ADR-0019`, `AXI-SCH-030` |
| Authority | approval authority, authority-scope summary, governing ADR references, governing publication references | `ADR-0017`, `ADR-0019`, `AXI-SCH-030` |
| Provenance | source-artifact references, evidence references, provenance completeness, derived-from knowledge references when applicable | `ADR-0014`, `ADR-0015`, `AXI-SCH-030` |
| Information Governance | stewardship, trust and confidence posture, classification, access policy, sharing policy, retention policy, licensing, regulatory constraints, jurisdictions, privacy requirements, audit requirements, inheritance rule, implementation boundary | `ADR-0023`, `AXI-SCH-030`, `AXI-SCH-031` |
| Lifecycle | status, lifecycle state, created and updated timestamps, lifecycle-record linkage when governed transitions occur | `ADR-0015`, `AXI-SCH-015`, `AXI-SCH-030` |
| Relationships | related organization references and related decision references where knowledge is decision-linked | `ADR-0014`, `ADR-0019`, `AXI-SCH-030` |
| Traceability | dependency references, publication references, review-case references when applicable | `ADR-0015`, `ADR-0017`, `AXI-SCH-030` |

---

# Lifecycle And Stewardship Rules

- Knowledge registration shall preserve the distinction between
  publication status and lifecycle state.
- Lifecycle interpretation shall reuse the governed state model from
  `ADR-0015`.
- Protection posture shall remain first-class governed metadata rather
  than free-form narrative in `metadata`.
- Canonical knowledge shall not move across knowledge domains without
  preserving the provenance and justification for that change.
- A knowledge record may be rendered by publications, dashboards, or
  diagrams, but those rendered artifacts do not replace the registered
  knowledge object.

---

# Protection Inheritance Rules

- Canonical `Knowledge` objects shall preserve a governed protection
  posture that downstream artifacts inherit rather than redefine.
- If multiple governed knowledge sources contribute to one downstream
  publication, dashboard, visualization, prompt route, or future
  rendered artifact, the downstream artifact shall inherit the
  strictest applicable source posture.
- Downstream operationalization shall not relax classification, access,
  sharing, retention, privacy, jurisdiction, or audit posture without
  later approved governance.

---

# Validation Rules

The register shall reject knowledge records that:

- omit required authority, provenance, lifecycle, information-
  governance, dependency, or publication metadata
- use a namespace other than `AXI-PLT`
- use an object type other than `Knowledge`
- collapse Regulatory Knowledge or Governed Expertise into the
  `Knowledge` object family
- place protected-knowledge posture only in free-form `metadata`
  instead of the governed schema fields
- claim canonical knowledge without source-artifact and evidence
  support
- reference unresolved ADR, publication, organization, decision,
  lifecycle, or dependency identifiers
- mix multiple knowledge domains without preserving explicit domain
  designation

---

# Traceability Rules

- Every governed knowledge record shall preserve evidence and
  provenance sufficient to explain why the knowledge is canonical,
  durable, and governable.
- Every governed knowledge record shall preserve protection metadata
  sufficient to explain why the knowledge may be shared, retained,
  operationalized, or restricted.
- If knowledge is derived from a decision, lesson, or publication
  update, the related upstream object or artifact shall remain
  traceable.
- Publication references shall identify where the knowledge is
  operationalized or rendered for governed reuse without relaxing the
  governed protection posture.

---

# Related

- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/ADR/ADR-0016_Decision_Support_Context_Governance.md`
- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/ADR/ADR-0019_Organization_Intelligence_and_Core_ODT_Schema_Governance.md`
- `Governance/ADR/ADR-0023_Information_Governance_and_Knowledge_Protection_Governance.md`
- `Governance/Schemas/AXI-SCH-015_Information_Lifecycle_Record.json`
- `Governance/Schemas/AXI-SCH-030_Knowledge.json`
- `Governance/Schemas/AXI-SCH-031_Information_Governance_Profile.json`
- `Governance/Publications/AXI_Information_Governance_and_Knowledge_Protection_Model.md`
- `Governance/Publications/AXI_Organization_Intelligence_Architecture.md`
- `Governance/Publications/Diagrams/DGM-008_Organization_Intelligence_ODT_Foundation_Map.md`
