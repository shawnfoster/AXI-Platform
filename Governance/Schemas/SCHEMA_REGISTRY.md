# AXI Schema Registry

**Version:** 1.8.0
**Status:** Approved
**Authority:** AXI Platform Governance

---

# Purpose

Record which schema artifacts in `Governance/Schemas/` are currently
published repository evidence and which remain placeholders.

This registry is derived from the currently published repository state.

---

# Repository Evidence

Published schema files with approved content:

| Schema ID | Title | Path | Status |
| --- | --- | --- | --- |
| `AXI-SCH-006` | Decision | `Governance/Schemas/AXI-SCH-006_Decisions.json` | Published |
| `AXI-SCH-007` | Platform Object | `Governance/Schemas/AXI-SCH-007_Platform_Object.json` | Published |
| `AXI-SCH-008` | Capability | `Governance/Schemas/AXI-SCH-008_Capability.json` | Published |
| `AXI-SCH-009` | Plugin Manifest | `Governance/Schemas/AXI-SCH-009_Plugin_Manifest.json` | Published |
| `AXI-SCH-010` | Application | `Governance/Schemas/AXI-SCH-010_Application.json` | Published |
| `AXI-SCH-011` | Engine | `Governance/Schemas/AXI-SCH-011_Engine.json` | Published |
| `AXI-SCH-012` | Pipeline | `Governance/Schemas/AXI-SCH-012_Pipeline.json` | Published |
| `AXI-SCH-013` | CLI Command | `Governance/Schemas/AXI-SCH-013_CLI_Command.json` | Published |
| `AXI-SCH-014` | API Operation | `Governance/Schemas/AXI-SCH-014_API_Operation.json` | Published |
| `AXI-SCH-015` | Information Lifecycle Record | `Governance/Schemas/AXI-SCH-015_Information_Lifecycle_Record.json` | Published |
| `AXI-SCH-016` | Repository Health Assessment | `Governance/Schemas/AXI-SCH-016_Repository_Health_Assessment.json` | Published |
| `AXI-SCH-017` | Archive Package | `Governance/Schemas/AXI-SCH-017_Archive_Package.json` | Published |
| `AXI-SCH-018` | Review Case | `Governance/Schemas/AXI-SCH-018_Review_Case.json` | Published |
| `AXI-SCH-019` | Operating Context | `Governance/Schemas/AXI-SCH-019_Operating_Context.json` | Published |
| `AXI-SCH-020` | Regulatory Knowledge | `Governance/Schemas/AXI-SCH-020_Regulatory_Knowledge.json` | Published |
| `AXI-SCH-021` | Readiness Profile | `Governance/Schemas/AXI-SCH-021_Readiness_Profile.json` | Published |
| `AXI-SCH-022` | Publication | `Governance/Schemas/AXI-SCH-022_Publication.json` | Published |
| `AXI-SCH-023` | Diagram | `Governance/Schemas/AXI-SCH-023_Diagram.json` | Published |
| `AXI-SCH-024` | Dashboard | `Governance/Schemas/AXI-SCH-024_Dashboard.json` | Published |
| `AXI-SCH-025` | Widget | `Governance/Schemas/AXI-SCH-025_Widget.json` | Published |
| `AXI-SCH-026` | Design System Asset | `Governance/Schemas/AXI-SCH-026_Design_System_Asset.json` | Published |
| `AXI-SCH-027` | Artifact Specification | `Governance/Schemas/AXI-SCH-027_Artifact_Specification.json` | Published |
| `AXI-SCH-028` | Visualization | `Governance/Schemas/AXI-SCH-028_Visualization.json` | Published |
| `AXI-SCH-029` | Organization | `Governance/Schemas/AXI-SCH-029_Organization.json` | Published |
| `AXI-SCH-030` | Knowledge | `Governance/Schemas/AXI-SCH-030_Knowledge.json` | Published |

---

# Placeholder Schemas

The following schema files exist in the repository but contain no
approved schema content:

- `AXI-SCH-001_Inventory.json`
- `AXI-SCH-002_Classification.json`
- `AXI-SCH-003_Duplicates.json`
- `AXI-SCH-004_Provenance.json`
- `AXI-SCH-005_Canonical.json`

Placeholder schemas are not authoritative and shall not be treated as
published validation inputs.

---

# Implementation Guidance

If a future runtime validation framework performs schema validation, it
should use only schema artifacts listed as `Published` in this registry
unless later governance approves additional schemas.

`AXI-SCH-006` publishes the governed structure for decision records.
Publication of that schema does not, by itself, authorize runtime
implementation or claim runtime validation support for decision-domain
artifacts.

`AXI-SCH-015` through `AXI-SCH-023` publish governance structures for
repository stewardship, decision-support context, publications, and
diagrams.

`AXI-SCH-024` through `AXI-SCH-028` publish governance structures for
dashboards, widgets, design-system assets, artifact specifications, and
visualizations.

Publication of those schemas does not, by itself, authorize runtime
implementation or claim runtime validation support for those domains.

`AXI-SCH-029` and `AXI-SCH-030` publish governance structures for
Organization and Knowledge objects within the Organization Intelligence
domain.

Publication of those schemas does not, by itself, authorize runtime
implementation or claim runtime validation support for the core `ODT`
domain.
