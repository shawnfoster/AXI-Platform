# ADR-0020 — Establish Knowledge Expansion And Repository Operationalization Governance

## Status

Accepted

---

## Purpose

Define the architectural governance required to evolve AXI from a
repository-centered governance system into the governing intelligence
layer for the user's broader digital knowledge ecosystem.

This ADR publishes the governing architecture for:

- Knowledge Expansion as a governed AXI domain
- Repository Operationalization as a future governed workspace posture
- progressive external-knowledge discovery, intake, and canonization
- provenance, duplicate, confidence, and review governance for
  external artifacts
- future Operational Pack boundaries
- future AI-generated reasoning governance over expanded knowledge

---

## Repository Evidence

The repository already publishes the following relevant evidence:

- `ADR-0014` establishes AXI as a Decision Intelligence Platform,
  preserves strict knowledge-domain separation, and makes the
  Organizational Digital Twin a first-class governed domain.
- `ADR-0015` publishes repository stewardship governance, including
  information lifecycle, repository-health, archive, and imported-
  content review controls.
- `ADR-0016` distinguishes durable organizational knowledge from
  Operating Context, Regulatory Knowledge, and Readiness.
- `ADR-0017` publishes the cross-reference, review, and diagram
  completeness rules required for new major architectural domains.
- `ADR-0018` publishes Presentation Services governance and requires
  rendered artifacts to remain downstream consumers of governed
  objects.
- `ADR-0019` publishes Organization Intelligence governance and begins
  the core `ODT` schema-and-register baseline through `M22`.
- `README.md`, `CODEX_HANDOFF.md`, and
  `Governance/Roadmap/AXI_Roadmap_v1.0.md` record that runtime
  implementation remains intentionally limited to `M18` and that `M22`
  remains the current active governance-only milestone.
- `CAPABILITY_REGISTER` already publishes stewardship, provenance,
  archive, review, publication, visualization, and decision-context
  capabilities, but it does not yet publish a constitutional
  architecture for governing the user's broader digital knowledge
  corpus.
- `Governance/Reconstruction/` contains historical and founder-review
  inventory, classification, duplicate, provenance, and canonicalization
  artifacts, but those materials are reconstruction evidence rather
  than current authoritative governance.

Before publication of this ADR, the repository does not publish:

- a canonical architecture for external knowledge expansion beyond the
  repository boundary
- a governed progression for how discovered artifacts become
  operationally useful AXI knowledge
- a future workspace-governance posture in which AXI governs the
  user's ecosystem without requiring total migration before value
- a constitutional boundary for Operational Packs that derive from
  governed knowledge rather than maintaining independent data silos

---

## Architectural Policy

Adopt the following Knowledge Expansion and Repository
Operationalization governance baseline.

### 1. Knowledge Expansion Domain

Knowledge Expansion is a governed architectural domain of AXI.

Its purpose is to progressively bring external artifacts, repositories,
documents, and media into governed AXI knowledge without losing
provenance, confidence, historical availability, or reviewability.

Knowledge Expansion is not a runtime ingest engine, indexing engine,
vector database, connector framework, or storage migration utility.

It is the governance architecture that makes future expansion of the
user's knowledge ecosystem safe, traceable, and operationally useful.

### 2. Repository Authority And Ecosystem Boundary

The AXI repository remains the authoritative source of governance.

It is not assumed to contain the complete raw knowledge corpus.

Future governed knowledge may originate from sources such as:

- local storage
- source repositories
- exported ChatGPT projects
- Notion
- research archives
- PDFs
- Word documents
- spreadsheets
- presentations
- diagrams
- images
- audio
- video
- business documentation
- creative assets
- historical archives
- templates
- reference libraries

External discoverability does not make an artifact canonical.

Every artifact outside the current canon shall enter governance through
the Knowledge Expansion architecture before it may influence
decision-quality, pack-derived outputs, or operational workspace
behavior as governed knowledge.

### 3. Knowledge Expansion Progression

AXI shall use the following canonical progression for future knowledge
expansion:

1. Discover
2. Inventory
3. Classify
4. Normalize
5. Deduplicate
6. Validate
7. Govern
8. Operationalize
9. Continuously Improve

