# AXI Organization Intelligence Architecture

**Publication ID:** `PUB-011`
**Publication Type:** `Reference`
**Version:** `1.0.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Semiannual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Audit Date:** `2026-07-19`

---

# Purpose

Publish the constitutional architecture for Organization Intelligence
as a governed AXI domain.

This publication explains why Organization Intelligence exists and how
it relates to the already approved decision, knowledge, evidence,
publication, presentation, and future Organizational Digital Twin
architecture before core schemas, registers, runtime objects, or
services are implemented.

---

# Repository Evidence

The repository already publishes the following relevant evidence:

- `ADR-0014` establishes the Decision as the primary governed object,
  elevates the Organizational Digital Twin to a first-class
  architectural domain, and requires outcomes and lessons to support
  explicit Digital Twin updates.
- `ADR-0015` establishes repository stewardship governance, including
  lifecycle, provenance, review, and archival controls that future
  Organization Intelligence artifacts must preserve.
- `ADR-0016` publishes Operating Context, Regulatory Knowledge, and
  Readiness as adjacent governed domains and distinguishes them from
  durable organizational structures and knowledge.
- `ADR-0017` publishes publication and diagram governance, including
  cross-reference integrity, review cycles, and visual-completeness
  rules for new major architectural domains.
- `ADR-0018` publishes presentation-services governance and already
  treats organization-domain objects as downstream governed consumers
  rather than presentation-owned data.
- `ADR-0019` establishes Organization Intelligence as a governed
  architectural domain and authorizes the future core `ODT`
  schema-and-register baseline.
- `M22` authorizes governance-only advancement of the core
  Organization Intelligence and `ODT` domain without authorizing
  runtime implementation.
- `PUB-002` already identifies Organization Intelligence as the sixth
  canonical volume of the AXI Operating Manual.

Before publication of this document, the repository does not publish a
standalone architecture reference explaining the constitutional role of
Organization Intelligence ahead of the schema-and-register baseline.

---

# Why Organization Intelligence Exists

Organization Intelligence exists because AXI must understand an
organization as a governed system, not merely as background context for
isolated decisions.

Without this domain:

- evidence remains disconnected from durable organizational meaning
- knowledge and expertise remain fragmented across engagements,
  outcomes, and publications
- reasoning about alternatives lacks a stable representation of the
  real organization it affects
- future Digital Twin representations risk becoming arbitrary data
  models instead of governed organizational meaning

Organization Intelligence is therefore the architectural discipline
that makes organizational state intelligible, traceable, and governable
across decisions, learning, publications, and later implementation.

---

# Scope

Organization Intelligence governs the meaning of durable organizational
conditions, including:

- organization identity, mission alignment, and ownership boundary
- people and roles as distinct governed concerns
- durable organizational knowledge and governed expertise
- internal policy, timelines, resources, and dependencies
- the traceable update path from decisions, outcomes, observations, and
  lessons into future Organizational Digital Twin state

Organization Intelligence does not replace:

- decision records
- operating context
- regulatory knowledge
- readiness assessment
- dashboards, widgets, visualizations, or other presentation artifacts

---

# Constitutional Role

Organization Intelligence is a governed supporting domain that keeps
AXI's understanding of organizations consistent with human
accountability, explainability, provenance, and traceability.

Its constitutional role is to ensure that decisions, evidence, lessons,
and future rendered artifacts are tied back to durable organizational
meaning instead of ad hoc narrative, temporary analysis, or local
implementation detail.

The Decision remains AXI's primary governed object.

Organization Intelligence exists to make the organizational reality
surrounding decisions reviewable and durable; it does not replace the
decision-centric mission of the platform.

---

# Relationship Model

| Domain | Relationship | Explicit Boundary |
| --- | --- | --- |
| Decision Intelligence | Organization Intelligence supplies the durable organizational meaning that governed decisions, decision context, execution planning, and learning must reference. | It does not replace the Decision as the platform's primary governed object and does not generate recommendations by itself. |
| Governed Reasoning | In this publication, governed reasoning means the approved Reasoning Layer activities published in `ADR-0014`: assumptions, scenarios, forecasts, simulations, and optimization under governance controls. Organization Intelligence provides the stable organizational referents and constraints those activities reason about. | It does not create a separate reasoning service, engine family, or automated approval surface. |
| Platform Objects | Organization Intelligence operates only through the published Platform Object boundary and the future object-family schemas authorized by `ADR-0019`. It gives durable meaning to `Organization`, `Person`, `Role`, `Knowledge`, `Expertise`, `Policy`, `Timeline`, `Resource`, and `Dependency` as governed objects. | It does not bypass `AXI-SCH-007` or invent a parallel object model. |
| Knowledge Objects | Organization Intelligence ties Organizational Knowledge and Governed Expertise to the real organization while preserving the knowledge separation required by `ADR-0014`. | It does not collapse Organizational Knowledge, Learned Knowledge, Regulatory Knowledge, AXI Methodology, and External Knowledge into one undifferentiated domain. |
| Evidence | Evidence informs Organization Intelligence interpretation, stewardship, and updates by providing the basis for what the organization is, knows, can do, or has changed. | It does not treat raw evidence as durable organizational fact without provenance, review, and traceable transition. |
| Organizations | Organization Intelligence treats organizations as governed systems of identity, authority, policy, resources, dependencies, timing, knowledge, and expertise rather than as flat account records or simple directories. | It does not reduce organizations to org charts, contact lists, or compliance labels. |
| Future Digital Twins | Organization Intelligence is the governance and meaning framework that future Organizational Digital Twin representations must implement. The Digital Twin is the governed representation; Organization Intelligence is the architectural rationale that gives that representation meaning. | It does not authorize Digital Twin runtime implementation, persistence design, simulation services, or application behavior. |

---

# Traceability Requirements

Future Organization Intelligence publications, schemas, registers, and
diagrams shall preserve at minimum:

- governing ADR and work-item references
- affected platform-object and schema references where published
- provenance for the evidence, decision, outcome, lesson, or review
  event that justifies an organizational interpretation or change
- explicit boundary references whenever information crosses between
  Organization Intelligence and Operating Context, Regulatory
  Knowledge, Readiness, Publication, or Presentation domains
- lifecycle, ownership, and review state consistent with `ADR-0015`
  and `ADR-0017`
- downstream publication, dashboard, widget, visualization, or diagram
  references when organization-domain meaning is rendered for governed
  consumption

Traceability is required so later schema, register, and runtime work
can distinguish durable organization-domain meaning from temporary,
evaluative, or presentation-specific interpretation.

---

# Governance Boundaries

This publication authorizes:

- explanation of Organization Intelligence purpose and architectural
  role
- cross-domain interpretation consistent with the approved ADR set
- future schema, register, and diagram work already authorized by
  `ADR-0019` and `M22`

This publication does not authorize:

- runtime implementation
- service, engine, API, CLI, GUI, portal, or persistence design
- schema or contract publication for the core `ODT` object families
- database, eventing, or interoperability design
- legal, HR, ERP, or compliance-system claims
- visual completeness for Organization Intelligence before a canonical
  diagram is published and registered

---

# Lifecycle Responsibilities

Organization Intelligence is responsible for:

- preserving durable organizational meaning across the approved object
  families and their later schema expressions
- distinguishing durable organization-domain knowledge from time-bound
  context, regulatory surfacing, and evaluative readiness
- receiving governed updates from decisions, outcomes, observations,
  and lessons through explicit lineage rather than implicit overwrite
- providing stable references for future `ODT` schemas, registers,
  diagrams, engines, applications, and presentation consumers
- remaining reviewable under the repository's publication, lifecycle,
  and stewardship governance

It is not responsible for:

- rendering dashboards
- issuing recommendations
- replacing human approval
- storing ungoverned evidence as canonical organizational truth

---

# M22 Phase Boundary

This publication completes only the architecture-definition portion of
the current `M22` governance cycle.

It does not satisfy the `M22` exit gate by itself.

`M22` remains incomplete until the repository publishes the authorized
core Organization Intelligence and `ODT` schemas and registers.

---

# Diagram Boundary

This publication establishes domain meaning but does not claim visual
completeness for Organization Intelligence.

A future canonical diagram shall be published and recorded in
`DIAGRAM_REGISTER` before AXI treats this domain as diagram-complete.

When published, that diagram shall comply with:

- `ADR-0017`
- `ADR-0019`
- `PUB-004`
- `PUB-005`
- `AS-006 Architecture Diagram`

---

# Related

- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/ADR/ADR-0016_Decision_Support_Context_Governance.md`
- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/ADR/ADR-0018_Presentation_Services_Governance.md`
- `Governance/ADR/ADR-0019_Organization_Intelligence_and_Core_ODT_Schema_Governance.md`
- `Governance/WorkQueue/M22-Core-Organizational-Digital-Twin-and-Knowledge-Object-Schemas.md`
- `Governance/Capabilities/CAPABILITY_REGISTER.md`
- `Governance/Decisions/DECISION_REGISTER.md`
- `Governance/Publications/PUBLICATION_REGISTER.md`
- `Governance/Publications/DIAGRAM_REGISTER.md`
- `Governance/Publications/AXI_Operating_Manual_Architecture.md`
- `Governance/Publications/AXI_Artifact_Specification_Baseline.md`
- `Governance/Roadmap/AXI_Roadmap_v1.0.md`
