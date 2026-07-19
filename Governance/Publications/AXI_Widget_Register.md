# AXI Widget Register

**Publication ID:** `PUB-008`
**Publication Type:** `Register`
**Version:** `1.0.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Semiannual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Audit Date:** `2026-07-19`

---

# Purpose

Publish the canonical widget baseline for AXI.

Widgets are governed reusable presentation objects with stable meaning,
security expectations, layout support, and data-source traceability.

---

# Supported Layout Vocabulary

The canonical widget layout vocabulary is:

- `Hero`
- `Full Width`
- `Half Width`
- `Third Width`
- `Quarter Width`
- `Sidebar`
- `Mobile Stack`

---

# Canonical Widget Register

| Widget ID | Version | Purpose | Visualization Type | Governed Data Source | Refresh Policy | Security | Dependencies | Supported Layouts | Accessibility | Related Schemas | Related ADRs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `WID-001` | `1.0.0` | Surface a single accountable measure with threshold context. | KPI Card | `Decision`, `Metric`, `Outcome` | Daily | Masked aggregate when required | Metric definitions, threshold policy | Hero, Quarter Width, Mobile Stack | Keyboard, text summary, color-independent status | `AXI-SCH-006`, `AXI-SCH-025`, `AXI-SCH-028` | `ADR-0014`, `ADR-0018` |
| `WID-002` | `1.0.0` | Show governed trend movement over time. | Line Chart | `Metric`, `Outcome`, `ReadinessProfile` | Daily | Aggregate only | Time-series baseline | Full Width, Half Width, Mobile Stack | Keyboard, axis summary, pattern differentiation | `AXI-SCH-021`, `AXI-SCH-025`, `AXI-SCH-028` | `ADR-0016`, `ADR-0018` |
| `WID-003` | `1.0.0` | Summarize operational or project status across accountable objects. | Scorecard | `Execution`, `Outcome`, `Objective` | Daily | Object-scoped | Status vocabulary, ownership mapping | Full Width, Half Width, Quarter Width | Keyboard, text alternative, color-independent state | `AXI-SCH-025`, `AXI-SCH-028` | `ADR-0014`, `ADR-0018` |
| `WID-004` | `1.0.0` | Present pending decisions, approvals, and escalations in auditable form. | Table | `Decision`, `Recommendation`, `ReviewCase` | Event-Driven | Row-level security | Approval-state mapping | Full Width, Half Width, Sidebar, Mobile Stack | Keyboard, column summaries, sort announcements | `AXI-SCH-006`, `AXI-SCH-018`, `AXI-SCH-025` | `ADR-0015`, `ADR-0018` |
| `WID-005` | `1.0.0` | Track next actions, handoffs, and execution follow-up. | Table | `Execution`, `Outcome`, `Timeline` | Event-Driven | Row-level security | Execution handoff lineage | Full Width, Half Width, Sidebar, Mobile Stack | Keyboard, activity summary, focus order | `AXI-SCH-025`, `AXI-SCH-028` | `ADR-0014`, `ADR-0018` |
| `WID-006` | `1.0.0` | Show concentration and severity of governed risk or control exposure. | Heatmap | `Risk`, `ReadinessProfile`, `ReviewCase` | Daily | Aggregate with masked detail | Severity and band definitions | Full Width, Half Width | Keyboard, numeric alternative, pattern encoding | `AXI-SCH-018`, `AXI-SCH-021`, `AXI-SCH-025`, `AXI-SCH-028` | `ADR-0015`, `ADR-0016`, `ADR-0018` |
| `WID-007` | `1.0.0` | Present multidimensional readiness and its recommendation effect. | Scorecard | `ReadinessProfile`, `OperatingContext` | Daily | Object-scoped | Readiness dimensions, effect vocabulary | Hero, Full Width, Half Width | Keyboard, text equivalent, dimension labels | `AXI-SCH-019`, `AXI-SCH-021`, `AXI-SCH-025`, `AXI-SCH-028` | `ADR-0016`, `ADR-0018` |
| `WID-008` | `1.0.0` | Track governance, publication, and policy compliance at the control level. | Table | `Publication`, `Diagram`, `ReviewCase`, `Capability` | Daily | Restricted detail | Review-cycle rules, control mapping | Full Width, Half Width | Keyboard, table summary, accessible sorting | `AXI-SCH-022`, `AXI-SCH-023`, `AXI-SCH-025` | `ADR-0017`, `ADR-0018` |
| `WID-009` | `1.0.0` | Surface repository health with governed dimension-level evidence. | Table | `HealthAssessment`, `LifecycleRecord` | Weekly | Aggregate only | Health dimensions, lifecycle mapping | Full Width, Half Width | Keyboard, screen-reader row summaries | `AXI-SCH-015`, `AXI-SCH-016`, `AXI-SCH-025` | `ADR-0015`, `ADR-0018` |
| `WID-010` | `1.0.0` | Show knowledge or publication coverage gaps against canonical domains. | Heatmap | `Knowledge`, `Publication`, `Lesson`, `Capability` | Weekly | Aggregate only | Coverage-domain taxonomy | Full Width, Half Width | Keyboard, numeric matrix alternative, pattern encoding | `AXI-SCH-022`, `AXI-SCH-025`, `AXI-SCH-028` | `ADR-0014`, `ADR-0017`, `ADR-0018` |
| `WID-011` | `1.0.0` | Display milestones, sequencing, and portfolio timing in governed order. | Timeline | `Timeline`, `Objective`, `Execution` | Daily | Object-scoped | Calendar and dependency lineage | Full Width, Hero, Mobile Stack | Keyboard, event list, focusable milestone details | `AXI-SCH-025`, `AXI-SCH-028` | `ADR-0014`, `ADR-0018` |
| `WID-012` | `1.0.0` | Visualize dependency structure across governed objects. | Dependency Graph | `Dependency`, `Resource`, `Execution`, `Risk` | Daily | Aggregate with gated drillback | Node and edge lineage | Full Width, Hero | Keyboard, text graph summary, non-color encoding | `AXI-SCH-025`, `AXI-SCH-028` | `ADR-0014`, `ADR-0018` |
| `WID-013` | `1.0.0` | Provide a concise organization state summary tied to governed objects. | Executive Summary | `Organization`, `Role`, `Capability`, `OperatingContext` | Daily | Object-scoped | Organization profile lineage | Hero, Full Width, Mobile Stack | Keyboard, text-first narrative, structured headings | `AXI-SCH-019`, `AXI-SCH-025`, `AXI-SCH-028` | `ADR-0016`, `ADR-0018` |
| `WID-014` | `1.0.0` | Show governed flow between work, resources, or outcomes. | Sankey Diagram | `Resource`, `Objective`, `Outcome`, `Dependency` | Weekly | Aggregate only | Flow-balance rules | Full Width, Hero | Keyboard, flow summary, node labeling | `AXI-SCH-025`, `AXI-SCH-028` | `ADR-0014`, `ADR-0018` |
| `WID-015` | `1.0.0` | Show spatially relevant governed context or exposure. | Geographic Map | `OperatingContext`, `RegulatoryKnowledge`, `Risk` | Weekly | Region-scoped | Approved geographic hierarchy | Full Width, Half Width | Keyboard, text region summary, non-map alternative | `AXI-SCH-019`, `AXI-SCH-020`, `AXI-SCH-025`, `AXI-SCH-028` | `ADR-0016`, `ADR-0018` |
| `WID-016` | `1.0.0` | Provide governed narrative interpretation for executive consumption. | Executive Summary | `Decision`, `Risk`, `ReadinessProfile`, `Publication` | Daily | Audience-scoped | Source-widget lineage, explanation boundary | Hero, Full Width, Mobile Stack | Keyboard, heading structure, source references | `AXI-SCH-006`, `AXI-SCH-021`, `AXI-SCH-022`, `AXI-SCH-025`, `AXI-SCH-028` | `ADR-0014`, `ADR-0017`, `ADR-0018` |
| `WID-017` | `1.0.0` | Surface operating windows, freezes, renewals, and calendar conflicts. | Calendar View | `OperatingContext`, `Timeline` | Daily | Object-scoped | Calendar precedence rules | Full Width, Half Width, Mobile Stack | Keyboard, event list, date summaries | `AXI-SCH-019`, `AXI-SCH-025` | `ADR-0016`, `ADR-0018` |
| `WID-018` | `1.0.0` | Present governed detailed measures or records in auditable tabular form. | Table | `Metric`, `Outcome`, `Decision`, `Capability` | Daily | Row-level security when required | Column-definition lineage | Full Width, Half Width, Sidebar, Mobile Stack | Keyboard, caption, column summaries | `AXI-SCH-006`, `AXI-SCH-025`, `AXI-SCH-028` | `ADR-0014`, `ADR-0018` |
| `WID-019` | `1.0.0` | Track lesson adoption and expertise-improvement progression. | Bar Chart | `Lesson`, `Expertise`, `Knowledge`, `Outcome` | Weekly | Aggregate only | Expertise lifecycle mapping | Full Width, Half Width | Keyboard, bar-value summary, pattern encoding | `AXI-SCH-025`, `AXI-SCH-028` | `ADR-0014`, `ADR-0018` |
| `WID-020` | `1.0.0` | Surface administrative workload, publication stewardship, and review cadence. | Table | `Publication`, `Diagram`, `LifecycleRecord`, `ReviewCase` | Daily | Restricted detail | Stewardship workflow lineage | Full Width, Half Width, Sidebar | Keyboard, row summaries, accessible sorting | `AXI-SCH-015`, `AXI-SCH-018`, `AXI-SCH-022`, `AXI-SCH-023`, `AXI-SCH-025` | `ADR-0015`, `ADR-0017`, `ADR-0018` |

---

# Approved Visualization Families

| Visualization Family | Approved Use | Prohibited Use | Governing Data Expectations |
| --- | --- | --- | --- |
| KPI Card | Single accountable measure with explicit threshold and owner. | Multi-step narrative or unsupported causal claims. | Governed metric definition, refresh cadence, and threshold vocabulary required. |
| Table | Auditable queues, detail, comparisons, and stewardship worklists. | Hiding unresolved semantics in unlabeled columns. | Column lineage, sort meaning, and access controls required. |
| Timeline | Sequencing, milestones, windows, renewals, and operational cadence. | Dense quantitative ranking or dependency inference without governance. | Ordered dates, event ownership, and calendar rules required. |
| Heatmap | Relative concentrations of risk, readiness, compliance, or coverage. | Exact-value presentation without accessible numeric alternative. | Banding rules, intensity legend, and text equivalent required. |
| Decision Tree | Explicit branching logic for decision or governance pathways. | Free-form process illustration with hidden criteria. | Branch criteria, exit conditions, and authoritative labels required. |
| Sankey Diagram | Governed flow of work, resources, or outcomes between accountable nodes. | Circular-state modeling or unsupported transformation claims. | Node/edge lineage, flow totals, and aggregation policy required. |
| Organizational Chart | Formal accountability, approval, or stewardship relationships. | Social or influence mapping without explicit governance approval. | Role lineage and hierarchy authority required. |
| Dependency Graph | Cross-object relationships and blocker structure. | Unfounded causal inference or implied sequencing without lineage. | Node/edge traceability and dependency meaning required. |
| Digital Twin Visualization | Governed state overlays across organizational structure or operating posture. | Raw transaction reporting or unsupported simulation claims. | Source-object lineage and state timestamp required. |
| Geographic Map | Spatial operating context, regional exposure, or geography-bound obligations. | Non-spatial ranking or symbolic decoration. | Approved geographic hierarchy and text alternative required. |
| Scorecard | Multi-measure status or readiness comparison against a fixed frame. | Deep causal analysis or narrative substitution. | Fixed measure set, scoring basis, and thresholds required. |
| Executive Summary | Governed narrative interpretation anchored to source widgets and objects. | Unsupported opinion, free-form branding copy, or hidden rationale. | Source references, explanation boundary, and audience scope required. |

---

# Related

- `Governance/ADR/ADR-0018_Presentation_Services_Governance.md`
- `Governance/Schemas/AXI-SCH-025_Widget.json`
- `Governance/Schemas/AXI-SCH-028_Visualization.json`
- `Governance/Publications/AXI_Dashboard_Register.md`
