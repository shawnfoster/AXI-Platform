# AI-008 — Review Checklist

**Version:** 1.2.0
**Status:** Approved

---

# Pre-Commit Review

Before every commit verify:

## Governance

- Constitution followed
- Development Rules followed
- Assigned governed objective completed

---

## Architecture

- Architecture preserved
- No duplicate functionality
- No contract violations
- No schema violations

---

## Validation

- Validation Policy followed
- Required compilation steps for the selected validation tier completed
- Required tests for the selected validation tier pass
- No failing required validation introduced

---

## Documentation

- Documentation updated
- ADR updated if architecture changed
- AI Architecture updated if `.ai/` structure or authority changed
- Schemas updated if required

---

## Git

- Clean working tree
- One logical commit
- Meaningful commit message
- Appropriate tag if milestone reached

---

## Final Question

Can another engineer understand this change without reading chat history?

If the answer is "No," improve the documentation before committing.

---

End of Document
