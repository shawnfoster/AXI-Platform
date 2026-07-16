# WORK QUEUE TEMPLATE

**Work Item:** M#
**Title:**
**Status:** Approved
**Priority:**
**Owner:** AXI Platform

---

# Objective

Describe the capability or subsystem to be implemented.

State the intended business and technical outcome.

---

# Background

Explain why this work exists.

Describe where it fits within the AXI Platform.

---

# Existing Components

List repository components that should be reused.

Example:

- Runtime/Registry
- Runtime/ObjectRegistry
- Runtime/CapabilityRegistry

Do not duplicate existing functionality.

---

# Scope

Describe exactly what this work item includes.

List expected directories and files.

Example:

```
Runtime/
    ExampleSubsystem/
```

Expected files:

- __init__.py
- registry.py
- model.py
- README.md

---

# Functional Requirements

List the required capabilities.

Example:

- register()
- unregister()
- lookup()
- update()
- validate()

Be explicit about required behavior.

---

# Dependencies

List required integrations.

Examples:

- BaseRegistry
- PlatformObject
- Capability Registry

No circular dependencies may be introduced.

---

# Constraints

Implementation shall:

- Preserve architecture.
- Preserve contracts.
- Preserve schemas.
- Preserve standards.
- Preserve provenance.
- Preserve traceability.
- Preserve reproducibility.

Architecture changes require an approved ADR.

---

# Validation

Describe validation requirements.

Examples:

- Reject duplicate identifiers.
- Validate metadata.
- Preserve lifecycle state.
- Raise existing platform exceptions.

---

# Tests

Create or update automated tests covering:

- Successful operation
- Failure scenarios
- Validation
- Edge cases
- Regression protection

All existing tests must continue to pass.

---

# Deliverables

Expected outputs.

Examples:

- Runtime implementation
- Documentation updates
- Unit tests
- Supporting artifacts

---

# Acceptance Criteria

Implementation is complete when:

✓ Functional requirements satisfied

✓ Validation passes

✓ Existing tests pass

✓ New tests pass

✓ No unrelated files modified

✓ Existing architecture preserved

---

# Definition of Done

Before completion:

- Compile successfully.
- Execute all required tests.
- Preserve governance.
- Preserve contracts.
- Preserve schemas.
- Preserve traceability.
- Preserve provenance.

Produce one logical Git commit.

Stop after completion.

---

# Suggested Commit Message

AI-XXX: <Describe completed work>