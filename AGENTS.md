# AXI Agent Instructions

Current Platform Release

AXI-Platform-v2.1

---

## Repository Authority

The repository is the authoritative source of truth.

Do not rely on conversational context when repository artifacts exist.

---

## Mandatory Startup

Before writing or modifying code:

1. Read `.ai/START_HERE.md`
2. Complete the startup sequence.
3. Read the active Work Queue item in `Governance/WorkQueue/`.
4. Review applicable ADRs and Schemas.
5. Follow all AI governance publications.

---

## Engineering Rules

- Implement exactly one Work Queue item.
- Preserve architecture.
- Preserve contracts.
- Preserve schemas.
- Preserve provenance.
- Run all required validation.
- Produce one logical commit.
- Leave the repository in a clean state.
- Stop after completing the assigned work.

---

## Architecture

Architecture changes require an ADR.

Do not introduce competing implementations or bypass approved governance.

---

## Validation

Before completion:

- Runtime compiles.
- Tests pass.
- Documentation updated if required.
- `git status` is clean.

---

## Success

A successful implementation is:

- Governed
- Traceable
- Tested
- Documented
- Reproducible