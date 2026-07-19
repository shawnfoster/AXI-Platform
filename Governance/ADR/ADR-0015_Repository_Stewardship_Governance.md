# ADR-0015 — Establish Repository Stewardship Governance

## Status

Accepted

---

## Purpose

Define the architectural governance required to keep AXI's repository
knowledge trustworthy, reviewable, restorable, and scalable as the
Decision Intelligence Platform evolves.

This ADR publishes the governing architecture for:

- information lifecycle management
- measurable repository health
- governed archival
- imported content review and quarantine

---

## Repository Evidence

The repository already publishes the following relevant evidence:

- `ADR-0014` establishes AXI's Decision Intelligence architecture
  baseline and requires strict knowledge separation, provenance,
  traceability, and Organizational Digital Twin updates.
- `SCHEMA_REGISTRY` publishes `AXI-SCH-006` through `AXI-SCH-014`, but
  no published schema currently governs information lifecycle,
  repository health, archival, or imported content review.
- `README.md` and `CODEX_HANDOFF.md` record that the runtime foundation
  is implemented through `M18 Runtime API` and that no decision-domain
  runtime implementation is yet claimed.
- Repository searches show historical and reconstruction artifacts that
  reference lifecycle, provenance, health reports, and archive material,
  but those documents are draft or historical artifacts rather than
  current published governance.

Before publication of this ADR, the repository does not publish:

- a canonical information lifecycle for governed repository knowledge
- a repository health model with measurable dimensions
- a governed archive package architecture
- a governed imported-content review and quarantine architecture

---

## Architectural Policy

Adopt the following repository stewardship governance baseline.

### 1. State Separation

AXI shall preserve the distinction between:

- publication status
- information lifecycle state
- review workflow status
- risk classification
- severity
- review authority

These concepts shall not be collapsed into one field.

`Approved` publication status does not imply `Active` lifecycle state.

`Archived` lifecycle state does not imply legal or disposal authority.

`High` severity does not identify which authority must review the case.

### 2. Canonical Information Lifecycle

AXI shall use the following canonical information lifecycle states:

- `Active`
- `Review`
- `Deprecated`
- `Archive Candidate`
- `Archived`
- `Historical`
- `Eligible for Disposal`

Interpretation:

- `Active` means the artifact is currently usable governed knowledge.
- `Review` means the artifact is under governed reassessment and may be
  restricted from new canonization or import use until review completes.
- `Deprecated` means the artifact remains preserved but is no longer the
  preferred active source.
- `Archive Candidate` means the artifact is being prepared for governed
  archival with manifest, snapshot, dependency, and provenance checks.
- `Archived` means the artifact has been packaged, preserved, and
  removed from active operational use without losing restoration
  capability.
- `Historical` means the artifact is retained for lineage, audit,
  provenance, or reference purposes even when it is not operationally
  active.
- `Eligible for Disposal` means the artifact may be considered for a
  separate manual human disposal process after all preservation,
  dependency, legal, audit, and provenance obligations are satisfied.

### 3. Lifecycle Transition Governance

Every lifecycle transition shall record:

- prior state
- new state
- reason
- authorized human owner
- authorization timestamp
- related evidence
- dependency impact summary
- archive package reference when applicable
- related decision or review case when applicable

The minimum governed transition paths are:

- `Active` -> `Review`
- `Review` -> `Active`
- `Review` -> `Deprecated`
- `Review` -> `Archive Candidate`
- `Review` -> `Historical`
- `Deprecated` -> `Archive Candidate`
- `Deprecated` -> `Historical`
- `Archive Candidate` -> `Archived`
- `Archive Candidate` -> `Active`
- `Archived` -> `Historical`
- `Historical` -> `Eligible for Disposal`
- `Historical` -> `Archived`

This ADR does not authorize automatic deletion from any lifecycle state.

Transition to `Eligible for Disposal` is manual-only and does not, by
itself, authorize destruction, removal from version history, or
permanent data loss.

### 4. Repository Health Model

Repository health shall be measured through explicit governed
assessments rather than ad hoc cleanup narratives.

The canonical repository health dimensions are:

- Knowledge Quality
- Knowledge Entropy
- Duplicate Risk
- Provenance Coverage
- Reference Integrity
- Governance Compliance
- Placeholder Artifacts
- Canonical Coverage
- Documentation Waste
- Import Readiness

Each health assessment shall preserve, for every dimension:

- a normalized health score
- a health status band
- a trend
- a measurement basis
- traceable supporting evidence

Health status bands are:

- `Healthy`
- `Watch`
- `At Risk`
- `Critical`

Health assessments may publish an aggregate repository health status,
but aggregate status shall never replace metric-level detail.

### 5. Repository Health Governance Expectations

The canonical interpretation of the health dimensions is:

- `Knowledge Quality`: clarity, completeness, structure, currency, and
  fitness for governed reuse.
