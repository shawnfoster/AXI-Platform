# Documentation Visualization Standard

**Publication ID:** `PUB-005`
**Publication Type:** `Standard`
**Version:** `1.2.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Annual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Audit Date:** `2026-07-19`

---

# Purpose

Publish the governing standard for diagrams used throughout AXI.

Diagrams are governed knowledge artifacts and must remain synchronized
with the publications they visualize.

---

# Approved Diagram Categories

The approved diagram categories are:

- Platform Architecture
- Object Relationships
- Decision Lifecycle
- Organizational Digital Twin
- Knowledge Architecture
- Repository Lifecycle
- Information Lifecycle
- Archive Lifecycle
- Review and Quarantine Workflow
- Readiness Framework
- Decision Pipelines
- Capability Maps
- Engine Layering
- Workflow Diagrams
- State Machines
- Sequence Diagrams
- Data Flow
- Dependency Graphs
- Organizational Operating Context
- Presentation Architecture
- Dashboard Architecture
- Design System Architecture
- Visualization Standards

---

# Notation Policy

The default notation standard for governed repository publications is
`Mermaid` embedded in Markdown.

`UML` or `BPMN` may be used only when the source publication requires a
notation that Mermaid cannot express clearly enough.

Hybrid notation requires explicit justification in the source
publication or diagram metadata.

---

# Required Diagram Metadata

Every governed diagram shall preserve:

- diagram identifier
- version
- status
- lifecycle state
- owner
- review cycle
- approval authority
- source publication reference
- notation
- category membership
- related ADR references
- related schema references
- revision history
- review history
- synchronization triggers

---

# Diagram Timestamp And Evidence Policy

- Diagram revision and review histories shall prefer immutable
  repository evidence wherever practical.
- Prefer diagram identifiers, version identifiers, source publication
  identifiers, governing ADR identifiers, milestone identifiers,
  publication status, and commit identifiers over narrative date prose
  when those identifiers are sufficient.
- When date-based traceability is required, use ISO `YYYY-MM-DD`
  values rather than natural-language dates.
- When a changed diagram set requires an `Audit Date` or equivalent
  review timestamp, use the execution environment date consistently
  across the changed artifacts.
- Do not rewrite historical revision or review entries solely because a
  conversational reference uses a different clock.

---

# Diagram Placement and Storage

- Canonical architectural diagrams shall be stored as source-controlled
  repository artifacts.
- Markdown-based diagram artifacts shall live under
  `Governance/Publications/Diagrams/` unless a later approved
  publication defines a narrower location for a specialized publication
  family.
- Diagrams embedded in larger publications still require a governed
  diagram record and identifier if they carry architectural meaning.

---

# Synchronization Rules

- A governed diagram shall be reviewed whenever its source publication
  changes in a way that affects diagram meaning.
- A governed diagram shall be reviewed whenever a referenced ADR or
  schema changes a visualized boundary, relationship, lifecycle,
  sequence, or object definition.
- A source publication shall not claim diagram completeness unless the
  corresponding canonical diagram artifacts are current.

---

# Completeness Validation

Diagram completeness is governed, not assumed.

The minimum completeness rule is:

- every major published architectural domain shall have at least one
  approved canonical diagram recorded in `DIAGRAM_REGISTER`
- every major publication shall record whether a canonical diagram is
  required for completeness
- every approved diagram shall identify whether it counts toward major
  domain completeness

Diagram completeness shall be reviewed whenever a new major
architectural domain is published.

---

# Presentation Rules

- Use stable identifiers and approved domain vocabulary in labels.
- Keep diagrams bounded to a clear purpose rather than mixing unrelated
  concerns.
- Show authoritative relationships, not speculative implementation.
- Include legends or explanatory notes when notation or directionality
  might be ambiguous.
- Preserve readability in Markdown-first rendering.

---

# Related

- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/ADR/ADR-0018_Presentation_Services_Governance.md`
- `Governance/Standards/DOCUMENTATION_QUALITY_STANDARD.md`
- `Governance/Publications/DIAGRAM_REGISTER.md`
- `Governance/Schemas/AXI-SCH-023_Diagram.json`
