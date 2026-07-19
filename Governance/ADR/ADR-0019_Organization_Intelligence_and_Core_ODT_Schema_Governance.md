# ADR-0019 — Establish Organization Intelligence And Core ODT Schema Governance

## Status

Accepted

---

## Purpose

Define the architectural governance required to publish the first
schema-and-register baseline for Organization Intelligence and the core
Organizational Digital Twin (`ODT`) object domains.

This ADR publishes the governing architecture for:

- Organization Intelligence as a governed architectural domain
- core `ODT` schema boundaries
- core `ODT` register requirements
- cross-domain reference rules between `ODT` objects and the already
  published decision, context, publication, and presentation domains

---

## Repository Evidence

The repository already publishes the following relevant evidence:

- `ADR-0014` establishes the Organizational Digital Twin as a
  first-class architectural domain and names the canonical object set
  that future decision-domain work shall preserve, including
  `Organization`, `Person`, `Role`, `Knowledge`, `Expertise`,
  `Policy`, `Timeline`, `Resource`, and `Dependency`.
- `ADR-0016` publishes Operating Context, Regulatory Knowledge, and
  Readiness as adjacent governed decision-support domains and explicitly
  distinguishes those domains from long-lived organizational knowledge,
  policy, and timeline structures.
- `ADR-0017` establishes publication and diagram governance, including
  cross-reference, review, and visual-completeness rules that future
  `ODT` registers and diagrams must follow.
- `ADR-0018` publishes dashboards, widgets, visualizations, and
  artifact specifications that already reference `Organization`,
  `Role`, `Knowledge`, `Expertise`, `Policy`, `Timeline`, `Resource`,
  and `Dependency` as governed object vocabularies.
- `AXI-SCH-007` publishes those object types in the platform-object
  taxonomy, but it does not yet publish canonical schemas for them.
- `Governance/Publications/AXI_Operating_Manual_Architecture.md`
  already names `Organization Intelligence` as a governed operating
  volume, but no milestone-specific governance yet publishes the core
  object schemas or registers that volume depends upon.
- `Governance/Roadmap/AXI_Roadmap_v1.0.md` defines the next planned
  repository phase as `Core Organizational Digital Twin and Knowledge
  Object Schemas`.

Before publication of this ADR, the repository does not publish:

- a milestone-specific governance boundary for Organization
  Intelligence
- canonical schema-boundary rules for the core `ODT` object families
- canonical register requirements for those object families
- authoritative cross-domain rules for how those object families relate
  to the existing decision, readiness, operating-context, regulatory,
  publication, and presentation domains

---

## Architectural Policy

Adopt the following Organization Intelligence and core `ODT` schema
governance baseline.

### 1. Organization Intelligence Domain

Organization Intelligence is a governed architectural domain of AXI.

Its purpose is to normalize the stable organizational structures and
knowledge objects required to make decision support, presentation, and
future engine governance traceable to real organizational conditions.

Organization Intelligence is not a presentation feature, report
family, or runtime shortcut.

It is the schema-and-register layer that makes the Organizational
Digital Twin governable.

### 2. Core ODT Object Families

The first core `ODT` schema baseline shall cover the following object
families:

- `Organization`
- `Person`
- `Role`
- `Knowledge`
- `Expertise`
- `Policy`
- `Timeline`
- `Resource`
- `Dependency`

These are the minimum object families required for phase-7 readiness.

Additional `ODT`-adjacent schema families may be published later, but
they shall not replace or collapse the object families above.

### 3. Boundary Separation

The core `ODT` object families shall remain distinct from the
previously published decision-support domains.

At minimum:

- `OperatingContext` remains time-bound, situational, and planning
  oriented; it does not replace durable organizational structure.
- `RegulatoryKnowledge` remains a separate planning and review domain;
  it does not replace internal `Policy`.
- `ReadinessProfile` remains an evaluative decision-support artifact; it
  does not replace the underlying `Organization`, `Resource`,
  `Timeline`, `Knowledge`, or `Expertise` objects it assesses.
- `Publication`, `Diagram`, `Dashboard`, `Widget`, `Visualization`, and
  `ArtifactSpecification` remain downstream consumers of governed
  object families rather than substitutes for them.

### 4. Object-Family Responsibilities

