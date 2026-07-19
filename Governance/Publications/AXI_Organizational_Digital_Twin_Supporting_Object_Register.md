# AXI Organizational Digital Twin Supporting Object Register

**Publication ID:** `PUB-020`
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

Publish the canonical registration baseline for the remaining governed
core Organizational Digital Twin (`ODT`) object families in AXI.

No object instances are published in this register yet.

This artifact completes the first `M22` schema-and-register baseline by
governing the supporting object families that complement the existing
Organization and Knowledge registers.

It preserves the constitutional separation between:

- `Person`
- `Role`
- `Expertise`
- `Policy`
- `Timeline`
- `Resource`
- `Dependency`

---

# Registration Boundary

This register governs the constitutional representation of the
supporting `ODT` object families required to make durable organization
state reviewable across decisions, knowledge, learning, and downstream
governed presentation surfaces.

It therefore registers:

- individual participants and stakeholders
- responsibility and authority roles
- governed expertise
- internal policy
- governed timelines
- governed resources
- governed dependencies

It does not register:

- organizations as a substitute for `PUB-012`
- knowledge as a substitute for `PUB-013`
- Operating Context
- Regulatory Knowledge
- Readiness Profiles
- dashboards, widgets, or visualizations
- runtime dependency-resolution behavior

Those remain separate governed domains.

---

# Published Canonical Families

| Object Family | Governing Schema | Unique Responsibility | Explicit Boundary |
| --- | --- | --- | --- |
| `Person` | `AXI-SCH-032` | Represent an individual participant, steward, or stakeholder without collapsing that identity into role or authority. | Does not replace `Role`, ownership authority, or organizational identity. |
| `Role` | `AXI-SCH-033` | Represent responsibility, authority, accountability, and reporting context separate from any specific person. | Does not replace `Person` or become a recommendation surface. |
| `Expertise` | `AXI-SCH-034` | Represent governed capability-in-practice, approved competency, and learned patterns that may evolve through lessons and outcomes. | Does not collapse into `Knowledge` or bypass decision and evidence lineage. |
| `Policy` | `AXI-SCH-035` | Represent binding internal governance, constraints, or rules distinct from regulatory-planning material and procedures. | Does not replace `RegulatoryKnowledge`, legal conclusions, or operating procedures. |
| `Timeline` | `AXI-SCH-036` | Represent planned, actual, milestone, and sequencing structures distinct from ambient operating-context calendars. | Does not absorb Operating Context timing or readiness scoring. |
| `Resource` | `AXI-SCH-037` | Represent allocable organizational assets, capacities, or means required for governed execution. | Does not replace readiness assessment or runtime allocation logic. |
| `Dependency` | `AXI-SCH-038` | Represent explicit cross-object reliance, sequencing, or blockage relationships with traceable lineage. | Does not replace the runtime `DependencyResolver` or reduce dependencies to narrative-only notes. |

---

# Register Entry Structure

Every governed supporting-object record shall preserve at minimum the
structure published by its governing schema:

- `Governance/Schemas/AXI-SCH-032_Person.json`
- `Governance/Schemas/AXI-SCH-033_Role.json`
- `Governance/Schemas/AXI-SCH-034_Expertise.json`
- `Governance/Schemas/AXI-SCH-035_Policy.json`
- `Governance/Schemas/AXI-SCH-036_Timeline.json`
- `Governance/Schemas/AXI-SCH-037_Resource.json`
- `Governance/Schemas/AXI-SCH-038_Dependency.json`

Every record therefore requires explicit preservation of:

- object identity
- namespace and object-type consistency
- lifecycle-state and status separation
- governance metadata
- ownership or stewardship metadata
- cross-object relationships
- evidence-based traceability

---

# Required Metadata By Family

