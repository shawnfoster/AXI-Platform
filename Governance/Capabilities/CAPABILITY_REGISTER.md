# AXI Capability Register

**Version:** 1.3.0
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

| Capability ID | Name | Primary Coverage | Purpose |
| --- | --- | --- | --- |
| `CAP-001` | Observation and Discovery | Observe, Discover, Situational Assessment | Detect signals, events, metrics, and anomalies that may require governed decisions. |
| `CAP-002` | Evidence and Provenance Management | Gather Evidence | Collect evidence with source references, provenance, and confidence context. |
| `CAP-003` | Decision and Operating Context Assembly | Assess Context | Assemble mission, organization, operating context, role, resource, dependency, timeline, and policy context for decisions. |
| `CAP-004` | Assumption, Constraint, and Regulatory Governance | Evaluate Constraints, Evaluate Capacity, Evaluate Calendar, Evaluate Ethics | Keep assumptions explicit, surface potentially applicable regulatory considerations, and apply binding governance limits. |
| `CAP-005` | Alternative and Scenario Generation | Frame Decision, Generate Alternatives | Produce distinct alternatives and plausible future scenarios. |
| `CAP-006` | Forecast, Simulation, and Tradeoff Analysis | Analyze Tradeoffs | Estimate outcomes, test scenarios, and analyze tradeoffs across alternatives. |
| `CAP-007` | Recommendation and Explainability | Recommend | Produce recommendations with rationale, traceability, and alternative analysis. |
| `CAP-008` | Human Factors and Collaborative Approval | Evaluate Human Factors, Human Approval | Preserve human accountability and collaborative review before execution. |
| `CAP-009` | Governed Execution and Measurement | Execute, Monitor, Measure | Coordinate approved execution and record monitored outcomes and metrics. |
| `CAP-010` | Learning, Expertise Improvement, and Digital Twin Update | Learn, Improve Expertise, Update Organizational Digital Twin | Convert outcomes into lessons, governed expertise, and Organizational Digital Twin updates. |
| `CAP-011` | Information Lifecycle Governance | Repository Stewardship | Govern Active, Review, Deprecated, Archive Candidate, Archived, Historical, and Eligible for Disposal transitions with traceability. |
| `CAP-012` | Repository Health Assessment | Repository Stewardship | Measure repository health through governed dimensions including quality, entropy, duplicate risk, provenance, integrity, compliance, placeholders, canonical coverage, documentation waste, and import readiness. |
| `CAP-013` | Archive and Restoration Governance | Repository Stewardship | Preserve governed history through archive packages, manifests, snapshots, dependency preservation, provenance preservation, and restoration requirements. |
| `CAP-014` | Imported Content Review and Quarantine | Repository Stewardship | Review imported content through explicit workflow status, risk classification, severity, review authority, quarantine, and governed release boundaries. |
| `CAP-015` | Operating Context Assessment | Assess Context, Evaluate Calendar, Execute | Evaluate decisions against fiscal, board, audit, reporting, maintenance, freeze, renewal, payroll, and other operational timing conditions before execution planning. |
| `CAP-016` | Regulatory Knowledge Surfacing | Assess Context, Evaluate Ethics, Recommend | Surface potentially applicable federal, state, local, industry, professional, internal, and contractual considerations without asserting legal conclusions. |
| `CAP-017` | Multidimensional Readiness Assessment | Recommend, Human Approval, Execute | Assess strategic, leadership, capacity, technology, governance, regulatory, financial, change, calendar, and knowledge readiness and translate the result into governed recommendation effects. |
| `CAP-018` | Publication and Diagram Governance | Repository Stewardship | Govern publication hierarchy, manual architecture, cross-reference integrity, diagram lifecycle, and synchronized visual authority so AXI documentation remains an authoritative platform subsystem. |
| `CAP-019` | Dashboard And Decision Surface Governance | Recommend, Human Approval, Execute, Monitor, Measure | Govern dashboard composition, lifecycle, permissions, inheritance, customization, and validation while ensuring dashboards consume governed platform objects rather than owning business data. |
| `CAP-020` | Design System And Brand Governance | Repository Stewardship, Recommend, Human Approval, Execute | Govern brand kits, themes, typography, color, iconography, layout grids, accessibility, export styles, and white-label overlays across all rendered AXI artifacts. |
| `CAP-021` | Visualization And Insight Communication | Observe, Discover, Situational Assessment, Recommend, Measure | Govern approved visualization families, interpretability rules, executive-summary patterns, and governed visualization-to-data-source traceability. |
| `CAP-022` | Artifact Specification And Export Governance | Repository Stewardship, Human Approval, Execute | Govern canonical rendering requirements, responsive variants, export formats, safe areas, typography scale, icon sizes, and accessibility across dashboards, documents, diagrams, reports, and presentations. |
| `CAP-023` | Information Governance And Knowledge Protection | Repository Stewardship, Assess Context, Human Approval | Govern protected-knowledge metadata, classification frameworks, access and sharing posture, retention posture, licensing, privacy, jurisdiction, audit requirements, and downstream protection inheritance for canonical `Knowledge` objects without authorizing cybersecurity implementation. |

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
- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/ADR/ADR-0016_Decision_Support_Context_Governance.md`
- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/ADR/ADR-0018_Presentation_Services_Governance.md`
- `Governance/ADR/ADR-0023_Information_Governance_and_Knowledge_Protection_Governance.md`
- `Governance/Decisions/DECISION_REGISTER.md`
- `Governance/Schemas/AXI-SCH-006_Decisions.json`
- `Governance/Schemas/AXI-SCH-008_Capability.json`
- `Governance/Schemas/AXI-SCH-031_Information_Governance_Profile.json`
- `Governance/Publications/AXI_Information_Governance_and_Knowledge_Protection_Model.md`