The core `ODT` object families shall preserve the following minimum
responsibilities:

| Object Family | Unique Responsibility |
| --- | --- |
| `Organization` | Represent the enduring governed identity, mission alignment, structure, and canonical ownership boundary of an organizational entity. |
| `Person` | Represent an individual participant, steward, or stakeholder without collapsing that identity into role or authority. |
| `Role` | Represent responsibility, authority, accountability, and reporting context separate from any specific person. |
| `Knowledge` | Represent durable governed knowledge holdings while preserving knowledge-domain separation defined by `ADR-0014`. |
| `Expertise` | Represent governed capability-in-practice, learned patterns, and approved domain competency that may evolve through lessons and outcomes. |
| `Policy` | Represent binding internal governance, constraints, or rules distinct from regulatory-planning material and from procedures. |
| `Timeline` | Represent governed planned, actual, milestone, and sequencing structures distinct from ambient operating context calendars. |
| `Resource` | Represent allocable organizational assets, capacities, or means required for governed execution. |
| `Dependency` | Represent explicit cross-object reliance, sequencing, or blockage relationships with traceable lineage. |

No core object family may absorb the unique responsibility of another
family without a later approved ADR.

### 5. Register Requirements

The first Organization Intelligence milestone shall publish registers
for the core object families it normalizes.

At minimum, that milestone shall publish:

- one or more governed registers that identify the canonical object set
  published for the phase
- traceability from each register entry to the governing ADRs and
  schemas it operationalizes
- clear distinction between published canonical objects and future
  planned object families

This ADR does not prescribe whether the phase uses one combined
register or multiple family-specific registers.

That choice shall be made by the milestone work item, provided the
result preserves cross-reference integrity and reviewability.

### 6. Cross-Domain Reference Rules

The future core schemas shall preserve explicit support for:

- linkage from `Decision` records to the relevant `Organization`,
  `Role`, `Resource`, `Timeline`, `Policy`, and `Dependency` objects
- linkage from `Knowledge` and `Expertise` objects back to decision,
  lesson, or outcome lineage where applicable
- linkage from presentation artifacts back to their governing core
  object families through the already published presentation-governance
  boundaries
- provenance and lifecycle fields consistent with the repository's
  existing governance model

### 7. Identifier And Numbering Boundary

This ADR authorizes the publication of the core object-family schemas
and registers, but it does not assign their final schema or register
identifiers in advance.

Those identifiers shall be assigned only in the governed milestone that
publishes the corresponding artifacts.

This preserves repository traceability without inventing unpublished
identifier reservations.

### 8. Implementation Boundary

This ADR authorizes:

- milestone-specific schema governance
- milestone-specific register governance
- roadmap and status updates that make the next milestone ready

This ADR does not authorize:

- runtime implementation
- engine implementation
- API, CLI, GUI, or portal implementation
- organization-intelligence services in software
- contracts for unpublished runtime boundaries

---

## Future Guidance

Future governance should proceed in the following order:

1. Publish the milestone work item that operationalizes this ADR.
2. Publish the core schemas and registers for the object families named
   in this ADR.
3. Publish canonical diagrams required to make the new domain visually
   complete.
4. Publish engine-specific ADRs only after the organization-intelligence
   schema baseline exists.
5. Publish decision-runtime or application planning work items only
   after the upstream schema-and-register governance is published.

---

## Non-Goals

This ADR does not approve:

- a monolithic `ODT` mega-schema
- collapsing `Knowledge`, `Expertise`, `Policy`, `Timeline`,
  `Resource`, and `Dependency` into one general-purpose object
- identity, access, or HR-system implementation
- database design
- event processing
- dashboard or visualization implementation

---

## Related

- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/ADR/ADR-0016_Decision_Support_Context_Governance.md`
- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/ADR/ADR-0018_Presentation_Services_Governance.md`
- `Governance/Schemas/AXI-SCH-006_Decisions.json`
- `Governance/Schemas/AXI-SCH-007_Platform_Object.json`
- `Governance/Schemas/AXI-SCH-019_Operating_Context.json`
- `Governance/Schemas/AXI-SCH-020_Regulatory_Knowledge.json`
- `Governance/Schemas/AXI-SCH-021_Readiness_Profile.json`
- `Governance/Roadmap/AXI_Roadmap_v1.0.md`
