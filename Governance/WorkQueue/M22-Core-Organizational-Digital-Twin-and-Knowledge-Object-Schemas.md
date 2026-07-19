# WQ-013 — Core Organizational Digital Twin And Knowledge Object Schemas

**Work Item:** M22
**Title:** Core Organizational Digital Twin And Knowledge Object Schemas
**Status:** Approved
**Priority:** High
**Owner:** AXI Platform

---

# Objective

Publish the first governed schema-and-register baseline for the core
Organizational Digital Twin (`ODT`) and Organization Intelligence
object families.

This milestone is governance-only.

It does not authorize runtime implementation.

---

# Background

The repository now publishes:

- runtime implementation through `M18 Runtime API`
- decision, stewardship, context, publication, and presentation
  governance through `ADR-0014` through `ADR-0018`
- the presentation-services governance milestone through `M21`

The repository roadmap now identifies the next planned phase as:

- `Core Organizational Digital Twin and Knowledge Object Schemas`

Published repository evidence already requires these schemas:

- `ADR-0014` names `Organization`, `Person`, `Role`, `Knowledge`,
  `Expertise`, `Policy`, `Timeline`, `Resource`, and `Dependency` as
  canonical platform objects.
- `ADR-0016` distinguishes `OperatingContext`, `RegulatoryKnowledge`,
  and `ReadinessProfile` from the durable organization-domain objects
  they inform.
- `ADR-0018` already publishes dashboards and widgets that reference
  several of these object families as governed consumers.

Before this work item, the repository publishes those object types in
vocabulary only.

It does not yet publish their canonical schemas or registers.

This work-item numbering follows the current published work-queue
sequence after `M21`.

It does not attempt to resolve the historical numbering drift recorded
in `Governance/DependencyMatrix.md`.

---

# Existing Components

Reuse published architecture and runtime foundations only.

Relevant upstream evidence includes:

- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/ADR/ADR-0016_Decision_Support_Context_Governance.md`
- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/ADR/ADR-0018_Presentation_Services_Governance.md`
- `Governance/ADR/ADR-0019_Organization_Intelligence_and_Core_ODT_Schema_Governance.md`
- `Governance/Schemas/AXI-SCH-006_Decisions.json`
- `Governance/Schemas/AXI-SCH-007_Platform_Object.json`
- `Governance/Schemas/AXI-SCH-019_Operating_Context.json`
- `Governance/Schemas/AXI-SCH-020_Regulatory_Knowledge.json`
- `Governance/Schemas/AXI-SCH-021_Readiness_Profile.json`
- `Governance/Publications/AXI_Operating_Manual_Architecture.md`
- `Runtime/ObjectModel/`
- `Runtime/Registry/`
- `Runtime/ObjectRegistry/`
- `Runtime/CapabilityRegistry/`
- `Runtime/ServiceRegistry/`
- `Runtime/Validation/`

No new runtime subsystem may be introduced in this milestone.

---

# Scope

Publish governed schema and register artifacts for the first core
Organization Intelligence baseline in:

```text
Governance/Schemas/
Governance/Publications/
Governance/ADR/
Governance/Roadmap/
Governance/WorkQueue/
```

Expected outputs include:

- canonical schemas for the core object families authorized by
  `ADR-0019`
- one or more canonical registers for those object families
- a canonical diagram if required to claim the domain visually complete
- repository status updates required to keep readiness evidence
  consistent

This milestone shall not modify:

- `Runtime/`
- `Core/`
- `Tests/`

except for validation-only adjustments if they become strictly
necessary.

---

# Functional Requirements

This milestone shall:

- publish canonical schemas for `Organization`, `Person`, `Role`,
  `Knowledge`, `Expertise`, `Policy`, `Timeline`, `Resource`, and
  `Dependency`
- preserve the knowledge-domain separation published by `ADR-0014`
- preserve the boundary separation between durable organization-domain
  objects and the already published `OperatingContext`,
  `RegulatoryKnowledge`, and `ReadinessProfile` domains
- publish one or more registers that identify the canonical object set
  produced by the milestone
- preserve cross-reference integrity to governing ADRs, published
  schemas, and future downstream consumers
- preserve provenance, lifecycle, ownership, and versioning semantics
  consistent with published repository governance

---

# Dependencies

`M22` depends on the following published repository evidence:

- roadmap phase 6 completion in
  `Governance/Roadmap/AXI_Roadmap_v1.0.md`
- `ADR-0014`
- `ADR-0015`
- `ADR-0016`
- `ADR-0017`
- `ADR-0018`
- `ADR-0019`
- `AXI-SCH-006`
- `AXI-SCH-007`
- `AXI-SCH-019`
- `AXI-SCH-020`
- `AXI-SCH-021`
- `M21`

No contract publication is required before beginning this governance
milestone because it does not authorize runtime interfaces.

---

# Dependency Audit

Record the dependency audit for this milestone.

- Produces:
  Core Organization Intelligence schemas and registers for the first
  `ODT` schema baseline.
- Published governance prerequisites:
  `ADR-0014` through `ADR-0019`, `AXI-SCH-006`, `AXI-SCH-007`,
  `AXI-SCH-019` through `AXI-SCH-021`, and the post-`M18` decision
  roadmap.
- Required implemented runtime modules:
  None beyond the current reusable runtime foundation already
  implemented through `M18`.
- Downstream consumers:
  engine-specific governance by layer, decision runtime and application
  planning, and future governed presentation consumers that already
  reference these object families.
- Repository readiness gate:
  phase 6 is complete, `M21` is complete, this work item is published,
  and `ADR-0019` is approved.

Readiness may not rely on placeholder files, intended future work, or
unpublished schema identifiers.

---

# Constraints

Implementation shall:

- preserve architecture
- preserve schemas
- preserve standards
- preserve provenance
- preserve traceability
- preserve reproducibility

Architecture changes require an approved ADR.

This milestone shall not claim:

- runtime code
- GUI code
- dashboards in software
- services in software
- API contracts for unpublished runtime boundaries

---

# Validation

The milestone shall reject governance that:

- collapses multiple core object families into one undifferentiated
  schema
- merges `OperatingContext`, `RegulatoryKnowledge`, or
  `ReadinessProfile` into the durable `ODT` objects
- publishes registers without clear traceability to the governing ADRs
  and schemas
- claims visual completeness for the new domain without publishing the
  required diagram evidence

---

# Deliverables

Expected outputs:

- core `ODT` schema artifacts
- Organization Intelligence register artifacts
- required roadmap and status updates
- a canonical diagram if needed for visual completeness

---

# Acceptance Criteria

Implementation is complete when:

✓ The repository publishes canonical schemas for the core object
families named by `ADR-0019`

✓ The repository publishes one or more governed registers for those
object families

✓ Cross-domain boundaries remain aligned with `ADR-0014`,
`ADR-0016`, and `ADR-0018`

✓ No runtime implementation is claimed

✓ Repository status artifacts remain consistent with the published
governance state

---

# Definition of Done

Before completion:

- run the validation required by the selected tier
- preserve governance
- preserve schemas
- preserve traceability
- preserve provenance
- produce one logical Git commit

Stop after completion.

---

# Suggested Commit Message

AI-XXX: publish core ODT schema baseline
