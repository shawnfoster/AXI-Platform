# ADR-0023 — Establish Information Governance And Knowledge Protection Governance

## Status

Accepted

---

## Purpose

Define the constitutional architecture required to govern protected
knowledge in AXI before any runtime, access-control, cybersecurity, or
secrets-management implementation is authorized.

This ADR publishes the governing architecture for:

- Information Governance as a first-class constitutional capability
- governed protection metadata for canonical `Knowledge` objects
- organization-defined information-classification frameworks
- inherited protection posture across downstream governed artifacts
- explicit boundaries between protection governance and implementation
  security controls

---

## Repository Evidence

The repository already publishes the following relevant evidence:

- `ADR-0014` establishes knowledge-domain separation, provenance,
  confidence, uncertainty, explainability, and Trust as constitutional
  decision requirements.
- `ADR-0015` governs information lifecycle, archival, imported-content
  review, risk classification, and review authority, but it does not
  publish durable protection metadata for canonical `Knowledge`
  objects.
- `ADR-0016` governs Regulatory Knowledge, jurisdiction-aware planning
  inputs, privacy and review authorities, and audit timing as adjacent
  decision-support domains rather than durable knowledge-object
  metadata.
- `ADR-0018` requires widgets to inherit the strictest constituent
  security policy from their governed data sources and object
  boundaries, but the published `Knowledge` schema does not yet define
  the upstream protection posture those renderers should inherit.
- `ADR-0019` and `M22` authorize publication of the core `ODT`
  schema-and-register baseline, including `Knowledge`, within the
  active governance-only milestone.
- `AXI-SCH-030` and `PUB-013` publish authority, provenance,
  lifecycle, dependency, and publication metadata for canonical
  `Knowledge` objects, but they do not yet govern classification,
  access posture, sharing posture, retention policy, licensing,
  copyright, privacy, jurisdiction, or audit requirements.

Before publication of this ADR, the repository does not publish:

- a constitutional capability dedicated to Information Governance and
  Knowledge Protection
- a reusable schema for governed protection metadata
- a requirement that canonical `Knowledge` objects carry first-class
  information-classification and protection metadata

---

## Architectural Policy

Adopt the following Information Governance and Knowledge Protection
baseline.

### 1. First-Class Constitutional Capability

Information Governance and Knowledge Protection is a first-class AXI
constitutional capability.

Its purpose is to govern the durable protection posture of canonical
knowledge before any runtime enforcement, automation, or access-control
implementation exists.

This capability governs information metadata, stewardship, and
inheritance boundaries.

It does not, by itself, authorize cybersecurity implementation.

### 2. Knowledge Protection Baseline

Every canonical `Knowledge` object shall preserve governed information
metadata.

That baseline is composed of:

- the existing canonical ownership field
- the existing authority metadata
- the existing provenance metadata
- the existing lifecycle metadata
- a new governed Information Governance profile

The Information Governance profile shall preserve at minimum:

- stewardship
- trust posture
- confidence posture
- classification
- access policy
- sharing policy
- retention policy
- licensing and copyright posture
- regulatory constraints
- jurisdiction
- privacy requirements
- audit requirements

### 3. Information Classification

Information Classification shall become a first-class `Knowledge`
object attribute.

Classification governance shall support organization-defined
classification frameworks rather than hardcoding one canonical label
set for all organizations.

The framework shall permit, where applicable:

- common enterprise labels such as `Public`, `Internal`,
  `Confidential`, `Restricted`, or `Highly Sensitive`
- organization-specific labels
- professional, healthcare, legal, defense, or government-authorized
  classifications when later governance requires them

This ADR governs the framework, not a single universal classification
taxonomy.

### 4. Inherited Protection Philosophy

The repository evidence supports the constitutional principle that
security is inherited governance rather than a downstream feature.

In AXI terms:

- canonical knowledge defines the upstream protection posture
- downstream publications, dashboards, widgets, visualizations, prompt
  routes, and future operational artifacts inherit the strictest
  applicable protection posture from their governed source knowledge
  and adjacent object boundaries

