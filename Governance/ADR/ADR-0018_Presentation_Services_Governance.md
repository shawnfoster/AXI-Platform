# ADR-0018 — Establish Presentation Services Governance

## Status

Accepted

---

## Purpose

Define the architectural governance required to treat dashboards,
design systems, visualizations, and rendered artifacts as governed AXI
services rather than user-interface details.

This ADR publishes the governing architecture for:

- Dashboard Service (`DAS`)
- Design System Service (`DSS`)
- Visualization Service (`VS`)
- governed widget architecture
- governed artifact specifications

---

## Repository Evidence

The repository already publishes the following relevant evidence:

- `ADR-0014` establishes the Decision as AXI's primary governed object
  and requires future services to preserve explainability,
  traceability, human accountability, and Organizational Digital Twin
  continuity.
- `ADR-0015` establishes repository stewardship governance, including
  lifecycle, health, archival, and review controls that presentation
  artifacts must not bypass.
- `ADR-0016` establishes Operating Context, Regulatory Knowledge, and
  Readiness as governed decision-support inputs that future dashboards
  and visualizations must surface without dilution.
- `ADR-0017` establishes publications and diagrams as governed platform
  objects and publishes the cross-reference and synchronization rules
  that rendered presentation artifacts must reuse.
- `README.md`, `CODEX_HANDOFF.md`, `Governance/RuntimeRoadmap.md`, and
  `Governance/DependencyMatrix.md` record that runtime implementation
  is complete through `M18 Runtime API` and that no later runtime
  implementation is claimed.
- `AXI-SCH-007` already publishes the `AXI-GUI` namespace, but before
  this ADR the repository does not publish governed object models for
  dashboards, widgets, design-system assets, artifact specifications,
  or visualizations.

Before publication of this ADR, the repository does not publish:

- a dashboard philosophy that distinguishes dashboards from reports
- a governed dashboard lifecycle, inheritance model, or validation
  model
- a governed widget object model
- a governed design-system architecture for brand kits, themes,
  templates, and export styles
- a governed publication type for canonical rendering requirements
- a governed visualization architecture that defines approved visual
  families and their data-source obligations

---

## Architectural Policy

Adopt the following presentation-services governance baseline.

### 1. Presentation Philosophy

Presentation in AXI is governed Decision Intelligence, not cosmetic
decoration.

Dashboards are governed decision surfaces built from canonical
platform objects.

Branding is a governed design system that standardizes how dashboards,
documents, diagrams, reports, presentations, portals, and generated
artifacts are rendered.

Visualizations are governed analytical objects that must preserve
interpretability, accessibility, and traceability.

Dashboards shall never own business data.

Dashboards may consume only:

- governed platform objects
- governed derived aggregates
- governed registers
- governed publication metadata

### 2. Service Set And Responsibility Boundaries

AXI shall use the following presentation service set.

| Service | Unique Responsibility | Required Inputs | Explicit Boundary |
| --- | --- | --- | --- |
| Dashboard Service (`DAS`) | Compose governed dashboards from canonical objects, widgets, templates, permissions, and validation rules. | Governed platform objects, governed widgets, governed templates, governed artifact specifications. | Does not own business data, design tokens, or independent visualization semantics. |
| Design System Service (`DSS`) | Govern brand kits, themes, typographic scales, color systems, component patterns, accessibility baselines, and export styles across rendered artifacts. | Brand governance, accessibility rules, artifact specifications, template taxonomy. | Does not change dashboard semantics, data permissions, or decision logic. |
| Visualization Service (`VS`) | Govern approved visualization families, interpretability rules, executive-summary patterns, and visualization-to-data-source traceability. | Governed platform objects, governed widget metadata, artifact specifications. | Does not own dashboard lifecycle, dashboard permissions, or raw business data. |

No additional presentation service is approved by this ADR.

Future presentation services may be added only when a later ADR proves
that the capability cannot be composed safely from `DAS`, `DSS`, and
`VS`.

### 3. Canonical Presentation Objects

The presentation layer shall treat the following as governed platform
objects:

