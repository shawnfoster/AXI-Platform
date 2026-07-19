# AXI Artifact Specification Baseline

**Publication ID:** `PUB-010`
**Publication Type:** `Artifact Specification`
**Version:** `1.0.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Annual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Audit Date:** `2026-07-19`

---

# Purpose

Publish the canonical rendering baseline for governed AXI artifact
families.

Artifact Specifications define the rendering contract for dashboards,
documents, diagrams, reports, presentations, and export packages
without changing the semantics of the governed objects they render.

---

# Canonical Artifact Specification Model

Every governed Artifact Specification shall define:

- `AS` identifier
- artifact family
- canonical dimensions
- responsive variants
- minimum sizes
- maximum sizes
- aspect ratio
- margins
- safe areas
- typography scale
- icon size scale
- diagram sizing rules
- supported export formats
- accessibility baseline
- rendering rules

---

# Canonical Artifact Specifications

| AS ID | Artifact Family | Canonical Dimensions | Responsive Variants | Min / Max / Aspect Ratio | Margins And Safe Areas | Type / Icon / Diagram Rules | Supported Exports | Accessibility Baseline |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `AS-001` | Dashboard Web View | `1440 x 900 px` | `1280`, `1600`, `1920` wide variants | Min `1024 x 640 px`, max `1920 x 1080 px`, `16:10` to `16:9` | `24 px` margins, `16 px` safe area | Type scale `12 / 14 / 18 / 24`, icons `16 / 20 / 24`, diagrams stay within governed grid | `HTML`, `PDF`, `PNG` | Keyboard navigation, screen-reader summaries, non-color encoding, AA contrast |
| `AS-002` | Dashboard Mobile View | `390 x 844 px` | `360 x 800`, `430 x 932` | Min `320 x 568 px`, max `480 x 960 px`, portrait-first | `16 px` margins, `12 px` safe area | Type scale `12 / 14 / 18 / 22`, icons `16 / 20`, diagrams collapse to single-column | `HTML`, `PDF`, `PNG` | Touch target minimums, text scaling, screen-reader summaries, AA contrast |
| `AS-003` | Executive Brief | `8.5 x 11 in` portrait | `A4` portrait variant | Min `8.27 x 11.69 in`, max `8.5 x 11 in`, portrait | `0.75 in` margins, `0.5 in` safe area | Type scale `10 / 12 / 18 / 28`, icons `14 / 18`, diagrams max `6.5 in` width | `PDF`, `DOCX` | Readable heading order, alt text for visuals, print-safe contrast |
| `AS-004` | Diagnostic Report | `8.5 x 11 in` portrait | `A4` portrait, landscape appendix pages | Min `8.27 x 11.69 in`, max `11 x 17 in` appendix, portrait primary | `0.85 in` margins, `0.5 in` safe area | Type scale `10 / 12 / 16 / 24`, icons `14 / 18`, complex diagrams may span landscape appendix | `PDF`, `DOCX` | Structured headings, table captions, appendix navigation, print-safe contrast |
| `AS-005` | Standard Operating Procedure | `8.5 x 11 in` portrait | `A4` portrait | Min `8.27 x 11.69 in`, max `8.5 x 11 in`, portrait | `1.0 in` margins, `0.5 in` safe area | Type scale `10 / 12 / 16 / 22`, icons `14 / 16`, diagrams limited to step-support visuals | `PDF`, `DOCX` | Step numbering clarity, alt text, accessible tables, print-safe contrast |
| `AS-006` | Architecture Diagram | `1600 x 900 px` | `1920 x 1080`, scalable `SVG` | Min `1200 x 675 px`, max scalable, `16:9` | `48 px` margins, `32 px` safe area | Type scale `14 / 18 / 24`, icons `20 / 24`, diagram nodes and edges must preserve label readability | `SVG`, `PNG`, `PDF` | Text alternatives, non-color encoding, readable label density |
| `AS-007` | Workflow Diagram | `1600 x 1200 px` | `1920 x 1440`, scalable `SVG` | Min `1200 x 900 px`, max scalable, `4:3` or vertical flow | `48 px` margins, `32 px` safe area | Type scale `14 / 18 / 22`, icons `18 / 22`, diagram spacing must preserve step order clarity | `SVG`, `PNG`, `PDF` | Text alternatives, directional clarity, non-color encoding |
| `AS-008` | Decision Tree | `1200 x 1600 px` | Landscape `1600 x 1200` when needed | Min `900 x 1200 px`, max scalable, portrait-first | `40 px` margins, `24 px` safe area | Type scale `14 / 18 / 22`, icons `18 / 20`, branch labels must remain readable without hover | `SVG`, `PNG`, `PDF` | Text alternatives, branch summaries, keyboard-accessible export when interactive later exists |
| `AS-009` | Presentation Deck | `1920 x 1080 px` | `1280 x 720`, `4:3` fallback | Min `1024 x 768 px`, max `1920 x 1080 px`, `16:9` primary | `64 px` margins, `32 px` safe area | Type scale `20 / 28 / 40`, icons `24 / 32`, diagrams fit slide-safe zones without microtext | `PPTX`, `PDF` | Large-text readability, presenter-notes compatibility, high-contrast export |
| `AS-010` | PDF Export Package | Inherits source artifact spec | Source-driven variants | Inherits source artifact size and ratio | Add `0.25 in` export-safe perimeter when paginated | Preserve source type scale and diagram sizing; no semantic relayout | `PDF` | Tagged PDF, bookmarks when paginated, alt text retention |
| `AS-011` | Word Document | `8.5 x 11 in` portrait | `A4` portrait | Min `8.27 x 11.69 in`, max `8.5 x 11 in`, portrait | `1.0 in` margins, `0.5 in` safe area | Type scale `10 / 12 / 16 / 22`, icons `14 / 16`, diagrams anchored inline or full-width | `DOCX`, `PDF` | Heading styles, accessible tables, alt text, printable contrast |
| `AS-012` | Printed Report | `8.5 x 11 in` portrait | `A4` portrait, `11 x 17 in` foldout appendix | Min `8.27 x 11.69 in`, max `11 x 17 in`, portrait primary | `0.75 in` margins, `0.5 in` safe area, print bleed only when approved | Type scale `10 / 12 / 18 / 26`, icons `14 / 18`, diagrams sized for arm's-length readability | `PDF`, print-ready output | Print-safe contrast, clear pagination, accessible source companion required |

---

# Rendering Rules

- Dashboard definitions shall not embed organization-specific brand
  tokens directly.
- Artifact Specifications apply after dashboard, widget, and
  visualization semantics are resolved.
- Export formats shall preserve the governing source order, labels, and
  explanatory context rather than reinterpreting them.
- If an artifact uses a governed diagram, the export shall preserve the
  diagram's readable label density and text alternative.
- When an artifact is rendered through a white-label profile, the
  artifact specification still governs safe areas, typography scale,
  accessibility, and export fidelity.

---

# Related

- `Governance/ADR/ADR-0018_Presentation_Services_Governance.md`
- `Governance/Schemas/AXI-SCH-022_Publication.json`
- `Governance/Schemas/AXI-SCH-027_Artifact_Specification.json`
- `Governance/Publications/AXI_Design_System_Architecture.md`
