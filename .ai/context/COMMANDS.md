# AI-005 — Canonical Commands

**Version:** 1.0.0  
**Status:** Approved

---

# Purpose

This document defines the canonical commands every AI implementation agent
must use when interacting with the AXI repository.

These commands represent the approved engineering workflow.

---

# Repository Status

Check repository status:

```bash
git status
```

View recent history:

```bash
git log --oneline --decorate -10
```

List tags:

```bash
git tag
```

---

# Runtime Validation

Compile runtime:

```bash
python3 -m compileall Runtime
```

Compile engines:

```bash
python3 -m compileall Engines
```

---

# Unit Tests

Run runtime tests:

```bash
python3 -m pytest Tests/Runtime -v
```

Run integration tests:

```bash
python3 -m pytest Tests/Integration -v
```

Run full test suite:

```bash
pytest
```

---

# Git Workflow

Review changes:

```bash
git diff
```

Stage changes:

```bash
git add <files>
```

Commit:

```bash
git commit -m "<message>"
```

Create milestone tag:

```bash
git tag <tag>
```

---

# Required Validation

Every implementation must complete:

- Successful compilation
- Successful tests
- Clean git status
- Documentation updates

---

# Completion Checklist

Before stopping:

- Runtime compiles
- Tests pass
- Work Queue updated
- Documentation updated
- One logical commit
- Repository clean

---

# Engineering Rule

Never leave the repository in a partially validated state.

---

End of Document