- `Dashboard`
- `Widget`
- `Visualization`
- `BrandKit`
- `Theme`
- `Template`
- `ArtifactSpecification`

`Dashboard`, `Widget`, `Visualization`, `BrandKit`, `Theme`, and
`Template` shall use the governed presentation namespace published
through `AXI-SCH-007`.

`ArtifactSpecification` shall remain a governed publication-boundary
object subordinate to publication governance and design-system
governance.

### 4. Dashboard Service Governance

Every governed dashboard shall preserve, at minimum:

- dashboard identifier
- dashboard type
- purpose
- audience
- governing object references
- required widgets
- optional widgets
- governed data-source references
- permission model
- version
- lifecycle stage
- inheritance lineage
- customization mode
- validation requirements

The canonical dashboard lifecycle stages are:

- `Defined`
- `Templated`
- `Configured`
- `Validated`
- `Published`
- `Suspended`
- `Retired`

The lifecycle stage is distinct from publication or object status.

### 5. Dashboard Data-Source Governance

Dashboards shall consume governed data only.

At minimum, every governed dashboard shall preserve:

- referenced schema identifiers
- referenced object-type vocabulary
- refresh policy
- lineage requirement
- access scope

Dashboards shall not:

- become a system of record
- store independent business-state copies outside governed object
  boundaries
- side-load ungoverned spreadsheets, extracts, or free-form metrics as
  canonical content

If a dashboard uses derived aggregates, those aggregates shall remain
traceable to governed source objects and access controls.

### 6. Dashboard Permissions, Versioning, And Inheritance

Dashboard permissions shall preserve the distinction between:

- viewing
- editing
- sharing
- administrative control

Permissions shall inherit the strictest relevant rule from the
governing objects and governed data sources referenced by the dashboard.

Dashboard versioning shall use semantic intent:

- major version change for dashboard meaning, audience, widget
  contract, or validation-boundary changes
- minor version change for approved scope expansion that preserves the
  dashboard's governing meaning
- patch version change for layout repair, textual clarification, or
  other edits that do not change governed meaning

Dashboard inheritance shall support:

- canonical base templates
- organization overlays
- layout overlays
- branding overlays
- widget-configuration overlays

No overlay may alter:

- the governing object model
- permission inheritance
- required validation rules
- the rule that dashboards do not own business data

### 7. Canonical Dashboard Types

The minimum approved dashboard set is:

- Executive Dashboard
- Organization Dashboard
- Decision Dashboard
- Repository Dashboard
- Governance Dashboard
- Knowledge Dashboard
- Operational Dashboard
- Risk Dashboard
- Readiness Dashboard
- Project Dashboard
- Portfolio Dashboard
- Learning Dashboard
- Administration Dashboard

Each dashboard type shall define:

- purpose
- audience
- governing objects
- required widgets
- optional widgets
- success metrics

These definitions are operationalized through the governed Dashboard
Register.

### 8. Widget Governance

Widgets are governed objects, not ad hoc interface fragments.

Every governed widget shall preserve, at minimum:

- widget identifier
- version
- purpose
- visualization type
- governed data source
- refresh policy
- security policy
- dependencies
- supported layouts
- accessibility requirements
- related schema references
- related ADR references

Widget security and refresh policy shall inherit from the strictest
constituent data-source and object boundary involved in the widget.

Widgets may be reused across dashboard types, but a widget shall not
change its governing meaning merely because it is placed on another
dashboard.

### 9. Design System Service Governance

`DSS` shall govern the canonical visual system for all rendered AXI
artifacts.

At minimum, the design system shall publish governance for:

- brand kits
- themes
- typography
- color systems
- iconography
- illustration standards
- diagram styling
- UI components
- layout grids
- dashboard templates
- report templates
- document templates
- presentation templates
- accessibility standards
- export styles

The canonical theme hierarchy is:

- Platform Base Theme
- Organization Brand Kit
- Organization Theme Overlay
- Contextual Theme Overlay
- Export Profile

Organizations may customize brand kits and themes without altering
dashboard definitions, governing object semantics, or platform
architecture.

### 10. Artifact Specification Governance

