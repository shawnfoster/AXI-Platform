# AXI Design System Architecture And Template Taxonomy

**Publication ID:** `PUB-009`
**Publication Type:** `Reference`
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

Publish the governed design-system architecture for AXI and the
canonical template taxonomy used by rendered presentation artifacts.

The design system is the governed visual language of the platform.

It ensures every dashboard, document, diagram, report, presentation,
portal, and generated artifact can share a coherent visual identity
without changing the semantics of the underlying governed objects.

---

# Design System Philosophy

The design system shall:

- apply branding at render time rather than semantic-definition time
- separate visual customization from dashboard meaning
- preserve accessibility as a non-optional control boundary
- support organization-specific brand overlays without forking
  canonical dashboard definitions
- support white-label rendering without architectural redesign

The design system shall not:

- change governing objects
- change dashboard permissions
- change widget meaning
- bypass artifact specifications

---

# Canonical Design Layers

| Layer | Governed Objects | Purpose | Customization Boundary |
| --- | --- | --- | --- |
| Brand Kit | `BrandKit` | Publish organization identity tokens, brand voice cues, and core visual signatures. | Organizations may replace brand-owned tokens while preserving accessibility and artifact-specification rules. |
| Theme | `Theme` | Apply color, typography, spacing, and emphasis choices to a presentation context. | Organizations may extend platform themes through overlays but may not remove required accessibility controls. |
| Typography Scale | `Theme` | Govern type hierarchy, fallback families, spacing, and readability rhythm. | Organizations may select approved font families and scale variants without changing semantic heading structure. |
| Color System | `BrandKit`, `Theme` | Govern palettes, semantic tokens, contrast rules, and emphasis patterns. | Organizations may map brand colors into governed semantic tokens but may not bypass contrast standards. |
| Iconography | `Theme` | Govern icon family, stroke logic, size scale, and meaning consistency. | Organizations may choose approved icon families and accents without changing icon semantic roles. |
| Illustration Standard | `Theme` | Govern non-data illustration motifs, scene language, and abstraction level. | Organizations may tailor style motifs while preserving tone and accessibility. |
| Diagram Styling | `Theme` | Align diagrams to the governed visual language while preserving notation clarity. | Organizations may restyle accents and containers without changing diagram meaning or notation. |
| UI Component System | `Template`, `Theme` | Govern cards, tables, headers, filters, navigation shells, and annotation patterns. | Organizations may vary ornamentation and density within approved component contracts. |
| Layout Grid | `Template` | Govern responsive structure, spacing rhythm, and safe placement zones. | Organizations may choose approved grid variants but may not violate safe areas or readability thresholds. |
| Dashboard Template Family | `Template` | Provide governed dashboard starting points by audience and purpose. | Organizations may overlay branding and layout; canonical object bindings remain governed. |
| Report Template Family | `Template` | Standardize executive briefs, diagnostic reports, and PDF report shells. | Organizations may overlay brand style and cover treatment without changing evidence structure. |
| Document Template Family | `Template` | Standardize SOP, reference, and document rendering patterns. | Organizations may customize headers, footers, and accent tokens within artifact-specification limits. |
| Presentation Template Family | `Template` | Standardize deck layouts for executive, board, and project communication. | Organizations may customize brand overlays while preserving slide-safe and typography rules. |
| Accessibility Baseline | `Theme`, `Template` | Make contrast, motion, text scaling, focus order, and non-visual alternatives mandatory. | No organization override may disable this layer. |
| Export Style Profile | `Theme`, `Template` | Govern print, PDF, PPT, DOCX, web, mobile, and white-label output behavior. | Organizations may choose approved output profiles without changing underlying artifact specifications. |

---

# Theme Hierarchy

The canonical theme hierarchy is:

1. Platform Base Theme
2. Organization Brand Kit
3. Organization Theme Overlay
4. Contextual Theme Overlay
5. Export Style Profile

A later layer may refine a prior layer only within its approved
boundary.

If two layers conflict, the stricter accessibility rule prevails.

If an export profile conflicts with a contextual theme, the governing
artifact specification prevails.

---

# Template Taxonomy

| Template Family | Governed Uses | Primary Channels | Default Artifact Specifications |
| --- | --- | --- | --- |
| Dashboard Templates | Executive, organization, decision, repository, governance, knowledge, operational, risk, readiness, project, portfolio, learning, and administration dashboards | Web, mobile, portal | `AS-001`, `AS-002` |
| Report Templates | Executive briefs, diagnostic reports, outcome summaries, printable management reports | PDF, print, web export | `AS-003`, `AS-004`, `AS-010`, `AS-012` |
| Document Templates | SOPs, reference documents, controlled narrative documents, Word-ready artifacts | DOCX, PDF, print | `AS-005`, `AS-010`, `AS-011` |
| Diagram Templates | Architecture diagrams, workflow diagrams, and decision trees with governed styling | Web, SVG, PNG, PDF | `AS-006`, `AS-007`, `AS-008` |
| Presentation Templates | Executive decks, board decks, project reviews, portfolio briefings | Presentation, PDF | `AS-009`, `AS-010` |
| Portal Templates | Executive portals, client portals, role-based command centers, embedded analytics shells | Web, mobile | `AS-001`, `AS-002` |
| Export Templates | PDF packages, print packages, white-label deliverables, branded handoff artifacts | PDF, print, DOCX, PPTX | `AS-009`, `AS-010`, `AS-011`, `AS-012` |

---

# Customization Rules

- Organizations may customize brand kits, themes, and template
  ornamentation without changing dashboard semantics.
- Dashboard definitions remain subordinate to governed object, widget,
  and validation contracts even when a local template overlay exists.
- Artifact specifications control safe areas, margins, aspect ratios,
  and export behavior even when the organization supplies a custom
  theme.
- White-label rendering is permitted only through approved brand-kit
  and export-profile overlays.

---

# Related

- `Governance/ADR/ADR-0018_Presentation_Services_Governance.md`
- `Governance/Schemas/AXI-SCH-026_Design_System_Asset.json`
- `Governance/Schemas/AXI-SCH-027_Artifact_Specification.json`
- `Governance/Publications/AXI_Artifact_Specification_Baseline.md`
- `Governance/Publications/Diagrams/DGM-007_Presentation_Services_Topology.md`
