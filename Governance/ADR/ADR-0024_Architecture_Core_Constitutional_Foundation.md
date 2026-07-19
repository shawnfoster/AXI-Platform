# ADR-0024 — Establish Architecture Core Constitutional Foundation

## Status

Accepted

---

## Purpose

Define the constitutional foundation required to govern AXI through one
shared Architecture Core rather than as a disconnected set of
object-family rules.

This ADR publishes the governing architecture for:

- the constitutional primitive set shared across major governed AXI
  families
- the Architecture Core layer model
- shared identity, state-surface, operation, transformation,
  relationship, authority, evidence, and lineage rules
- repository-wide constitutional invariants
- family-specific specialization boundaries that remain subordinate to
  the shared core

---

## Repository Evidence

The repository already publishes the following relevant evidence:

- `ADR-0014` establishes Decision Intelligence, the Decision as the
  primary governed object, platform-object identity, provenance,
  explainability, human approval, and Organizational Digital Twin
  update responsibilities.
- `ADR-0015` establishes information lifecycle governance, review and
  quarantine controls, repository-health assessment, archival, and
  explicit state separation between lifecycle, review, risk, severity,
  and authority.
- `ADR-0016` distinguishes durable organizational meaning from
  operating context, regulatory knowledge, and readiness inputs.
- `ADR-0017` establishes publication hierarchy, traceability,
  publication state, diagram completeness, and constitutional
  interpretation boundaries.
- `ADR-0018` establishes downstream-rendering boundaries and inherited
  posture for dashboards, widgets, visualizations, and governed
  presentation artifacts.
- `ADR-0019` establishes Organization Intelligence and the first core
  `ODT` schema-and-register baseline.
- `ADR-0020` publishes Knowledge Expansion and Repository
  Operationalization, including a governed progression from discovery
  through operationalization and downstream pack boundaries.
- `ADR-0021` establishes Constitutional Transition Gates as
  repository-evidence controls for major phase transitions.
- `ADR-0022` establishes Prompt Operations as a governed routing layer
  that remains subordinate to repository authority.
- `ADR-0023` establishes Information Governance and Knowledge
  Protection as durable upstream metadata for canonical `Knowledge`
  objects.
- `AXI-SCH-006`, `AXI-SCH-007`, `AXI-SCH-015`, `AXI-SCH-018`,
  `AXI-SCH-022`, `AXI-SCH-023`, `AXI-SCH-029`, `AXI-SCH-030`, and
  `AXI-SCH-031` publish the current governed structures most directly
  involved in identity, lifecycle, review, publication, organization,
  knowledge, and protection posture.
- `PUB-011`, `PUB-018`, `DGM-008`, and `DGM-009` already expose a
  cross-domain architectural convergence that is wider than any one
  object family.

Before publication of this ADR, the repository does not publish:

- one explicit constitutional foundation that consolidates the common
  architecture already implied across object families
- one shared operation vocabulary that spans the published
  constitutional domains
- one shared rule set for when identity persists, when state changes,
  when lineage must be preserved, and how downstream artifacts remain
  subordinate to source authority

---

## Architectural Policy

Adopt the following Architecture Core constitutional foundation.

### 1. Architecture Core As Constitutional Floor

The Architecture Core is a first-class constitutional foundation of
AXI.

Its purpose is to define the minimum shared architecture every future
AXI governance artifact must satisfy before family-specific behavior is
added.

The Architecture Core does not replace the Constitution, accepted ADRs,
or published schemas.

It is the common architectural floor that explains how those artifacts
relate across object families.

### 2. Constitutional Primitive Set

AXI shall use the following constitutional primitives:

- `Object`
- `Identity`
- `State Surface`
- `Operation`
- `Relationship`
- `Authority`
- `Evidence`
- `Lineage`

These primitives are the minimum shared set required to explain the
repository's current governed object families.

Future governance shall not add another primitive unless later
repository evidence proves the current set is insufficient.

### 3. Architecture Core Layers

The canonical Architecture Core layers are:

1. Identity and Object Baseline
2. State-Surface Model
3. Authority and Evidence Control
4. Operations and Transformations
5. Relationship and Lineage
6. Family Specialization
7. Downstream Operationalization and Preservation

These layers define interpretation order.

Lower layers may not override higher layers.

Family specialization remains valid only when it preserves the shared
core above it.

### 4. Constitutional Invariants

Every future governance artifact that participates in the Architecture
Core shall preserve the following invariants:

- identity exists before governance acts on an object
- orthogonal state surfaces remain distinguishable
- no constitutional change is self-authorizing
- evidence justifies governed interpretation and change
- lineage preserves historical continuity across revision,
  transformation, promotion, derivation, supersession, and archival
- downstream artifacts remain subordinate to their governed sources
- preservation outranks deletion when constitutional history would
  otherwise be lost

### 5. State-Surface Separation Rule

AXI governs multiple independent state surfaces.

At minimum, future governance shall distinguish where applicable:

- publication status
- information lifecycle state
- review or quarantine workflow state
- approval authority and authorization boundary
- protection posture
- route or milestone state when the artifact is a prompt or work-item
  control surface

No future governance shall collapse those surfaces into one generic
lifecycle unless a later ADR proves that collapse is a valid
family-specific exception.

### 6. Operation Vocabulary

The repository evidence supports the following primitive constitutional
operations:

- `Identify`
- `Register`
- `Classify`
- `Validate`
- `Review`
- `Authorize`
- `Transform`
- `Preserve`