| Object Family | Minimum Required Metadata Groups | Governing Basis |
| --- | --- | --- |
| `Person` | identity, affiliation, governance, ownership, relationships, traceability | `ADR-0014`, `ADR-0015`, `ADR-0017`, `ADR-0019`, `AXI-SCH-032` |
| `Role` | role definition, governance, ownership, relationships, traceability | `ADR-0014`, `ADR-0017`, `ADR-0019`, `AXI-SCH-033` |
| `Expertise` | expertise profile, governance, ownership, relationships, traceability | `ADR-0014`, `ADR-0015`, `ADR-0019`, `AXI-SCH-034` |
| `Policy` | policy definition, governance, ownership, relationships, traceability | `ADR-0014`, `ADR-0016`, `ADR-0019`, `AXI-SCH-035` |
| `Timeline` | timeline definition, governance, ownership, relationships, traceability | `ADR-0014`, `ADR-0015`, `ADR-0019`, `AXI-SCH-036` |
| `Resource` | resource profile, governance, ownership, relationships, traceability | `ADR-0014`, `ADR-0015`, `ADR-0019`, `AXI-SCH-037` |
| `Dependency` | dependency definition, governance, ownership, relationships, traceability | `ADR-0014`, `ADR-0015`, `ADR-0019`, `AXI-SCH-038` |

---

# Cross-Family Relationship Rules

- `Person` and `Role` shall remain separate even when one person
  currently occupies one role.
- `Expertise` shall remain separate from `Knowledge`; expertise may
  depend on knowledge, but it does not replace governed knowledge.
- `Policy` shall remain separate from `RegulatoryKnowledge`; internal
  policy may reference regulatory knowledge without collapsing into it.
- `Timeline` shall remain separate from `OperatingContext`; durable
  sequencing and milestone structures do not replace time-bound
  situational calendars.
- `Resource` shall remain separate from `ReadinessProfile`; the
  resource is governed state, while readiness is evaluative
  interpretation.
- `Dependency` shall remain a governed `ODT` object family rather than
  a runtime-only technical concern.

---

# Lifecycle And Stewardship Rules

- Supporting-object registration shall preserve the distinction between
  publication status and lifecycle state.
- Lifecycle interpretation shall reuse the governed state model from
  `ADR-0015`.
- Supporting-object meaning shall remain tied to evidence, decisions,
  publications, lifecycle records, or review outcomes rather than
  conversational assertion.
- No supporting-object record may be removed from canon solely because a
  rendered artifact or future runtime consumer stops using it.

---

# Validation Rules

The register shall reject supporting-object records that:

- omit required governance, ownership, relationship, or traceability
  metadata
- use a namespace other than `AXI-PLT`
- use an object type other than the governed family named by the
  relevant schema
- collapse `Person` into `Role` or `Role` into `Person`
- collapse `Expertise` into `Knowledge`
- treat `Policy` as a replacement for Regulatory Knowledge or
  procedures
- encode ambient execution calendars inside `Timeline` as if they were
  Operating Context
- treat `Resource` as readiness scoring rather than governed capacity
- treat `Dependency` as a runtime implementation artifact rather than a
  governed organizational relationship
- reference unresolved ADR, publication, decision, lifecycle, or
  related-object identifiers

---

# Traceability Rules

- Every supporting-object record shall preserve evidence sufficient to
  explain why its current constitutional meaning is canonical.
- Every supporting-object record shall preserve publication references
  where that meaning is rendered or operationalized for governed reuse.
- If a supporting-object meaning changes because of a decision, lesson,
  review, or publication update, the upstream evidence and related
  decision lineage shall remain traceable.
- Registers, diagrams, and future runtime consumers shall remain
  downstream to these governed object families rather than replacing
  them.

---

# Related

- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/ADR/ADR-0016_Decision_Support_Context_Governance.md`
- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/ADR/ADR-0019_Organization_Intelligence_and_Core_ODT_Schema_Governance.md`
- `Governance/WorkQueue/M22-Core-Organizational-Digital-Twin-and-Knowledge-Object-Schemas.md`
- `Governance/Schemas/AXI-SCH-032_Person.json`
- `Governance/Schemas/AXI-SCH-033_Role.json`
- `Governance/Schemas/AXI-SCH-034_Expertise.json`
- `Governance/Schemas/AXI-SCH-035_Policy.json`
- `Governance/Schemas/AXI-SCH-036_Timeline.json`
- `Governance/Schemas/AXI-SCH-037_Resource.json`
- `Governance/Schemas/AXI-SCH-038_Dependency.json`
- `Governance/Publications/AXI_Organization_Intelligence_Architecture.md`
- `Governance/Publications/AXI_Organization_Register.md`
- `Governance/Publications/AXI_Knowledge_Register.md`
- `Governance/Publications/Diagrams/DGM-008_Organization_Intelligence_ODT_Foundation_Map.md`