`Artifact Specification` is an approved governed publication type.

Artifact Specifications define canonical rendering requirements for
rendered artifact families.

Every governed artifact family shall preserve, at minimum:

- canonical dimensions
- responsive variants
- minimum sizes
- maximum sizes
- aspect ratios
- margins
- safe areas
- typography scale
- icon sizes
- diagram sizing
- supported export formats
- accessibility expectations
- rendering rules

Artifact Specifications govern rendering behavior for:

- dashboards
- executive briefs
- diagnostic reports
- procedures
- diagrams
- presentations
- PDFs
- Word documents
- mobile views
- web views
- printed reports

Artifact Specifications shall not change the semantics of the governed
dashboard, widget, or source object they render.

### 11. Visualization Service Governance

`VS` shall govern the approved visualization families for AXI.

The minimum approved visualization families are:

- chart standards
- tables
- timelines
- heatmaps
- decision trees
- Sankey diagrams
- organizational charts
- dependency graphs
- Digital Twin visualizations
- geographic maps
- KPI cards
- scorecards
- executive summaries

Every governed visualization shall preserve:

- explicit governed data-source references
- approved use conditions
- prohibited use conditions
- interpretability rules
- narrative-summary expectations when applicable
- uncertainty or confidence disclosure when applicable
- accessibility equivalents

Executive summaries are governed visualization artifacts.

They shall not operate as unsupported narrative decoration.

### 12. Customization And Upgrade Compatibility

Organizations may:

- create dashboards
- clone dashboards
- customize layouts
- customize branding
- configure widgets
- save dashboard templates

only through governed overlay and inheritance boundaries.

Platform upgrades shall preserve organization customizations by
treating local customization as traceable overlay artifacts rather than
silent mutations of the canonical parent definition.

No upgrade may silently rewrite:

- dashboard-to-object mappings
- permission inheritance
- required validation rules
- organization brand ownership

### 13. Future Compatibility Boundary

This architecture shall support future:

- interactive dashboards
- AI-generated dashboards
- role-based command centers
- embedded analytics
- client portals
- executive portals
- mobile applications
- white-label deployments

without requiring architectural redesign.

Future implementation may expand interaction patterns, but it shall
remain subordinate to the governed object, schema, artifact
specification, and customization boundaries published here.

### 14. Constitutional Validation Extension

Future dashboards, widgets, visualizations, and rendered artifacts
shall preserve explicit support for:

- evidence
- provenance
- explainability
- traceability
- human accountability
- accessibility
- security
- uncertainty disclosure where applicable
- governed rendering consistency

---

## Non-Goals

This ADR does not approve:

- runtime implementation of dashboards, web surfaces, portals, or
  mobile applications
- selection of a specific BI, reporting, or front-end framework
- autonomous dashboard publication
- dashboards as systems of record
- free-form branding exceptions that bypass governed design-system
  controls
- any claim that AXI currently renders these services in runtime
  software

---

## Related

- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/ADR/ADR-0016_Decision_Support_Context_Governance.md`
- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/Schemas/AXI-SCH-007_Platform_Object.json`
- `Governance/Schemas/AXI-SCH-022_Publication.json`
- `Governance/Schemas/AXI-SCH-023_Diagram.json`
- `Governance/Schemas/AXI-SCH-024_Dashboard.json`
- `Governance/Schemas/AXI-SCH-025_Widget.json`
- `Governance/Schemas/AXI-SCH-026_Design_System_Asset.json`
- `Governance/Schemas/AXI-SCH-027_Artifact_Specification.json`
- `Governance/Schemas/AXI-SCH-028_Visualization.json`
- `Governance/Publications/AXI_Dashboard_Register.md`
- `Governance/Publications/AXI_Widget_Register.md`
- `Governance/Publications/AXI_Design_System_Architecture.md`
- `Governance/Publications/AXI_Artifact_Specification_Baseline.md`
- `Governance/Publications/Diagrams/DGM-007_Presentation_Services_Topology.md`
- `Governance/WorkQueue/M21-Dashboard-Design-System-Visualization-Services.md`
