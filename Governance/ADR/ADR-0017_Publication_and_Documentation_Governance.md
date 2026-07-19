# ADR-0017 — Establish Publication and Documentation Governance

## Status

Accepted

---

## Purpose

Define the architectural governance required to treat AXI publications,
manuals, and diagrams as governed platform objects rather than
supporting material.

This ADR publishes the governing architecture for:

- publication philosophy and hierarchy
- publication relationships and cross-reference rules
- constitutional transition-gate governance as a publication family
- publication lifecycle and versioning
- review requirements and approval authorities
- operating and field manual architecture baselines
- governed diagram artifacts and visualization synchronization
- documentation quality expectations

---

## Repository Evidence

The repository already publishes the following relevant evidence:

- `ADR-0014` establishes AXI's Decision Intelligence architecture
  baseline and requires traceability, explainability, provenance, human
  accountability, and Organizational Digital Twin updates.
- `ADR-0015` establishes state separation between publication status,
  information lifecycle, workflow status, risk, severity, and review
  authority, and publishes the canonical repository health model.
- `ADR-0016` establishes the operating context, regulatory knowledge,
  and readiness architecture that future operational documentation must
  preserve without dilution.
- `CAPABILITY_REGISTER` publishes repository stewardship capabilities,
  but no published capability currently governs publications and
  diagrams as a first-class repository subsystem.
- `SCHEMA_REGISTRY` publishes `AXI-SCH-006` through `AXI-SCH-021`, but
  no published schema currently governs publication metadata or diagram
  metadata.

Before publication of this ADR, the repository does not publish:

- a canonical publication object model
- an approved publication hierarchy for manuals, standards, and
  operational documentation
- a governed architecture for AXI's Operating Manual or Field Manual
- a governed diagram model with versioning, review history, and
  completeness validation

---

## Architectural Policy

Adopt the following publication and documentation governance baseline.

### 1. Documentation Philosophy

Documentation is a governed AXI subsystem.

Publications are platform objects that preserve architectural,
operational, and expertise knowledge in reviewable form.

Publications shall not be treated as optional illustrations, informal
notes, or secondary artifacts.

If a publication conflicts with an approved ADR, schema, contract, or
constitutional rule, the approved higher-authority artifact governs.

### 2. Publication Hierarchy

AXI shall use the following canonical publication hierarchy:

- `Constitutional Core`: Constitution and Operating System
- `Architecture and Governance Core`: ADR, Standard, Policy, Schema,
  Register, Artifact Specification, Transition Gate
- `Operational Guidance`: Operating Manual, Procedure (SOP), Workflow,
  Checklist, Guide, Reference
- `Applied Practice`: Field Manual, Playbook, Tutorial, Training Module
- `Visual Governance`: Architecture Diagram, Flow Diagram, Decision
  Tree

Publication hierarchy determines interpretation authority.

Higher layers govern lower layers.

Lower layers operationalize higher layers and shall not override them.

### 3. Publication Relationships

The canonical publication relationship model is:

- Constitutional publications define the non-bypassable principles and
  operating system of AXI.
- ADRs define architectural decisions and control boundaries.
- Standards, policies, schemas, registers, and artifact
  specifications operationalize those decisions in reusable governed
  forms.
- Transition Gates determine whether a constitutional phase change is
  authorized by current repository evidence; they shall not invent
  completion, infer acceptance from conversation context, or override
  the upstream governance they evaluate.
- The Operating Manual consolidates how the platform operates while
  remaining subordinate to constitutional and architectural governance.
- The Field Manual converts governed methodology and expertise into
  use-case playbooks while remaining subordinate to constitutional,
  architectural, and operating-manual governance.
- Diagrams visualize governed knowledge and may clarify structure,
  sequence, state, or relationship, but shall not introduce
  architecture, policy, or capability that is not already approved.

### 4. Publication Lifecycle and State Separation

Publication governance shall preserve the distinction between:

- publication status
- information lifecycle state
- review workflow status
- approval authority

Approved publications still participate in the information lifecycle
defined by `ADR-0015`.

Every governed publication and diagram shall preserve, at minimum:

- a publication or diagram identifier
- version
- publication status
- lifecycle state
- owner
- review cycle
- approval authority
- traceability references

### 5. Versioning Strategy

Publication and diagram versioning shall use governed semantic intent:

- major version changes for meaning, control-boundary, or
  interpretation changes
- minor version changes for approved scope expansion or materially new
  governed sections that preserve the existing interpretation
- patch version changes for clarifications, reference repair, or other
  edits that do not change governed meaning

When a diagram changes architectural meaning, the diagram version shall
change in lockstep with the governing publication update that
introduced that meaning.

### 6. Traceability and Cross-Reference Standard

Every governed publication shall preserve explicit traceability to the
authority it operationalizes.

At minimum, governed publications shall preserve references to:

- governing ADRs
- related schemas
- related capabilities where applicable
- dependencies
- supersession relationships
- source or derived diagrams where applicable