- `Knowledge Entropy`: uncontrolled drift, fragmentation, contradiction,
  and semantic disorder.
- `Duplicate Risk`: likelihood of competing or conflicting canonical
  sources.
- `Provenance Coverage`: traceable source and authorship coverage across
  governed artifacts.
- `Reference Integrity`: whether links, references, dependencies, and
  citations remain valid and resolvable.
- `Governance Compliance`: conformance to published ADR, schema,
  contract, roadmap, and workflow obligations.
- `Placeholder Artifacts`: presence of placeholder-only files in paths
  where published governance or canonical content is expected.
- `Canonical Coverage`: extent to which governed domains are covered by
  approved canonical artifacts instead of orphan or ambiguous content.
- `Documentation Waste`: redundant, stale, low-signal, or misleading
  material that consumes review effort without improving governance.
- `Import Readiness`: whether imported content is sufficiently
  classified, provenance-aware, reviewable, and quarantinable before it
  can be proposed as governed knowledge.

### 6. Archive Architecture

AXI archival shall preserve restorable governed history.

Archival shall be implemented through:

- Archive Packages
- Archive Manifest
- Repository Snapshots
- Restoration Requirements
- Dependency Preservation
- Provenance Preservation
- Historical Classification

Artifacts shall never be deleted automatically as part of the archival
process.

Every archive package shall preserve:

- the archived artifact set
- a manifest of included artifacts
- a repository snapshot reference
- dependency preservation records
- provenance preservation records
- restoration instructions
- historical classification

The standard governed archive structure is:

```text
Archive/
  Packages/
    <archive_package_id>/
      manifest.json
      snapshot/
      artifacts/
      dependencies/
      provenance/
      restoration/
```

The archive package is the canonical unit of archival governance.

### 7. Archive Restoration Requirements

An archive package shall not be considered governed archival evidence
unless restoration requirements are documented.

Restoration requirements shall preserve at minimum:

- required tools or environments
- required approvals
- dependency reconstruction requirements
- repository snapshot or VCS reference
- material blockers to successful restoration

### 8. Historical Classification

Archive packages shall preserve one or more historical classifications.

The approved classifications are:

- Governance History
- Decision History
- Evidence History
- Knowledge History
- Imported Content History
- Runtime History
- Release History
- Legal Hold History

Future governance may extend this classification set, but this ADR does
not authorize unclassified archival.

### 9. Imported Content Review

Imported content requiring review shall not enter the governed
knowledge base directly.

Imported content shall first enter a governed review case and, when
required, a quarantine boundary.

The canonical review workflow status values are:

- `Submitted`
- `Screening`
- `Under Review`
- `Escalated`
- `Awaiting Disposition`
- `Dispositioned`
- `Closed`

The canonical risk classifications are:

- `Security`
- `Privacy`
- `Legal`
- `Compliance`
- `Governance`
- `Provenance`
- `Content`
- `Quality`
- `Executive Review`

The canonical severity values are:

- `Informational`
- `Low`
- `Moderate`
- `High`
- `Critical`

The canonical review authority values are:

- `Content Steward`
- `Governance Steward`
- `Provenance Steward`
- `Security Review`
- `Privacy Review`
- `Legal Review`
- `Compliance Review`
- `Executive Review`

### 10. Quarantine Architecture

Quarantine exists to preserve evidence without polluting the governed
knowledge base.

Quarantined content:

- remains preserved
- remains traceable
- may be analyzed
- may be referenced by review records
- shall not be treated as approved governed knowledge until released

The standard governed quarantine structure is:

```text
Governance/
  Quarantine/
    <review_case_id>/
      case.json
      source/
      evidence/
      analysis/
      release/
```

The review case is the canonical governance boundary for imported
content under review.

### 11. Release Boundary

Imported content may enter governed knowledge only when:

- required authorities have completed review
- disposition permits governed ingest
- provenance is preserved
- release conditions are satisfied
- quarantine status is updated accordingly

This ADR does not authorize automatic canonization of imported content.

---

## Future Guidance

Future governance may publish:

- repository health scoring formulas
- automated but governed measurement tools
- archive storage policies
- quarantine tooling
- disposal procedure governance

Those items are not implementation-approved by this ADR.

---

## Non-Goals

This ADR does not approve:

- automatic repository deletion
- automatic historical disposal
- automatic canonization of imported content
- runtime implementation for repository stewardship
- any claim that archival or quarantine automation exists today

---

## Related

- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/Schemas/AXI-SCH-015_Information_Lifecycle_Record.json`
- `Governance/Schemas/AXI-SCH-016_Repository_Health_Assessment.json`
- `Governance/Schemas/AXI-SCH-017_Archive_Package.json`
- `Governance/Schemas/AXI-SCH-018_Review_Case.json`
- `Governance/Roadmap/AXI_Roadmap_v1.0.md`
