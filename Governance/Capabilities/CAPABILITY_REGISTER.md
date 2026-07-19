# AXI Capability Register

**Version:** 1.0.0
**Status:** Approved
**Authority:** AXI Platform Governance
**Audit Date:** 2026-07-19

---

# Purpose

Publish the current governed capability map for AXI as a Decision
Intelligence Platform.

This register defines the stable capabilities that future engines,
services, applications, and decision workflows shall trace to.

---

# Published Capabilities

| Capability ID | Name | Primary Lifecycle Coverage | Purpose |
| --- | --- | --- | --- |
| `CAP-001` | Observation and Discovery | Observe, Discover, Situational Assessment | Detect signals, events, metrics, and anomalies that may require governed decisions. |
| `CAP-002` | Evidence and Provenance Management | Gather Evidence | Collect evidence with source references, provenance, and confidence context. |
| `CAP-003` | Decision Context Assembly | Assess Context | Assemble mission, organization, role, resource, dependency, timeline, and policy context for decisions. |
| `CAP-004` | Assumption and Constraint Governance | Evaluate Constraints, Evaluate Capacity, Evaluate Calendar, Evaluate Ethics | Keep assumptions explicit and apply binding governance limits. |
| `CAP-005` | Alternative and Scenario Generation | Frame Decision, Generate Alternatives | Produce distinct alternatives and plausible future scenarios. |
| `CAP-006` | Forecast, Simulation, and Tradeoff Analysis | Analyze Tradeoffs | Estimate outcomes, test scenarios, and analyze tradeoffs across alternatives. |
| `CAP-007` | Recommendation and Explainability | Recommend | Produce recommendations with rationale, traceability, and alternative analysis. |
| `CAP-008` | Human Factors and Collaborative Approval | Evaluate Human Factors, Human Approval | Preserve human accountability and collaborative review before execution. |
| `CAP-009` | Governed Execution and Measurement | Execute, Monitor, Measure | Coordinate approved execution and record monitored outcomes and metrics. |
| `CAP-010` | Learning, Expertise Improvement, and Digital Twin Update | Learn, Improve Expertise, Update Organizational Digital Twin | Convert outcomes into lessons, governed expertise, and Organizational Digital Twin updates. |

---

# Engine Review

The following engine set is the current approved architectural engine
map. These entries govern architectural responsibility only and do not
claim runtime implementation.

| Engine | Primary Layer | Unique Responsibility | Overlap Boundary | Governance Status |
| --- | --- | --- | --- | --- |
| Situational Intelligence | Intelligence | Convert observations, metrics, and signals into a governed situational assessment. | Does not own stable organizational context or policy constraints. | Approved candidate |
| Context | Intelligence | Assemble decision context from mission, organization, roles, policies, resources, dependencies, and timelines. | Does not produce recommendations or replace evidence gathering. | Approved candidate |
| Behavioral Intelligence | Intelligence | Model stakeholder behavior, incentives, and adoption risk. | Does not coordinate approval workflow. | Approved candidate |
| Assumption | Reasoning | Make assumptions explicit and track confidence, uncertainty, and invalidation. | Does not replace constraints or approval. | Approved candidate |
| Scenario | Reasoning | Generate plausible alternatives and futures. | Does not forecast or optimize them. | Approved candidate |
| Forecast | Reasoning | Estimate likely outcome trajectories for alternatives. | Does not simulate dynamic interactions or select winners. | Approved candidate |
| Simulation | Reasoning | Stress-test alternatives and execution plans against Organizational Digital Twin state. | Does not own baseline forecasting or collaboration workflow. | Approved candidate |
| Optimization | Reasoning | Rank alternatives against objectives, tradeoffs, and limits. | Does not replace human approval. | Approved candidate |
| Collaboration | Execution | Coordinate human approval, assignments, execution handoffs, and feedback loops. | Does not score trust, ethics, or optimize alternatives. | Approved candidate |
| Constraint | Governance | Apply policy, resource, dependency, calendar, and ethics limits as binding governance checks. | Does not generate alternatives or forecasts. | Approved candidate |
| Explanation | Governance | Produce rationale, provenance chains, and traceability artifacts. | Does not calculate trustworthiness or manage approval workflow. | Approved candidate |
| Trust | Governance | Evaluate provenance completeness, confidence, uncertainty, and integrity. | Does not replace explanation or policy constraints. | Approved candidate |
| Expertise Lifecycle | Governance | Convert outcomes and lessons into governed expertise and Organizational Digital Twin updates. | Does not collect raw evidence or execute decisions directly. | Approved candidate |

---

# Architectural Controls

- No additional engine domain is approved unless a future ADR proves a
  unique responsibility not covered by the current engine map.
- No current engine may expand into an undifferentiated "do everything"
  decision engine.
- The Organizational Digital Twin remains a first-class domain, not an
  additional engine. Multiple approved engines may read from or update
  it through governed boundaries.
- Capabilities remain stable even when later runtime implementations,
  engine packages, or applications change.

---

# Related

- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/Decisions/DECISION_REGISTER.md`
- `Governance/Schemas/AXI-SCH-006_Decisions.json`
- `Governance/Schemas/AXI-SCH-008_Capability.json`
