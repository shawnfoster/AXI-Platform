# AXI Decision Register

**Version:** 1.0.0
**Status:** Approved
**Authority:** AXI Platform Governance
**Audit Date:** 2026-07-19

---

# Purpose

Publish the canonical governance structure that every AXI decision
record shall follow.

No decision instances are published in this register yet.

This artifact establishes the lifecycle, object topology, and minimum
governance expectations required before future decision records are
implemented.

---

# Canonical Decision Lifecycle

1. Observe
2. Discover
3. Situational Assessment
4. Gather Evidence
5. Assess Context
6. Frame Decision
7. Generate Alternatives
8. Analyze Tradeoffs
9. Evaluate Constraints
10. Evaluate Human Factors
11. Evaluate Capacity
12. Evaluate Calendar
13. Evaluate Ethics
14. Recommend
15. Human Approval
16. Execute
17. Monitor
18. Measure
19. Learn
20. Improve Expertise
21. Update Organizational Digital Twin

Decision records shall preserve explicit traceability across every
completed stage.

---

# Register Entry Structure

Every governed decision record shall preserve at minimum:

- one `decision_id`
- one `mission_id`
- one `decision_context_id`
- one current lifecycle stage
- one accountable owner
- explicit strategic alignment
- operating context references when execution timing is affected
- evidence with provenance
- imported-content review references when evidence is not yet governed
- assumptions with confidence and uncertainty
- alternatives with tradeoff analysis
- regulatory knowledge considerations where potentially applicable
- readiness profile inputs before execution planning
- one recommendation
- explicit human approval state
- governed execution state
- outcomes, observations, and metrics
- lessons, expertise updates, and Organizational Digital Twin updates
- explainability and traceability artifacts

The published structure for these fields is governed by:

- `Governance/Schemas/AXI-SCH-006_Decisions.json`

---

# Canonical Object Topology

The minimum canonical object map for governed decisions is:

| Domain | Canonical Objects | Namespace Guidance |
| --- | --- | --- |
| Decision Core | `Decision`, `DecisionContext`, `Alternative`, `Recommendation`, `Assumption`, `Constraint`, `Risk`, `Opportunity` | Prefer `AXI-DEC` |
| Mission and Organizational Digital Twin | `Mission`, `Organization`, `Person`, `Role`, `Objective`, `Policy`, `Timeline`, `Resource`, `Dependency`, `Capability` | Prefer `AXI-PLT` and `AXI-CAP` |
| Decision Support Context | `OperatingContext`, `RegulatoryKnowledge`, `ReadinessProfile` | Prefer `AXI-PLT` and `AXI-DEC` |
| Evidence and Knowledge | `Evidence`, `Knowledge`, `Expertise`, `Observation`, `Metric` | Prefer `AXI-DEC` for decision-bound evidence and `AXI-PLT` for reusable knowledge and expertise |
| Repository Stewardship and Review | `LifecycleRecord`, `HealthAssessment`, `ArchivePackage`, `ReviewCase` | Prefer `AXI-RVW` and `AXI-PLT` |
| Execution and Learning | `Execution`, `Outcome`, `Lesson` | Prefer `AXI-DEC` |

Future implementation may refine namespace allocations through later
governance, but it shall not bypass this object topology.

---

# Organizational Digital Twin Policy

The Organizational Digital Twin is the governed representation of the
organization's:

- mission
- objectives
- people
- roles
- capabilities
- resources
- dependencies
- timelines
- policies
- knowledge
- expertise
- outcomes
- metrics
- operating context and operational timing

Decision outcomes and lessons shall be capable of updating this domain
through explicit, traceable records rather than implicit side effects.

---

# Knowledge Architecture Policy

The following knowledge domains shall remain logically separate:

- AXI Methodology
- External Knowledge
- Organizational Knowledge
- Regulatory Knowledge
- Learned Knowledge
- Governed Expertise

If content moves across domains, the decision or learning event that
caused the transformation shall remain traceable.

---

# Constitutional Validation Minimums

Every published decision record shall explicitly support:

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

Free-form narrative alone is not sufficient.

---

# Related

- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/ADR/ADR-0016_Decision_Support_Context_Governance.md`
- `Governance/Schemas/AXI-SCH-006_Decisions.json`
- `Governance/Schemas/AXI-SCH-007_Platform_Object.json`
- `Governance/Capabilities/CAPABILITY_REGISTER.md`
