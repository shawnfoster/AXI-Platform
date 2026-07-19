# Documentation Quality Standard

**Publication ID:** `PUB-006`
**Publication Type:** `Standard`
**Version:** `1.1.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Annual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Audit Date:** `2026-07-19`

---

# Purpose

Publish the measurable quality baseline for AXI documentation.

Documentation quality is a governed repository-health surface rather
than an informal editorial judgment.

---

# Canonical Metrics

| Metric | Definition | Minimum Evidence Basis | Repository Health Tie |
| --- | --- | --- | --- |
| Coverage | Degree to which required canonical publications exist for the approved architecture domains. | Published publication register, roadmap, and architectural domain list. | Canonical Coverage |
| Traceability | Degree to which publications preserve required references to governing ADRs, schemas, capabilities, and dependencies. | Publication metadata and cross-reference audit. | Provenance Coverage, Governance Compliance |
| Diagram Coverage | Degree to which major domains and major publications have required canonical diagrams. | Diagram register and completeness audit. | Canonical Coverage, Knowledge Quality |
| Cross-reference Integrity | Degree to which identifiers, paths, and cited artifacts resolve correctly. | Link, path, and identifier audit. | Reference Integrity |
| Publication Freshness | Degree to which publications remain within their governed review cycle. | Review-cycle audit and review history. | Knowledge Quality |
| Review Compliance | Degree to which required reviews and approvals are completed by the correct authority. | Review history and approval records. | Governance Compliance |
| Completeness | Degree to which required sections, metadata, and supporting artifacts are present. | Publication-family checklist and schema audit. | Knowledge Quality |
| Canonical Consistency | Degree to which lower-level publications remain aligned with higher-authority governance. | ADR-to-publication consistency review. | Governance Compliance, Duplicate Risk |
| Readability | Degree to which the publication can be understood without ambiguity, uncontrolled jargon, or incoherent structure. | Governed review judgment with documented findings. | Knowledge Quality |
| Reuse | Degree to which publications reuse canonical references instead of duplicating or fragmenting governed guidance. | Cross-reference audit and duplicate-content review. | Documentation Waste, Knowledge Entropy |

---

# Measurement Rules

- Every metric shall preserve traceable evidence.
- Narrative claims of quality are insufficient without the auditable
  basis used to support them.
- Where normalized scoring is used, documentation-quality assessments
  may reuse the repository-health status bands from `ADR-0015`:
  `Healthy`, `Watch`, `At Risk`, `Critical`.
- Metric-level detail shall be preserved even when an aggregate
  documentation-quality summary is reported.

---

# Timestamp And Evidence Policy

- Repository audit claims shall be grounded in immutable repository
  evidence wherever practical.
- Prefer commit identifiers, version identifiers, publication
  identifiers, ADR identifiers, schema identifiers, milestone
  identifiers, and approved status or lifecycle state over narrative or
  conversational dates when those identifiers are sufficient.
- Natural-language dates should be avoided wherever a stable repository
  identifier or status can express the same fact.
- When a publication family requires an `Audit Date`, use the execution
  environment date in ISO `YYYY-MM-DD` form consistently across the
  changed artifact set.
- Do not infer repository dates from chat conversation timing.
- Do not rewrite historical repository timestamps solely because a
  conversational reference uses a different clock.

---

# Review Expectations

- Documentation quality shall be reviewed whenever a major publication
  is introduced, superseded, or materially restructured.
- Documentation quality shall be reviewed when repository-health
  findings indicate deterioration in canonical coverage, reference
  integrity, placeholder artifacts, or documentation waste.
- Documentation quality shall be reviewed before AXI claims a manual or
  playbook family is operationally ready.

---

# Future Integration Boundary

This standard is intended to support future interactive manuals,
searchable knowledge, context-aware guidance, training surfaces, and
brief-generation workflows without redefining the quality model.

This standard does not authorize implementation of those capabilities.

---

# Related

- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/Publications/PUBLICATION_REGISTER.md`
- `Governance/Publications/DIAGRAM_REGISTER.md`
- `Governance/Schemas/AXI-SCH-016_Repository_Health_Assessment.json`