Cross-references shall use stable identifiers rather than narrative-only
phrasing wherever possible.

### 7. Review Requirements and Approval Authorities

The default review model is:

- Constitutional, architectural, schema, standard, register, artifact
  specification, transition-gate, and diagram artifacts: annual review
  plus change-triggered review, with milestone-closeout review when
  the artifact governs a milestone transition
- Operating manual, procedure, workflow, checklist, guide, reference,
  field manual, playbook, tutorial, and training artifacts: semiannual
  review plus change-triggered review

Transition-gate evaluation results shall also be reviewed whenever the
underlying milestone, roadmap, repository-status, or dependency
evidence changes in a way that could affect gate state.

The default approval model is:

- Constitution, ADR, Standard, Policy, Schema, Register, Artifact
  Specification, Transition Gate: AXI Platform Governance
- Operating Manual and Field Manual architecture artifacts: domain
  owner plus AXI Platform Governance
- Diagram artifacts: the same authority as the source publication, with
  AXI Platform Governance required whenever the diagram affects
  architectural meaning

Until narrower domain owners are published, AXI Platform Governance
acts as the current domain owner for architecture-only manual
baselines.

Future publications may narrow review ownership, but they shall not
remove human accountability.

### 8. Operating Manual Baseline

AXI shall maintain a governed Operating Manual publication family.

The Operating Manual is the canonical operational interpretation layer
for the platform.

It shall publish the approved volume topology for:

- Foundations
- Platform Operations
- Decision Intelligence
- Knowledge Management
- Repository Stewardship
- Organization Intelligence
- Expertise Engineering
- Governance
- Administration
- Reference

This ADR approves the architecture and table of contents only.

It does not approve full operational prose for those volumes.

### 9. Field Manual Baseline

AXI shall maintain a governed Field Manual publication family.

The Field Manual is the canonical applied-practice layer that converts
Decision Intelligence methodology and governed expertise into practical
playbooks.

This ADR approves the architecture and table of contents only for the
initial domains:

- Prospect Research
- Executive Discovery
- Sales Preparation
- Organizational Diagnostics
- Due Diligence
- Strategic Planning
- Board Support
- Government Decision Support
- Nonprofit Advisory
- Startup Evaluation
- Partnership Assessment
- Vendor Evaluation

### 10. Diagram Governance

Architectural diagrams are governed artifacts, not merely
illustrations.

Every governed diagram shall preserve:

- unique diagram identifier
- version
- status
- lifecycle state
- owner
- review cycle
- approval authority
- source publication
- related ADRs
- related schemas
- revision history
- review history

Every governed diagram shall be updated whenever its source
publication, governing ADR, or visualized schema changes in a way that
affects diagram meaning.

Diagram completeness shall be validated through a governed diagram
register.

Every major published architectural domain shall have at least one
canonical approved diagram before AXI treats that domain as visually
complete.

### 11. Documentation Quality

Documentation quality shall be measured explicitly.

The canonical documentation quality metrics are:

- Coverage
- Traceability
- Diagram Coverage
- Cross-reference Integrity
- Publication Freshness
- Review Compliance
- Completeness
- Canonical Consistency
- Readability
- Reuse

These metrics may feed repository health dimensions published by
`ADR-0015`, but documentation quality remains an explicit governed
surface rather than an implicit side effect.

### 12. Future Integration Boundary

The publication architecture shall support future:

- interactive manuals
- searchable governed knowledge
- embedded Decision Intelligence guidance
- context-aware guidance
- training modules
- AXI Academy publications
- executive brief generation

This ADR does not authorize implementation of those capabilities.

It publishes the metadata and traceability architecture required so
that future integration does not require redesign of the documentation
subsystem.

### 13. Constitutional Validation Extension

Future publications that guide decisions or operationalize decision
methodology shall preserve explicit support for:

- evidence
- provenance
- explainability
- traceability
- human accountability
- assumptions
- confidence
- uncertainty
- ethics
- alternative analysis
- capacity awareness
- calendar awareness
- human factors
- strategic alignment

---

## Non-Goals

This ADR does not approve:

- automated publication generation
- automated diagram synchronization
- runtime documentation services
- interactive manuals
- training delivery implementation
- any claim that AXI currently performs publication governance in
  runtime software

---

## Related

- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/ADR/ADR-0016_Decision_Support_Context_Governance.md`
- `Governance/ADR/ADR-0021_Constitutional_Transition_Gate_Governance.md`
- `Governance/Schemas/AXI-SCH-022_Publication.json`
- `Governance/Schemas/AXI-SCH-023_Diagram.json`
- `Governance/Publications/PUBLICATION_REGISTER.md`
- `Governance/Publications/DIAGRAM_REGISTER.md`
- `Governance/Publications/AXI_Operating_Manual_Architecture.md`
- `Governance/Publications/AXI_Field_Manual_Architecture.md`
- `Governance/Standards/DOCUMENTATION_VISUALIZATION_STANDARD.md`
- `Governance/Standards/DOCUMENTATION_QUALITY_STANDARD.md`