This progression is constitutional guidance, not a runtime workflow
implementation.

It shall remain distinct from the information lifecycle states
published in `ADR-0015`.

An artifact may move through multiple progression stages while still
remaining in lifecycle states such as `Review`, `Historical`, or
`Archived`.

### 4. Governed Import And Expansion Boundary

Future knowledge-expansion governance shall preserve explicit support
for:

- discovery records for artifacts not yet governed
- inventory identity and source-system tracking
- provenance capture before canonization
- classification and normalization before operational reuse
- duplicate and canonical-selection review
- governed review and quarantine when evidence, ownership, confidence,
  sensitivity, or authority remain unresolved
- traceable mapping into governed objects, knowledge domains,
  publications, historical holdings, or archive packages

No future artifact shall move directly from discovery into approved
canon without the governed review path required by repository
stewardship and later milestone-specific governance.

### 5. Provenance And Historical Preservation

Knowledge Expansion shall preserve origin rather than overwrite it.

At minimum, future expansion governance shall preserve:

- source location or source-system identity when available
- acquisition or reconstruction context
- timestamps and stewards where available
- transformation lineage when content is normalized, merged, or derived
- supersession relationships
- historical accessibility for non-canonical or superseded variants

Canonical selection shall never erase alternate sources, duplicates,
drafts, or predecessor artifacts without preserving the governed
history required to explain why the canon changed.

### 6. Canonical Selection, Duplicate Governance, And Confidence

Knowledge Expansion shall treat duplicate handling and canonical
selection as governed decisions, not convenience heuristics.

Future knowledge-expansion governance shall preserve explicit support
for:

- duplicate candidate identification
- canonical-selection rationale
- alternate-source preservation
- conflict or contradiction state
- evidence-strength and confidence representation
- uncertainty and incompleteness signaling
- unresolved review routing when canonical choice remains unsafe

This ADR does not assign the final schema for confidence expression.

It does require future schemas, registers, and packs to represent
confidence, uncertainty, and reviewability explicitly rather than
burying them in free-form notes.

### 7. Review Workflow For Unresolved Knowledge

When discovered or imported knowledge remains unresolved, AXI shall
prefer governed review over false canonization.

Future knowledge-expansion governance shall ensure unresolved knowledge
can be:

- held in review
- quarantined when risk, authority, or provenance gaps require it
- preserved historically without being treated as active canon
- escalated for human review when decision, legal, ethical, privacy, or
  business significance requires explicit approval

Imported or reconstructed knowledge that has not satisfied the required
review path shall not be treated as approved decision input merely
because it is searchable or present in storage.

### 8. Repository Operationalization

Repository Operationalization is the future governed posture in which
AXI becomes the user's primary operating environment for governed
knowledge work.

This posture shall be progressive.

AXI shall not require users to manually reorganize the full corpus
before providing governed value.

Operational value may begin through governed discovery, inventory,
classification, duplicate review, metadata enrichment, canonization,
pack derivation, or search improvement before full migration is
complete.

The future governed workspace shall support domains including:

- business
- organizations
- career
- employment
- projects
- research
- creative work
- music
- writing
- sales
- marketing
- operations
- legal references
- financial planning
- decision support
- documentation
- knowledge
- media
- training
- reference libraries
- personal intellectual property

Repository Operationalization does not require every artifact to live
inside one physical repository or one runtime store.

It requires AXI governance to remain the controlling layer over how
those artifacts are discovered, interpreted, derived, and used.

### 9. Knowledge Expansion Pack

AXI shall support a future Operational Pack dedicated to Knowledge
Expansion.

The future Knowledge Expansion Pack shall be responsible for governed
coordination of activities such as:

- drive inventory
- repository inventory
- storage optimization
- duplicate detection
- artifact migration
- metadata generation
- archive governance
- search optimization
- canonical selection
- knowledge reconstruction

This Pack is a future governed consumer of the Knowledge Expansion
architecture.

It is not authorized by this ADR for runtime implementation, connector
implementation, indexing implementation, or storage-control execution.

### 10. Operational Pack And Presence Integration

All future Operational Packs shall derive artifacts from governed
knowledge rather than maintain independent canonical data silos.

