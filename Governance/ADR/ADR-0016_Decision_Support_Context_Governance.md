# ADR-0016 — Establish Decision Support Context Governance

## Status

Accepted

---

## Purpose

Define the architectural governance required for decisions to account
for real operating conditions, potentially applicable obligations, and
organizational readiness before execution planning begins.

This ADR publishes the governing architecture for:

- Organizational Operating Context
- Regulatory Knowledge
- Multidimensional Readiness

---

## Repository Evidence

The repository already publishes the following relevant evidence:

- `ADR-0014` establishes the Decision as the platform's primary
  governed object and elevates the Organizational Digital Twin to a
  first-class architectural domain.
- `AXI-SCH-006` publishes the current canonical decision record
  structure but does not yet publish explicit structures for operating
  context, regulatory knowledge, or readiness.
- `DECISION_REGISTER` requires decision records to preserve strategic
  alignment, evidence, assumptions, constraints, human factors,
  calendar awareness, and capacity awareness.
- `AXI_Roadmap_v1.0` identifies Organizational Digital Twin and
  knowledge governance as the next architectural phase after the
  decision baseline.

Before publication of this ADR, the repository does not publish:

- an Organizational Operating Context schema
- a Regulatory Knowledge layer separate from organizational knowledge
- a governed readiness model spanning the required dimensions
- explicit decision-schema support for these governed inputs

---

## Architectural Policy

Adopt the following decision-support context governance baseline.

### 1. Organizational Operating Context

The Organizational Digital Twin shall be expanded to include an
Operating Context domain.

The Operating Context domain captures time-bound operational conditions
that materially affect planning, timing, sequencing, approvals, and
execution feasibility.

The canonical Operating Context model shall support, where applicable:

- Fiscal Year
- Fiscal Calendar
- Financial Close
- Budget Cycle
- Strategic Planning Cycle
- Board Calendar
- Audit Windows
- Stub Audit Timing
- Regulatory Reporting Calendar
- Contract Renewal Calendar
- Insurance Renewal
- Payroll Calendar
- Benefits Calendar
- Maintenance Windows
- Technology Freeze Windows
- Major Operational Events

Recommendations shall be evaluated against the relevant Operating
Context before execution planning.

### 2. Operating Context Boundary

Operating Context is not interchangeable with:

- long-lived organizational knowledge
- policy
- readiness
- regulatory knowledge

Operating Context is temporal, situational, and planning-oriented.

It informs:

- execution timing
- approval sequencing
- staging
- freeze-window avoidance
- reporting and audit timing
- resource and calendar conflict detection

### 3. Regulatory Knowledge Layer

AXI shall maintain a Regulatory Knowledge layer separate from
Organizational Knowledge.

The Regulatory Knowledge layer exists to surface potentially applicable
considerations and planning impacts, not to assert legal conclusions.

The approved Regulatory Knowledge domains are:

- `Federal`
- `State`
- `Local`
- `Industry`
- `Professional Standards`
- `Internal Policy`
- `Contractual Requirements`

### 4. Regulatory Knowledge Boundary

Regulatory Knowledge may use organizational characteristics to identify
potential applicability, including:

- geography
- industry
- entity form
- regulated activities
- workforce characteristics
- data characteristics
- contract characteristics

Regulatory Knowledge shall not, by itself:

- declare legal compliance
- declare legal non-compliance
- replace legal review
- replace policy approval

It may:

- identify potentially applicable obligations
- identify review authorities
- identify planning impacts
- identify evidence gaps
- increase uncertainty or escalation requirements

### 5. Readiness Framework

AXI shall use a governed multidimensional readiness model.

The canonical readiness dimensions are:

- Strategic Readiness
- Leadership Readiness
- Capacity Readiness
- Technology Readiness
- Governance Readiness
- Regulatory Readiness
- Financial Readiness
- Change Readiness
- Calendar Readiness
- Knowledge Readiness

Each dimension shall be assessed independently.

Readiness is not binary by default.

### 6. Readiness Influence on Recommendations

Readiness assessments shall influence recommendations in governed ways.

At minimum:

- `Strategic Readiness` influences strategic alignment confidence and
  whether the recommendation should proceed at all.
- `Leadership Readiness` influences approval confidence, sponsorship
  viability, and escalation requirements.
- `Capacity Readiness` influences staffing assumptions, scope, and
  sequencing.
- `Technology Readiness` influences feasibility, dependencies, and
  staging requirements.
- `Governance Readiness` influences whether required controls, owners,
  and evidence exist.
- `Regulatory Readiness` influences whether expert review or additional
  evidence is required before execution.
- `Financial Readiness` influences affordability, budget timing, and
  investment alternatives.
- `Change Readiness` influences adoption risk, rollout strategy, and
  collaboration design.
- `Calendar Readiness` influences execution windows and conflict
  management.
- `Knowledge Readiness` influences uncertainty, required discovery, and
  confidence in recommendation quality.

### 7. Recommendation Effect Vocabulary

The canonical readiness effect outputs are:

- `Proceed`
- `Proceed With Mitigations`
- `Stage Before Execution`
- `Defer`
- `Escalate for Human Review`

Future recommendation logic may refine how these outputs are produced,
but this ADR publishes them as the approved architectural vocabulary.

### 8. Decision Model Integration

Decision records shall be able to reference:

- Operating Context inputs
- Regulatory Knowledge inputs
- Readiness Profiles
- Imported-content review cases when evidence requires governed review

These inputs shall remain explicit rather than being hidden in free-form
notes.

### 9. Constitutional Validation Extension

This ADR extends the decision baseline by requiring future decision
recommendations to preserve explicit support for:

- operating-context awareness
- regulatory-planning awareness
- readiness-based recommendation effects
- escalation when uncertainty or authority gaps remain material

---

## Future Guidance

Future governance may publish:

- organization, role, resource, and timeline schemas that further
  normalize Operating Context inputs
- regulatory source taxonomy refinements
- readiness scoring formulas
- dimension-specific mitigation patterns

Those items are not implementation-approved by this ADR.

---

## Non-Goals

This ADR does not approve:

- legal conclusion engines
- compliance assertion engines
- autonomous readiness approval
- runtime implementation for context, regulatory, or readiness services
- any claim that AXI currently performs these assessments in software

---

## Related

- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/Schemas/AXI-SCH-006_Decisions.json`
- `Governance/Schemas/AXI-SCH-019_Operating_Context.json`
- `Governance/Schemas/AXI-SCH-020_Regulatory_Knowledge.json`
- `Governance/Schemas/AXI-SCH-021_Readiness_Profile.json`
- `Governance/Roadmap/AXI_Roadmap_v1.0.md`
