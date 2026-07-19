# AXI Organization Profile Model

**Publication ID:** `PUB-014`
**Publication Type:** `Reference`
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

Publish the constitutional model for how AXI represents an
organization's profile within the Organization Intelligence domain.

This publication defines the governed structure for operational
identity, organizational context, and decision context before any
workflow, onboarding experience, runtime behavior, or recommendation
logic is implemented.

The Organization Profile is not an onboarding wizard.

It is the constitutional representation of what AXI must know about an
organization so future decision analysis can remain evidence-based,
traceable, and reviewable.

---

# Repository Evidence

The repository already publishes the following relevant evidence:

- `ADR-0014` establishes the Organizational Digital Twin as a
  first-class architectural domain and requires durable organizational
  meaning for future decision support.
- `ADR-0015` establishes lifecycle, provenance, and traceability rules
  that profile assertions must preserve.
- `ADR-0016` distinguishes Operating Context, Regulatory Knowledge, and
  Readiness from the durable organizational structures they inform.
- `ADR-0017` governs publication structure, traceability, and diagram
  completeness for new constitutional references.
- `ADR-0019` authorizes Organization Intelligence and the core `ODT`
  schema-and-register baseline for `Organization` and related object
  families.
- `M22` authorizes governance-only advancement of the Organization
  Intelligence and core `ODT` baseline without authorizing runtime
  implementation.
- `PUB-011` publishes the Organization Intelligence architecture
  baseline, while `AXI-SCH-029` and `PUB-012` already publish the first
  `Organization` schema and register baseline.

Before publication of this document, the repository does not publish a
standalone constitutional model that explains how organization-profile
and decision-context inputs belong inside the governed `Organization`
object without becoming advice, readiness scoring, or operating-window
logic.

---

# Constitutional Role

The Organization Profile Model is the governed input surface that
future AXI decision analysis shall use to understand what an
organization is, how it operates, and which durable decision-shaping
conditions must be preserved before alternatives are evaluated.

This model exists to make future reasoning about organizations
reviewable.

It does not authorize any reasoning algorithm, scoring rubric,
recommendation engine, onboarding workflow, or automated approval
behavior.

---

# Model Structure

| Model Area | Constitutional Role | Canonical Elements | `AXI-SCH-029` Operationalization | Explicit Boundary |
| --- | --- | --- | --- | --- |
| Organization Identity | Define the stable organizational identity AXI must treat as canonical. | Name, jurisdiction, industry, organization type, mission, vision, core values, governance maturity, mission alignment, ownership boundary | `name` plus `identity.canonical_name`, `identity.organization_kind`, `identity.jurisdiction`, `identity.industry`, `identity.mission`, `identity.vision`, `identity.core_values`, `identity.governance_maturity`, `identity.mission_alignment`, `identity.ownership_boundary` | Does not replace evidence, decision records, or legal-entity analysis. |
| Organizational Context | Capture the durable business posture surrounding the organization. | Size, stage, revenue model, geographic scope, stakeholders, strategic objectives | `organizational_context.size`, `organizational_context.stage`, `organizational_context.revenue_model`, `organizational_context.geographic_scope`, `organizational_context.stakeholders`, `organizational_context.strategic_objectives` | Does not replace time-bound Operating Context calendars, windows, or live execution telemetry. |
| Decision Context | Preserve organization-level decision inputs that future analysis must consider explicitly. | Legal entity type, entity status, growth objectives, capital strategy, risk tolerance, regulatory environment, reporting requirements | `decision_context.legal_entity_type`, `decision_context.entity_status`, `decision_context.growth_objectives`, `decision_context.capital_strategy`, `decision_context.risk_tolerance`, `decision_context.regulatory_environment`, `decision_context.reporting_requirements`, `decision_context.guidance_boundary` | Does not assert legal, tax, accounting, or compliance conclusions and does not recommend an outcome. |

---

# Decision Context Rules

- `decision_context.entity_status` may be `Existing`, `Planned`, or
  `WILL DECIDE`.
- `WILL DECIDE` is the approved governed value for unresolved entity
  direction when the organization has not yet committed to a structure.
- Regulatory-environment and reporting-requirement profile fields
  identify decision-shaping conditions, not final applicability
  determinations, filing calendars, or expert conclusions.
- The guidance boundary published in `AXI-SCH-029` shall preserve that
  the organization profile does not assert a recommended outcome and
  does not present legal, tax, or accounting advice.

---

# Boundary Rules

- Operating Context remains the authoritative domain for time-bound
  calendars, cycles, freeze windows, and execution timing.
- Regulatory Knowledge remains the authoritative domain for surfaced
  obligations, planning impacts, and review authorities.
- Readiness remains the authoritative domain for evaluative scoring,
  mitigation effects, and proceed/defer judgments.
- The Organization Profile may inform those adjacent domains, but it
  shall not absorb their responsibilities.
- Rendered artifacts such as dashboards, diagrams, and reports remain
  downstream consumers of the profile; they are not the canonical
  organization record.

---

# Future Decision Analysis Support

This model is published so future governed reasoning can evaluate
alternatives across areas such as:

- entity structure
- tax implications
- governance models
- organizational design
- operational maturity
- accounting approaches
- compliance considerations

This publication authorizes only the information architecture required
to support those future evaluations.

It does not publish decision rules, optimization criteria, scenario
logic, legal advice, tax advice, or accounting advice.

---

# Stewardship And Traceability Requirements

- Organization-profile assertions shall remain grounded in evidence,
  approved knowledge, or governed review outcomes.
- Changes to operational identity, organizational context, or decision
  context shall remain traceable to the decision, outcome, lesson,
  review, or evidence event that justifies the change.
- Future registers, publications, and runtime consumers shall treat the
  governed `Organization` object as the authoritative upstream profile
  source.
- Future engine, API, CLI, persistence, or UI work may consume this
  model only through later published governance.

---

# Diagram Relationship

`DGM-008` remains the canonical diagram coverage for this model because
the Organization Profile is a specialization of the already published
Organization Intelligence domain rather than a separate architectural
domain.

No new standalone diagram is required for this publication to remain
constitutionally complete.

---

# Related

- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/ADR/ADR-0016_Decision_Support_Context_Governance.md`
- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/ADR/ADR-0019_Organization_Intelligence_and_Core_ODT_Schema_Governance.md`
- `Governance/WorkQueue/M22-Core-Organizational-Digital-Twin-and-Knowledge-Object-Schemas.md`
- `Governance/Schemas/AXI-SCH-015_Information_Lifecycle_Record.json`
- `Governance/Schemas/AXI-SCH-019_Operating_Context.json`
- `Governance/Schemas/AXI-SCH-020_Regulatory_Knowledge.json`
- `Governance/Schemas/AXI-SCH-021_Readiness_Profile.json`
- `Governance/Schemas/AXI-SCH-029_Organization.json`
- `Governance/Publications/AXI_Organization_Intelligence_Architecture.md`
- `Governance/Publications/AXI_Organization_Register.md`
- `Governance/Publications/Diagrams/DGM-008_Organization_Intelligence_ODT_Foundation_Map.md`
- `Governance/Roadmap/AXI_Roadmap_v1.0.md`
