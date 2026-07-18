# AI-005 — Canonical Commands

**Version:** 1.1.0
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

# Validation Policy Reference

Select the applicable validation tier from:

`.ai/governance/DEVELOPMENT_RULES.md`

Then execute the commands required by that tier plus any stricter
task-specific governance.

---

# Documentation Validation

Check patch formatting:

```bash
git diff --check
```

Validate Markdown when a tool is available:

```bash
command -v markdownlint >/dev/null && markdownlint <files>
```

Validate links or references when a tool is available:

```bash
command -v markdown-link-check >/dev/null && markdown-link-check <files>
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

Every change must complete the validation required by the selected
validation tier in `DEVELOPMENT_RULES.md` plus any stricter published
task-specific governance.

---

# Completion Checklist

Before stopping:

- Required validation tier completed
- Applicable compile and test commands pass
- Work Queue updated when required
- Documentation updated
- One logical commit
- Repository clean

---

# Engineering Rule

Never leave the repository in a partially validated state.

---

End of Document
