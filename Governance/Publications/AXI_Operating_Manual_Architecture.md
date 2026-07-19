# AXI Operating Manual Architecture

**Publication ID:** `PUB-002`
**Publication Type:** `Operating Manual`
**Version:** `1.0.0`
**Status:** `Approved`
**Lifecycle State:** `Active`
**Owner:** `AXI Platform Governance`
**Review Cycle:** `Semiannual and change-triggered`
**Approval Authority:** `AXI Platform Governance`
**Audit Date:** `2026-07-19`
**Related Diagram:** `DGM-005`

---

# Purpose

Publish the architecture and canonical table of contents for the AXI
Operating Manual.

The Operating Manual is the governed operational interpretation layer of
the platform.

It explains how approved architecture, governance, runtime foundations,
and knowledge systems are used together without overriding the
authoritative ADRs, schemas, standards, or constitutional rules.

---

# Architectural Role

The Operating Manual:

- consolidates governed operating knowledge
- organizes operational interpretation into durable volumes
- ties platform use back to approved architecture
- provides a controlled surface for future operational detail
- remains subordinate to constitutional, architectural, and schema
  authority

The Operating Manual shall not:

- invent runtime capabilities
- redefine decision architecture
- replace ADRs, schemas, or standards
- assert compliance, approval, or automation that is not already
  governed

---

# Volume Topology

| Volume | Title | Purpose | Governing Publications | Relationship to the Platform |
| --- | --- | --- | --- | --- |
| I | Foundations | Publish the constitutional basis, platform mission, glossary, architectural principles, and repository authority model. | Constitution, `ADR-0014`, `ADR-0017` | Anchors every operational interpretation to the approved platform baseline. |
| II | Platform Operations | Explain operation of the implemented runtime foundation through `M18`, repository controls, release discipline, and operator responsibilities. | `Governance/RuntimeRoadmap.md`, `Governance/DependencyMatrix.md`, runtime ADRs, `ADR-0017` | Describes how the current runtime substrate is operated without claiming later runtime implementation. |
| III | Decision Intelligence | Explain the canonical decision lifecycle, decision object model, capabilities, engine layering, and human approval boundary. | `ADR-0014`, `DECISION_REGISTER`, `CAPABILITY_REGISTER` | Connects platform operations to AXI's decision-centric mission. |
| IV | Knowledge Management | Explain AXI Methodology, External Knowledge, Organizational Knowledge, Learned Knowledge, Governed Expertise, and evidence handling. | `ADR-0014`, `ADR-0015`, `ADR-0017` | Preserves strict knowledge separation and provenance. |
| V | Repository Stewardship | Explain information lifecycle, repository health, archival, review and quarantine, and publication governance. | `ADR-0015`, `ADR-0017` | Governs repository health as an operational discipline rather than cleanup work. |
| VI | Organization Intelligence | Explain the Organizational Digital Twin, operating context, regulatory knowledge, readiness, and future organization-domain schemas. | `ADR-0016`, future ODT schemas | Connects decisions to real organizational conditions before execution planning. |
| VII | Expertise Engineering | Explain lessons, expertise lifecycle, knowledge improvement, and field-to-platform feedback loops. | `ADR-0014`, `CAPABILITY_REGISTER`, future expertise governance | Converts outcomes into governed expertise and Digital Twin updates. |
| VIII | Governance | Explain ADR practice, standards, policies, schemas, registers, approval authorities, and exception handling. | Constitution, ADR set, standards set | Keeps operators aligned to the constitutional and architectural control model. |
| IX | Administration | Explain administration, release coordination, freeze handling, repository health reviews, and publication stewardship. | `Governance/Freezes/`, `Governance/Source_Control/`, `ADR-0015`, `ADR-0017` | Provides the controlled administrative layer for maintaining AXI as a governed platform. |
| X | Reference | Publish indexes, directory standards, naming and ID references when approved, schema references, checklists, and diagram references. | registers, standards, schemas, checklists | Supplies the stable lookup surface that supports the rest of the manual. |

---

# Canonical Table of Contents

## Volume I — Foundations

1. Repository Authority
2. Constitutional Principles
3. Decision Intelligence Mission
4. Platform Terminology and Glossary
5. Architectural Reading Order

## Volume II — Platform Operations

1. Runtime Foundation Through `M18`
2. Service, Engine, Pipeline, CLI, and API Boundaries
3. Validation and Review Discipline
4. Release, Freeze, and Handoff Practices
5. Operational Responsibilities

## Volume III — Decision Intelligence

1. Canonical Decision Lifecycle
2. Canonical Platform Objects
3. Capability Map
4. Engine Layering
5. Human Approval and Execution Boundaries

## Volume IV — Knowledge Management

1. Knowledge Architecture Separation
2. Evidence and Provenance Handling
3. Organizational Knowledge
4. Learned Knowledge and Lessons
5. Governed Expertise

## Volume V — Repository Stewardship

1. Information Lifecycle
2. Repository Health Model
3. Archive Governance
4. Review and Quarantine Governance
5. Publication and Diagram Governance

## Volume VI — Organization Intelligence

1. Organizational Digital Twin
2. Operating Context
3. Regulatory Knowledge
4. Readiness Framework
5. Decision Support Boundaries

## Volume VII — Expertise Engineering

1. Expertise Lifecycle
2. Lesson Conversion
3. Knowledge Improvement
4. Playbook Feedback
5. Training and Academy Inputs

## Volume VIII — Governance

1. ADR and Boundary Governance
2. Standards and Policies
3. Schemas and Registers
4. Review Authorities
5. Exceptions and Escalation

## Volume IX — Administration

1. Administrative Roles
2. Publication Stewardship
3. Repository Health Reviews
4. Freeze and Release Operations
5. Operational Escalation

## Volume X — Reference

1. Canonical Registers
2. Schema Reference
3. Checklist Reference
4. Diagram Reference
5. Indexes and Lookup Tables

---

# Cross-Reference Rules

- Every volume shall reference the governing ADRs, schemas, and
  standards it operationalizes.
- Every volume shall identify which controlled publications it depends
  upon and which later publications may derive from it.
- Every volume shall identify whether a canonical diagram is required
  for publication completeness.
- No operating-manual section may supersede a constitutional or
  architectural control artifact.

---

# Related

- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/Publications/PUBLICATION_REGISTER.md`
- `Governance/Publications/DIAGRAM_REGISTER.md`
- `Governance/Publications/Diagrams/DGM-005_Operating_Manual_Volume_Map.md`
