# AI-008 — Review Checklist

**Version:** 1.0.0
**Status:** Approved

---

# Pre-Commit Review

Before every commit verify:

## Governance

- Constitution followed
- Development Rules followed
- Work Queue item completed

---

## Architecture

- Architecture preserved
- No duplicate functionality
- No contract violations
- No schema violations

---

## Runtime

- Runtime compiles

---

## Testing

- Relevant tests pass
- No failing tests introduced

---

## Documentation

- Documentation updated
- ADR updated if architecture changed
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