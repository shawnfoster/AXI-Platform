# ADR-0021 — Establish Constitutional Transition Gate Governance

## Status

Accepted

---

## Purpose

Define the architectural governance required to control major AXI phase
transitions through explicit repository-evidence gates rather than
conversation context, inferred completion, or implied readiness.

This ADR publishes the governing architecture for:

- Constitutional Transition Gates as a first-class governance artifact
- repository-evidence validation for major constitutional transitions
- closed-by-default gate behavior
- transition authorization boundaries
- synchronization rules between gate state and repository status
  surfaces

---

## Repository Evidence

The repository already publishes the following relevant evidence:

- `ADR-0014` through `ADR-0020` establish AXI's current constitutional,
  architectural, publication, presentation, Organization
  Intelligence, and Knowledge Expansion governance baselines.
- `ADR-0017` publishes the canonical publication hierarchy, traceability
  rules, and approval model for governed publication artifacts.
- `Governance/Roadmap/AXI_Roadmap_v1.0.md` already uses entry-gate and
  exit-gate language for roadmap phases, but it does not yet publish
  Constitutional Transition Gates as a first-class artifact family.
- `README.md` and `CODEX_HANDOFF.md` publish repository state, active
  milestone, and next planned milestone evidence.
- `M22` publishes the current active governance-only milestone, while
  `M23` is published as the next planned governance-only milestone.

Before publication of this ADR, the repository does not publish:

- a constitutional artifact family dedicated to phase-transition
  verification
- a canonical rule that major phase transitions remain closed until
  repository evidence explicitly satisfies every required criterion
- a governed repository location and identifier pattern for transition
  gates

---

## Architectural Policy

Adopt the following Constitutional Transition Gate governance baseline.

### 1. First-Class Governance Artifact

Constitutional Transition Gates are a first-class AXI governance
artifact family.

Their purpose is to determine whether AXI may transition between major
constitutional phases, milestone states, or repository operating
postures.

Transition-gate artifacts are governed publications and shall remain
subject to the publication-governance controls established by
`ADR-0017`.

### 2. Repository-Evidence Authority

Transition Gates shall evaluate repository evidence only.

Conversation history, intent, recommendation, or memory shall never
satisfy a gate.

If repository evidence conflicts with conversational claims, the
repository governs.

### 3. Closed-By-Default Rule

Every Constitutional Transition Gate is closed by default.

A gate becomes satisfied only when every required criterion passes
based on published repository evidence.

Partial completion, future intent, placeholder files, or inferred
readiness shall not open a gate.

### 4. Identifier And Location Model

Constitutional Transition Gates shall use the identifier pattern
`CTG-###`.

They shall be published in:

`Governance/TransitionGates/`

Each Transition Gate shall also receive a governed publication
identifier through `PUBLICATION_REGISTER`.

### 5. Required Gate Content

Every Constitutional Transition Gate shall preserve, at minimum:

- gate identifier
- publication identifier
- objective
- source phase or state
- target transition or authorization
- explicit repository evidence criteria
- validation procedure
- current evaluation outcome
- deficiency record when not satisfied
- authorization boundary upon success

Transition Gates may include additional evidence detail when required,
but they shall not omit the fields above.

### 6. Relationship Rules

Transition Gates do not replace ADRs, work items, roadmap phases,
publication registers, or status artifacts.

They evaluate whether those governed artifacts collectively support a
transition claim.

Transition Gates shall remain subordinate to the Constitution, accepted
ADRs, approved schemas, approved work items, and published repository
status evidence they reference.

### 7. Authorization Boundary

Satisfaction of a Transition Gate authorizes only the transition scope
explicitly stated by that gate.

A satisfied gate does not imply:

- runtime authorization
- implementation authorization
- operational authority beyond the published gate boundary
- bypass of later milestone, ADR, schema, contract, or human-approval
  requirements

### 8. Status Synchronization

If a gate requires milestone completion, repository status artifacts
shall remain synchronized before the gate may be satisfied.

At minimum, affected gates shall evaluate the consistency of:

- governing work items
- `README.md`
- `CODEX_HANDOFF.md`
- roadmap state
- publication/register state
- dependency evidence when the transition changes published
  dependencies

### 9. Future Transition Discipline

Future major constitutional transitions shall be governed through
Constitutional Transition Gates rather than conversational
authorization.

Later gates may govern transitions such as:

- milestone completion to validation posture
- validation posture to broader knowledge expansion
- planning completion to implementation readiness
- one operating mode to another when repository authority must remain
  explicit

---

## Non-Goals

This ADR does not approve:

- automatic gate evaluation in runtime software
- runtime implementation beyond `M18`
- operational implementation beyond approved governance
- bypass of milestone-specific acceptance criteria
- replacement of roadmap, work-queue, or publication governance

---

## Related

- `Governance/ADR/ADR-0017_Publication_and_Documentation_Governance.md`
- `Governance/ADR/ADR-0019_Organization_Intelligence_and_Core_ODT_Schema_Governance.md`
- `Governance/ADR/ADR-0020_Knowledge_Expansion_and_Repository_Operationalization_Governance.md`
- `Governance/WorkQueue/M22-Core-Organizational-Digital-Twin-and-Knowledge-Object-Schemas.md`
- `Governance/WorkQueue/M23-Knowledge-Expansion-and-Repository-Operationalization-Planning.md`
- `Governance/Schemas/AXI-SCH-022_Publication.json`
- `Governance/Publications/PUBLICATION_REGISTER.md`
- `Governance/TransitionGates/CTG-001_M22_Completion_Gate.md`
- `Governance/Roadmap/AXI_Roadmap_v1.0.md`