This rule applies to future Packs including:

- Startup Pack
- Employment Pack
- Portfolio & Presence Pack
- Artist & Creator Pack
- Executive Pack
- Sales Pack
- Consulting Pack
- Organization Pack
- Nonprofit Pack
- Government Pack
- Church Pack
- Healthcare Pack

Examples of governed derived artifacts include:

- resumes
- cover letters
- executive biographies
- consulting profiles
- artist biographies
- Electronic Press Kits (`EPKs`)
- promotional materials
- media kits
- capability statements
- websites
- grant narratives
- sponsorship packages
- project portfolios
- marketing collateral

Future presence-oriented and portfolio-oriented packs shall remain
downstream consumers of governed knowledge and the already published
Presentation Services architecture.

They shall not replace `ADR-0018`, define competing presentation
governance, or create independent canons for public-facing identity
artifacts.

### 11. AI Governance Integration

Future AI-generated reasoning over expanded knowledge shall remain
subordinate to AXI governance.

The minimum governed sequence is:

1. Evidence
2. Governance Validation
3. Decision Intelligence
4. Human Review when required
5. Governed Decision

AI providers, models, and agent surfaces shall remain replaceable.

No AI provider shall become the governing authority for AXI knowledge,
canon, or decision outcomes.

This ADR does not authorize provider-specific architecture.

### 12. Implementation Boundary

This ADR authorizes:

- future milestone-specific governance for knowledge expansion
- future schemas, registers, and pack-governance publications
- roadmap and status updates that record this planning boundary
- future architectural planning for operational workspace behavior

This ADR does not authorize:

- runtime implementation
- ingestion engines
- indexing engines
- vector databases
- APIs
- persistence changes
- workflow automation
- connector implementation
- provider-specific AI architecture
- legal, tax, accounting, or regulatory advice generation

---

## Future Guidance

Future governance should proceed in the following order:

1. Complete the remaining `M22` core `ODT` schemas and registers.
2. Use the next published milestone to operationalize Knowledge
   Expansion and Repository Operationalization planning after `M22`
   reaches its repository exit condition.
3. Publish future schema-and-register governance for external artifact
   inventory, duplicate candidates, canonical selection, confidence,
   and operational packs only after the current Organization
   Intelligence baseline is sufficiently complete.
4. Keep Pack architecture downstream from governed knowledge and
   downstream from the published Presentation Services architecture.
5. Do not begin runtime or connector planning until the upstream
   knowledge-expansion governance surface exists.

---

## Non-Goals

This ADR does not approve:

- mandatory full migration before value can be realized
- a single monolithic knowledge store
- automatic canonization of discovered files
- deletion of non-canonical or superseded artifacts without governed
  historical preservation
- runtime ingest pipelines
- search infrastructure implementation
- cloud-drive connector implementation
- AI-provider lock-in
- independent Pack-owned systems of record

---

## Related

- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/ADR/ADR-0016_Decision_Support_Context_Governance.md`
- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/ADR/ADR-0018_Presentation_Services_Governance.md`
- `Governance/ADR/ADR-0019_Organization_Intelligence_and_Core_ODT_Schema_Governance.md`
- `Governance/WorkQueue/M22-Core-Organizational-Digital-Twin-and-Knowledge-Object-Schemas.md`
- `Governance/WorkQueue/M23-Knowledge-Expansion-and-Repository-Operationalization-Planning.md`
- `Governance/Capabilities/CAPABILITY_REGISTER.md`
- `Governance/Decisions/DECISION_REGISTER.md`
- `Governance/Publications/DIAGRAM_REGISTER.md`
- `Governance/Publications/Diagrams/DGM-002_Repository_Stewardship_Lifecycle_Map.md`
- `Governance/Publications/Diagrams/DGM-007_Presentation_Services_Topology.md`
- `Governance/Publications/Diagrams/DGM-008_Organization_Intelligence_ODT_Foundation_Map.md`
- `Governance/Publications/Diagrams/DGM-009_Knowledge_Expansion_and_Operationalization_Topology.md`
- `Governance/Roadmap/AXI_Roadmap_v1.0.md`
