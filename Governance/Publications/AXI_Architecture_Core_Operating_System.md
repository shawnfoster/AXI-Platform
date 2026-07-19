# AXI Architecture Core Operating System

**Publication ID:** `PUB-019`
**Publication Type:** `Operating System`
**Version:** `1.0.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Annual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Audit Date:** `2026-07-19`
**Related Diagram:** `DGM-010`

---

# Purpose

Publish the Architecture Core as the constitutional operating system of
AXI.

This publication consolidates the repository's shared architectural
floor across governed object families without reopening architectural
discovery, extending the primitive set, or authorizing implementation.

It defines the minimum constitutional model every future governance
artifact must satisfy.

---

# Repository Evidence

The repository already publishes the following relevant evidence:

- `ADR-0014` establishes the Decision as the primary governed object,
  preserves platform-object identity, and requires provenance,
  explainability, and human accountability.
- `ADR-0015` establishes information lifecycle, review, archival,
  stewardship, and explicit state-surface separation.
- `ADR-0016` distinguishes durable organizational meaning from
  operating context, regulatory knowledge, and readiness inputs.
- `ADR-0017` establishes governed publication hierarchy, traceability,
  review, and diagram completeness.
- `ADR-0018` establishes downstream-rendered artifacts as governed
  consumers rather than systems of record.
- `ADR-0019` establishes Organization Intelligence and the first
  constitutional `ODT` baseline.
- `ADR-0020` establishes Knowledge Expansion and Repository
  Operationalization as governed progression and transformation
  boundaries.
- `ADR-0021` establishes Constitutional Transition Gates as
  repository-evidence controls.
- `ADR-0022` establishes Prompt Operations as a governed routing
  layer.
- `ADR-0023` establishes durable Information Governance and Knowledge
  Protection for canonical `Knowledge`.
- `AXI-SCH-006`, `AXI-SCH-007`, `AXI-SCH-015`, `AXI-SCH-018`,
  `AXI-SCH-022`, `AXI-SCH-023`, `AXI-SCH-029`, `AXI-SCH-030`, and
  `AXI-SCH-031` publish the current canonical structures most directly
  involved in identity, state, review, publication, organization,
  knowledge, and protection posture.
- `PUB-011`, `PUB-018`, `DGM-008`, and `DGM-009` already expose a
  repository-wide cross-domain pattern wider than any one published
  family.
- `ADR-0024` publishes the governing Architecture Core constitutional
  foundation for this operating-system baseline.

Before publication of this operating system, the repository did not
publish a single constitutional publication that unified those shared
patterns into one architectural floor.

---

# Constitutional Role

The Architecture Core exists because AXI has outgrown object-family
governance treated as isolated local rules.

The repository now governs decisions, knowledge, review cases,
publications, diagrams, prompt routes, operationalization, and
information posture through a shared architecture that must remain
explicit if future governance is to stay coherent.

This publication is that explicit foundation.

It does not replace the Constitution or the accepted ADR set.

It defines the operating system through which those artifacts are to be
interpreted together.

---

# Constitutional Primitives

| Primitive | Constitutional Responsibility | Why It Is Required |
| --- | --- | --- |
| `Object` | The governed thing AXI recognizes and acts upon. | AXI governance is applied to identifiable artifacts, records, publications, and downstream derivatives rather than to free-floating narrative. |
| `Identity` | The stable referent that persists across governed activity. | The repository distinguishes revision from derivation, preserves unique identifiers, and prevents ambiguous authority. |
| `State Surface` | The independent status dimensions through which governance interprets current condition. | The repository already separates publication status, lifecycle, review, gate state, and protection posture. |
| `Operation` | The authorized constitutional action applied to an object. | Repository behavior is governed through explicit actions such as review, authorization, publication, operationalization, supersession, and archival. |
| `Relationship` | The explicit connection by which objects depend on, derive from, contextualize, or govern one another. | Traceability, dependency ordering, and downstream-subordination all rely on governed relationship meaning. |
| `Authority` | The human or governed source that may authorize a constitutional action. | Repository evidence consistently preserves approval authority and non-self-authorizing change. |
| `Evidence` | The basis that justifies a constitutional interpretation, review outcome, or change. | Provenance, reviewability, and repository-evidence transition rules require justification independent of content narrative. |
| `Lineage` | The continuity chain that preserves history across revision, transformation, promotion, derivation, supersession, and archival. | AXI preserves historical continuity instead of overwriting constitutional meaning. |

---

# Architecture Core Layers

| Layer | Responsibility | Boundary |
| --- | --- | --- |
| 1. Identity and Object Baseline | Defines what exists, what it is, and how it is uniquely referenced. | No later layer may dissolve object identity into workflow narrative. |
| 2. State-Surface Model | Separates the independent condition surfaces through which governance interprets an object. | No later layer may collapse orthogonal states into one generic lifecycle without explicit exception governance. |
| 3. Authority and Evidence Control | Defines who may act and what justifies action. | Evidence does not self-authorize; authority is not content. |
| 4. Operations and Transformations | Defines what constitutional actions may occur and how those actions change state or produce derivations. | Family-specific verbs remain subordinate to the shared operation model. |
| 5. Relationship and Lineage | Preserves dependency, derivation, succession, and historical continuity. | No downstream artifact may become detached from its source chain. |
| 6. Family Specialization | Allows Decisions, Knowledge, ReviewCases, Publications, and other families to keep valid local behavior. | Specialization may not violate the layers above it. |
| 7. Downstream Operationalization and Preservation | Governs publication, rendering, packs, routing, archives, and other derived surfaces. | Downstream surfaces may consume or operationalize source meaning but may not outrank it. |

---

# Constitutional Invariants

Every future governance artifact that participates in the Architecture
Core shall preserve these invariants:

- identity is stable before an operation is authorized
- state surfaces remain orthogonal unless a governed exception is
  explicit
- authority is never implied merely because an artifact exists
- evidence is required where reviewable constitutional change is
  claimed
- lineage is preserved across revision, transformation, derivation,
  promotion, supersession, and archival
- downstream artifacts inherit from upstream governed sources rather
  than replacing them
- preservation outranks deletion when constitutional history would be
  lost

---

# State-Surface Model

AXI governs multiple state surfaces rather than one universal
lifecycle.

| State Surface | Typical Meaning | Current Published Examples |
| --- | --- | --- |
| Publication Status | Draft, approved, deprecated, superseded, or archived publication meaning. | `AXI-SCH-022`, publication metadata, `PUBLICATION_REGISTER` |
| Information Lifecycle | Active, review, archived, historical, and related stewardship condition. | `ADR-0015`, `AXI-SCH-015`, `AXI-SCH-030` |
| Review / Quarantine Workflow | Whether unresolved evidence is being held, reviewed, escalated, or released. | `ADR-0015`, `AXI-SCH-018`, imported-content governance |
| Authorization Boundary | Which authority may approve or gate an action. | ADR approval, publication approval, CTGs, prompt-route boundaries |
| Protection Posture | Classification, sharing, retention, privacy, and audit handling. | `ADR-0023`, `AXI-SCH-031`, `AXI-SCH-030` |
| Route / Milestone State | Whether a milestone or prompt route is active, planned, closed, or historical. | Work-queue artifacts, `PUB-017`, `CTG-001` |

The repository shall not treat these surfaces as interchangeable.

Prompt Operations remains a valid family-specific exception where route
state is intentionally composite and subordinate to higher-authority
governance.

---

# Common Operation Vocabulary

## Primitive Operations

| Operation | Constitutional Purpose | Authority / Boundary |
| --- | --- | --- |
| `Identify` | Establish a stable referent for governance. | Required before durable constitutional handling. |
| `Register` | Record the object or artifact in a governed canonical set. | Requires repository-controlled traceability. |
| `Classify` | Assign governed interpretive categories or posture. | Must remain explicit and reviewable where policy or protection depends on it. |
| `Validate` | Check the object against governing requirements. | Does not approve by itself. |
| `Review` | Examine unresolved, sensitive, or consequential change under governance. | May hold, escalate, or route for human approval. |
| `Authorize` | Approve, reject, release, or otherwise decide a governed action boundary. | Never implied by artifact existence alone. |
| `Transform` | Change state, meaning, or representation under governed rules. | Must preserve identity or lineage explicitly. |
| `Preserve` | Retain constitutional continuity, history, and accessibility. | Outranks convenience deletion. |

## Derived Operations

The repository also already implies or publishes these derived
operations:

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

These remain subordinate to the primitive model above.

---

# Common Transformation Vocabulary

| Transformation | Core Meaning | Identity Effect |
| --- | --- | --- |
| `Revision` | Updates governed content or metadata while preserving the same constitutional entity. | Preserves identity. |
| `Transformation` | Applies an authorized constitutional change in state or representation. | May preserve identity if the governed entity remains the same. |
| `Promotion` | Raises an artifact into a higher-authority or higher-trust governed role. | Preserves lineage and may preserve identity depending on family rules. |
| `Derivation` | Produces a downstream artifact from governed sources. | Creates a new downstream identity with source lineage. |
| `Aggregation` | Combines multiple governed sources into a derived whole. | Creates a derived identity with multi-source lineage. |
| `Operationalization` | Converts governed knowledge into an operating posture or downstream work surface. | Creates derived operational surfaces without a competing canon. |
| `Publication` | Releases approved governed meaning as documentary authority. | Creates or revises publication identity under publication governance. |
| `Supersession` | Replaces an active interpretation while preserving historical continuity. | Preserves predecessor lineage. |
| `Archival` | Preserves governed history outside active use. | Preserves historical identity and access path. |
| `Canonicalization` | Establishes the authoritative governed variant among candidates or alternates. | Preserves alternates and rationale through lineage. |

---

# Identity Rules

Future governance shall preserve the following identity rules:

- revision preserves object identity
- derivation creates a downstream identity
- aggregation creates a derived identity with explicit multi-source
  provenance
- supersession never erases predecessor identity
- archival preserves historical identity even when active use ends
- canonicalization selects authority without erasing alternates,
  duplicates, or source history

The repository shall state clearly when a change is a revision of an
existing identity and when it creates a new identity with lineage back
to governed sources.

---

# Lineage Model

Lineage is the constitutional continuity mechanism of AXI.

At minimum, lineage shall preserve:

- source references
- derivation path
- supersession chain
- archival continuity
- review or approval events where those events justify a change in
  constitutional standing

Lineage applies across both canonical objects and downstream artifacts.

It is not limited to runtime or data-model concerns.

---

# Authority Model

Authority is orthogonal to object content.

At minimum, future governance shall preserve:

- explicit approval authority where a constitutional action requires
  human or governed approval
- clear authorization boundaries for milestones, transition gates,
  prompt routes, and downstream publications
- the rule that lower-authority artifacts may not relax higher-authority
  governance

Prompt routes, publications, diagrams, rendered artifacts, and future
packs may expose or operationalize authority.

They do not become the origin of that authority unless a governing ADR
states so explicitly.

---

# Evidence Model

Evidence justifies constitutional interpretation and change.

At minimum, future governance shall preserve:

- provenance or source references where the family requires them
- explicit justification for governed review, release, canonicalization,
  or promotion decisions
- the boundary that evidence informs authority but does not replace it

Repository evidence remains the authoritative basis for milestone,
transition, and constitutional completion claims.

---

# Relationship Model

AXI shall preserve explicit relationship meaning across families.

The common relationship classes include:

- governing
- dependency
- contextual
- evidentiary
- derivational
- operationalization or rendering
- succession or preservation

Future governance may specialize these labels, but it shall not make
relationship meaning implicit where authority, dependency, derivation,
or preservation depends on it.

---

# Family-Specific Exceptions

The Architecture Core permits family-specific behavior only where the
shared constitutional floor remains intact.

| Family | Valid Exception | Boundary |
| --- | --- | --- |
| Decisions | Decision remains AXI's primary governed execution object. | The Architecture Core does not replace the decision-centric mission of the platform. |
| ReviewCases | ReviewCase governs unresolved review, quarantine, and release boundaries. | It does not become a replacement canon. |
| Publications / Diagrams | Dissemination and visualization remain first-class constitutional surfaces. | They remain subordinate to their governing ADRs and schemas. |
| Repository Operationalization | Discovery, operational packs, and workspace posture are downstream transformation concerns. | They do not become independent canons or bypass review. |
| Prompt Operations | Route state may remain composite and execution-oriented. | Prompt routes remain routing surfaces, not authority sources. |
| Presentation Services | Dashboards, widgets, and visualizations inherit from governed sources. | They do not become systems of record. |
| Information Governance | Protection posture may add a distinct state surface to canonical `Knowledge`. | It does not replace lifecycle, review, or authority surfaces. |

---

# Architectural Principles For Future Governance

Every future AXI governance artifact should satisfy the following
principles:

1. Reuse the current primitive set unless later evidence proves it
   insufficient.
2. Preserve orthogonal state surfaces.
3. Require explicit authority for consequential constitutional actions.
4. Preserve evidence and lineage for governed change.
5. Keep downstream artifacts subordinate to upstream governing sources.
6. Distinguish revision, derivation, operationalization, publication,
   supersession, and archival explicitly.
7. Prefer preservation over deletion when historical meaning would be
   lost.
8. Treat family-specific exceptions as governed boundaries, not as
   opportunities to bypass the core.

---

# Boundary

This operating system authorizes:

- constitutional interpretation of the shared Architecture Core
- downstream governance alignment to that shared core
- continued use of existing object families and publication types

This operating system does not authorize:

- runtime implementation
- schema authoring
- contract authoring
- new object-family creation
- new primitive creation
- milestone advancement beyond currently published repository evidence

---

# Diagram Boundary

`DGM-010` is the canonical diagram for this operating-system baseline.

That diagram establishes visual completeness for the Architecture Core
as a major architectural domain.

It does not, by itself, authorize implementation or later milestone
execution.

---

# Related

- `Governance/ADR/ADR-0024_Architecture_Core_Constitutional_Foundation.md`
- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/ADR/ADR-0018_Presentation_Services_Governance.md`
- `Governance/ADR/ADR-0019_Organization_Intelligence_and_Core_ODT_Schema_Governance.md`
- `Governance/ADR/ADR-0020_Knowledge_Expansion_and_Repository_Operationalization_Governance.md`
- `Governance/ADR/ADR-0021_Constitutional_Transition_Gate_Governance.md`
- `Governance/ADR/ADR-0022_Prompt_Operations_Manual_Governance.md`
- `Governance/ADR/ADR-0023_Information_Governance_and_Knowledge_Protection_Governance.md`
- `Governance/WorkQueue/M24-Architecture-Core.md`
- `Governance/Publications/PUBLICATION_REGISTER.md`
- `Governance/Publications/DIAGRAM_REGISTER.md`
- `Governance/Publications/AXI_Operating_Manual_Architecture.md`
- `Governance/Publications/Diagrams/DGM-010_Architecture_Core_Constitutional_Topology.md`
- `Governance/Roadmap/AXI_Roadmap_v1.0.md`