The repository evidence also supports the following derived operations
when governed by the primitive set above:

- `Approve`
- `Reject`
- `Release`
- `Revise`
- `Derive`
- `Aggregate`
- `Normalize`
- `Deduplicate`
- `Canonicalize`
- `Operationalize`
- `Publish`
- `Synchronize`
- `Supersede`
- `Deprecate`
- `Archive`
- `Restore`

Future governance may specialize these operations for individual object
families, but it shall not treat family-specific labels as an excuse to
abandon the shared operation model.

### 7. Transformation Vocabulary

AXI shall preserve the following shared transformation meanings:

- `Revision` updates governed content without creating a new object
  family
- `Transformation` changes governed state or representation under
  explicit authority
- `Promotion` advances an object into a higher-trust or more
  authoritative role
- `Derivation` produces a downstream artifact from governed sources
- `Aggregation` combines governed sources while preserving source
  lineage
- `Operationalization` converts governed knowledge into an operating
  posture or downstream work surface without creating a competing canon
- `Publication` releases approved knowledge in governed documentary
  form
- `Supersession` replaces an active interpretation while preserving the
  historical chain
- `Archival` preserves governed history outside active use
- `Canonicalization` establishes the authoritative governed variant

Future schemas and publications shall preserve these meanings unless a
later ADR narrows them explicitly.

### 8. Identity And Lineage Rules

AXI shall use the following identity rules:

- revision preserves identity
- transformation may preserve identity when the governing object
  remains the same constitutional entity
- derivation creates a downstream identity while preserving a source
  lineage chain
- aggregation creates a derived identity with explicit multi-source
  lineage
- supersession preserves predecessor lineage rather than erasing it
- archival preserves historical identity even when the object leaves
  active use

Future governance shall state clearly whether a change is a revision of
an existing identity or the creation of a new identity with lineage
back to prior governed sources.

### 9. Authority And Evidence Model

Authority and evidence are orthogonal to object content.

Future governance shall preserve the following rules:

- authority determines who may authorize a constitutional action
- evidence determines what justifies a constitutional action
- evidence shall not be treated as self-authorizing
- authority shall not be exercised without traceable evidence when the
  artifact family requires reviewable change
- prompt routes, rendered artifacts, and downstream packs may route or
  present authority, but they shall not outrank the upstream governing
  source

### 10. Relationship Model

AXI shall preserve explicit constitutional relationships across object
families.

At minimum, future governance may use relationship classes such as:

- governing
- dependency
- contextual
- evidentiary
- derivational
- operationalization or rendering
- succession or preservation

Relationship labels may be specialized by family, but the repository
shall preserve explicit relationship meaning wherever authority,
evidence, derivation, or dependency interpretation depends on it.

### 11. Family Specialization Boundary

Family-specific behavior remains valid only where it does not break the
Architecture Core.

At minimum:

- Decisions remain AXI's primary governed execution objects.
- `ReviewCase` remains the quarantine and unresolved-review family.
- Publications and diagrams remain dissemination and visualization
  families.
- Knowledge remains canonical where the repository already publishes it
  as such.
- Repository Operationalization remains a downstream transformation and
  operating-posture concern rather than a competing canon.
- Prompt Operations remains a routing layer and may preserve a
  composite route-state surface as a valid family-specific exception.
- Presentation artifacts remain downstream governed consumers and do
  not become systems of record.

### 12. Publication Boundary

This ADR authorizes:

- one formal Architecture Core constitutional milestone
- one Architecture Core constitutional publication
- one canonical diagram for the new major architectural domain
- the status, register, route, and roadmap updates required to keep
  repository evidence synchronized

This ADR does not authorize:

- runtime implementation
- schema creation
- contract creation
- new object-family publication beyond the Architecture Core
- transition-gate expansion by default
- milestone advancement beyond the currently published repository state

---

## Future Guidance

Future governance should use the Architecture Core as the constitutional
floor for:

1. later object-family schemas and registers
2. later governance reviews and milestone planning
3. later operationalization and implementation-planning milestones
4. later constitutional exception analysis when a family appears to
   diverge from the shared model

Those follow-on milestones are not authorized by this ADR.

---

## Non-Goals

This ADR does not approve:

- a new runtime boundary
- a new platform-object family
- a new schema family
- automatic transition evaluation
- runtime enforcement of operation semantics
- expansion of the primitive set

---

## Related

- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/ADR/ADR-0016_Decision_Support_Context_Governance.md`
- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/ADR/ADR-0018_Presentation_Services_Governance.md`
- `Governance/ADR/ADR-0019_Organization_Intelligence_and_Core_ODT_Schema_Governance.md`
- `Governance/ADR/ADR-0020_Knowledge_Expansion_and_Repository_Operationalization_Governance.md`
- `Governance/ADR/ADR-0021_Constitutional_Transition_Gate_Governance.md`
- `Governance/ADR/ADR-0022_Prompt_Operations_Manual_Governance.md`
- `Governance/ADR/ADR-0023_Information_Governance_and_Knowledge_Protection_Governance.md`
- `Governance/WorkQueue/M24-Architecture-Core.md`
- `Governance/Publications/AXI_Architecture_Core_Operating_System.md`
- `Governance/Publications/Diagrams/DGM-010_Architecture_Core_Constitutional_Topology.md`
- `Governance/Publications/PUBLICATION_REGISTER.md`
- `Governance/Publications/DIAGRAM_REGISTER.md`
- `Governance/Roadmap/AXI_Roadmap_v1.0.md`
