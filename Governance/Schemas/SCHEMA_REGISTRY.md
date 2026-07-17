# AXI Schema Registry

**Version:** 1.1.0
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
| `AXI-SCH-007` | Platform Object | `Governance/Schemas/AXI-SCH-007_Platform_Object.json` | Published |
| `AXI-SCH-008` | Capability | `Governance/Schemas/AXI-SCH-008_Capability.json` | Published |
| `AXI-SCH-009` | Plugin Manifest | `Governance/Schemas/AXI-SCH-009_Plugin_Manifest.json` | Published |
| `AXI-SCH-010` | Application | `Governance/Schemas/AXI-SCH-010_Application.json` | Published |
| `AXI-SCH-011` | Engine | `Governance/Schemas/AXI-SCH-011_Engine.json` | Published |
| `AXI-SCH-012` | Pipeline | `Governance/Schemas/AXI-SCH-012_Pipeline.json` | Published |

---

# Placeholder Schemas

The following schema files exist in the repository but contain no
approved schema content:

- `AXI-SCH-001_Inventory.json`
- `AXI-SCH-002_Classification.json`
- `AXI-SCH-003_Duplicates.json`
- `AXI-SCH-004_Provenance.json`
- `AXI-SCH-005_Canonical.json`
- `AXI-SCH-006_Decisions.json`
- `AXI-SCH-013_CLI_Command.json`
- `AXI-SCH-014_API_Operation.json`

Placeholder schemas are not authoritative and shall not be treated as
published validation inputs.

---

# Implementation Guidance

If a future runtime validation framework performs schema validation, it
should use only schema artifacts listed as `Published` in this registry
unless later governance approves additional schemas.
