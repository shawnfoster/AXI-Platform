# AXI Dashboard Register

**Publication ID:** `PUB-007`
**Publication Type:** `Register`
**Version:** `1.0.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Semiannual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Audit Date:** `2026-07-19`
**Related Diagram:** `DGM-007`

---

# Purpose

Publish the canonical dashboard baseline for AXI.

This register defines the approved dashboard lifecycle and the minimum
dashboard types that count as governed decision-intelligence views
within the platform.

Dashboards are not reports.

Dashboards are governed decision surfaces built from canonical platform
objects, governed widgets, governed visualizations, and governed
artifact specifications.

---

# Canonical Dashboard Lifecycle

| Lifecycle Stage | Intent |
| --- | --- |
| `Defined` | The dashboard purpose, audience, governing objects, and validation boundary are approved conceptually. |
| `Templated` | A canonical base template and required widget set are approved for reuse. |
| `Configured` | The dashboard has concrete widget bindings, layout, permissions, and artifact-specification bindings. |
| `Validated` | Accessibility, data-source, permission, traceability, and rendering checks are complete. |
| `Published` | The dashboard is approved for governed use by its intended audience. |
| `Suspended` | The dashboard remains preserved but is temporarily withdrawn pending remediation or review. |
| `Retired` | The dashboard is no longer approved for active use and remains preserved for lineage. |

---

# Canonical Dashboard Types

| Dashboard Type | Purpose | Audience | Governing Objects | Required Widgets | Optional Widgets | Success Metrics |
| --- | --- | --- | --- | --- | --- | --- |
| Executive Dashboard | Give senior leaders a governed view of strategic condition, key risks, and execution posture. | Executive leadership, board-facing sponsors | `Decision`, `Metric`, `Outcome`, `Risk`, `ReadinessProfile`, `OperatingContext` | `WID-001`, `WID-006`, `WID-007`, `WID-016` | `WID-011`, `WID-015`, `WID-018` | Decision latency, strategic objective trend, unresolved critical risks, readiness trend |
| Organization Dashboard | Represent the current state of the organization as a governed operating surface rather than a static profile. | Organization leaders, operating stewards | `Organization`, `Role`, `Capability`, `Resource`, `Dependency`, `OperatingContext` | `WID-013`, `WID-012`, `WID-017`, `WID-018` | `WID-001`, `WID-006`, `WID-015` | Dependency visibility, operating-window conflicts, capability coverage, resource alignment |
| Decision Dashboard | Track decision flow, alternatives, approvals, and execution readiness across the canonical decision lifecycle. | Decision owners, reviewers, approvers | `Decision`, `Alternative`, `Recommendation`, `Constraint`, `Evidence`, `ReadinessProfile` | `WID-004`, `WID-007`, `WID-018`, `WID-016` | `WID-006`, `WID-011`, `WID-017` | Queue aging, approval throughput, evidence completeness, escalation rate |
| Repository Dashboard | Surface repository health, publication quality, lifecycle posture, and stewardship priorities. | Repository stewards, governance operators | `LifecycleRecord`, `HealthAssessment`, `ReviewCase`, `Publication`, `Diagram` | `WID-008`, `WID-009`, `WID-010`, `WID-020` | `WID-001`, `WID-016`, `WID-018` | Health-band movement, placeholder reduction, reference integrity, review backlog |
| Governance Dashboard | Provide a control view of policy coverage, exceptions, approvals, and governance compliance. | Governance stewards, approvers | `Policy`, `Capability`, `Decision`, `ReviewCase`, `Publication`, `Diagram` | `WID-008`, `WID-004`, `WID-006`, `WID-016` | `WID-001`, `WID-018`, `WID-020` | Exception volume, approval cycle time, control coverage, unresolved policy gaps |
| Knowledge Dashboard | Surface knowledge coverage, publication reuse, lessons, and expertise improvement patterns. | Knowledge stewards, domain owners | `Knowledge`, `Expertise`, `Lesson`, `Publication`, `Decision` | `WID-010`, `WID-019`, `WID-016` | `WID-001`, `WID-002`, `WID-018` | Canonical coverage, reuse rate, lesson adoption, expertise refresh cadence |
| Operational Dashboard | Monitor current operations, execution windows, work status, and timing conflicts. | Operations leaders, program operators | `OperatingContext`, `Timeline`, `Resource`, `Execution`, `Outcome` | `WID-003`, `WID-017`, `WID-018`, `WID-005` | `WID-001`, `WID-006`, `WID-011` | Operational throughput, blocked work, timing conflicts, execution variance |
| Risk Dashboard | Present current risk concentrations, dependencies, exposures, and escalations in governed form. | Risk owners, executives, reviewers | `Risk`, `Dependency`, `Policy`, `RegulatoryKnowledge`, `ReviewCase` | `WID-006`, `WID-012`, `WID-018`, `WID-016` | `WID-001`, `WID-011`, `WID-015` | Risk concentration, unresolved high-severity items, dependency exposure, escalation response time |
| Readiness Dashboard | Show multidimensional readiness posture and its effect on recommendations and execution planning. | Sponsors, project leads, approvers | `ReadinessProfile`, `OperatingContext`, `Resource`, `Timeline`, `Risk` | `WID-007`, `WID-017`, `WID-003`, `WID-018` | `WID-006`, `WID-016`, `WID-001` | Dimension readiness movement, mitigation completion, deferment rate, execution-blocker count |
| Project Dashboard | Track project status, sequence, dependencies, and execution health. | Project managers, sponsors | `Objective`, `Timeline`, `Resource`, `Dependency`, `Risk`, `Execution` | `WID-003`, `WID-011`, `WID-018`, `WID-005` | `WID-006`, `WID-007`, `WID-016` | Schedule variance, dependency blockers, action aging, risk trend |
| Portfolio Dashboard | Compare project and initiative performance across a governed strategic portfolio. | Portfolio leaders, executives | `Objective`, `Metric`, `Resource`, `Dependency`, `Outcome` | `WID-011`, `WID-014`, `WID-001`, `WID-018` | `WID-006`, `WID-016`, `WID-015` | Portfolio balance, outcome variance, resource concentration, dependency bottlenecks |
| Learning Dashboard | Track lessons, knowledge growth, expertise updates, and adoption of improved practices. | Knowledge leaders, training owners | `Lesson`, `Expertise`, `Knowledge`, `Outcome`, `Metric` | `WID-019`, `WID-010`, `WID-001` | `WID-002`, `WID-016`, `WID-018` | Lesson conversion rate, expertise adoption, stale-knowledge reduction, training completion |
| Administration Dashboard | Provide governed administration visibility for publication stewardship, access posture, and operational controls. | Platform administrators, stewards | `Publication`, `Diagram`, `LifecycleRecord`, `HealthAssessment`, `ReviewCase`, `Capability` | `WID-020`, `WID-008`, `WID-003`, `WID-018` | `WID-001`, `WID-009`, `WID-016` | Admin backlog, unresolved control issues, review-cycle compliance, permission exception count |

---

# Inheritance And Customization Rules

- Canonical dashboard templates define the default widget contract,
  validation boundary, and artifact-specification binding for a
  dashboard type.
- Organization-specific dashboards may inherit from a canonical parent
  through layout, branding, or widget-configuration overlays.
- Overlays may not change the dashboard's governing objects, permission
  inheritance, or validation rules.
- Dashboard cloning creates a new governed child dashboard that must
  preserve lineage back to its approved parent template.

---

# Related

- `Governance/ADR/ADR-0018_Presentation_Services_Governance.md`
- `Governance/Schemas/AXI-SCH-024_Dashboard.json`
- `Governance/Schemas/AXI-SCH-025_Widget.json`
- `Governance/Schemas/AXI-SCH-027_Artifact_Specification.json`
- `Governance/Schemas/AXI-SCH-028_Visualization.json`
- `Governance/Publications/AXI_Widget_Register.md`
- `Governance/Publications/AXI_Artifact_Specification_Baseline.md`
- `Governance/Publications/Diagrams/DGM-007_Presentation_Services_Topology.md`