This inheritance model governs metadata and interpretation only.

It does not authorize runtime authentication, authorization,
encryption, cybersecurity controls, or secrets management.

### 5. Boundary Separation

Information Governance and Knowledge Protection remains distinct from
other constitutional domains.

At minimum:

- `ADR-0015` continues to own lifecycle, archival, quarantine, review
  workflow state, and imported-content risk classification.
- `ADR-0016` continues to own Regulatory Knowledge, jurisdiction-aware
  planning signals, privacy review authorities, and audit timing as
  decision-support inputs rather than durable object protection
  posture.
- `ADR-0018` continues to govern how rendered artifacts inherit from
  upstream governed data; it does not own the canonical knowledge
  protection metadata itself.
- Prompt Operations routes execution, but it shall not relax or
  override governed knowledge-protection posture.
- Constitutional Transition Gates govern phase changes, not access
  decisions or object handling rules.

### 6. Schema Boundary

AXI shall publish a reusable Information Governance Profile schema for
canonical `Knowledge` objects.

The published `Knowledge` schema shall require that profile as a
first-class field rather than relegating protection posture to free-form
metadata.

This ADR does not authorize a new standalone platform-object family for
classification or access control within `M22`.

It extends the existing `Knowledge` object boundary.

### 7. Standards Boundary

Future governance should publish narrower standards for:

- organization-defined classification schemes
- access and sharing policy normalization
- retention, licensing, privacy, and audit handling normalization

Those standards are not required to publish the minimum constitutional
baseline in this ADR because the active objective is to establish the
architectural framework, not the full cross-organization standards
catalog.

### 8. Implementation Boundary

This ADR authorizes:

- knowledge-protection metadata governance
- capability publication
- schema publication or schema extension
- register and publication updates required to keep `M22` evidence
  consistent

This ADR does not authorize:

- runtime enforcement
- authentication
- authorization
- encryption
- cybersecurity controls
- secrets management
- compliance assertion engines
- automated classification engines

---

## Future Guidance

Future governance may extend this baseline to:

1. `Expertise`, `Policy`, `Resource`, and later protected object
   families when those schemas are published.
2. organization-defined classification-scheme standards and policy
   registers.
3. downstream artifact-handling standards for publications, dashboards,
   prompts, and exports.
4. later implementation-planning milestones for governed enforcement,
   audit capture, retention execution, and access-control reuse.

Those follow-on milestones are not authorized by this ADR.

---

## Non-Goals

This ADR does not approve:

- a security implementation stack
- identity or entitlement design
- encryption architecture
- secrets vault design
- cybersecurity monitoring
- operational access review workflows
- advancement of `M23`

---

## Related

- `Governance/ADR/ADR-0014_Decision_Intelligence_Architecture.md`
- `Governance/ADR/ADR-0015_Repository_Stewardship_Governance.md`
- `Governance/ADR/ADR-0016_Decision_Support_Context_Governance.md`
- `Governance/ADR/ADR-0018_Presentation_Services_Governance.md`
- `Governance/ADR/ADR-0019_Organization_Intelligence_and_Core_ODT_Schema_Governance.md`
- `Governance/ADR/ADR-0022_Prompt_Operations_Manual_Governance.md`
- `Governance/WorkQueue/M22-Core-Organizational-Digital-Twin-and-Knowledge-Object-Schemas.md`
- `Governance/Capabilities/CAPABILITY_REGISTER.md`
- `Governance/Schemas/AXI-SCH-015_Information_Lifecycle_Record.json`
- `Governance/Schemas/AXI-SCH-020_Regulatory_Knowledge.json`
- `Governance/Schemas/AXI-SCH-030_Knowledge.json`
- `Governance/Schemas/AXI-SCH-031_Information_Governance_Profile.json`
- `Governance/Publications/AXI_Knowledge_Register.md`
- `Governance/Publications/AXI_Information_Governance_and_Knowledge_Protection_Model.md`
- `Governance/Publications/PromptOperations/AXI_Prompt_Operations_Manual.md`
- `Governance/TransitionGates/CTG-001_M22_Completion_Gate.md`
