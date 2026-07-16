# AI-007 — Coding Standard

**Version:** 1.0.0
**Status:** Approved

---

# Purpose

This document defines the minimum coding standards for all AI-generated
implementation within the AXI Platform.

---

# Design Principles

Code shall be:

- Simple
- Readable
- Deterministic
- Reusable
- Testable
- Documented

Prefer clarity over cleverness.

---

# Naming

Use descriptive names.

Avoid abbreviations unless they are established platform terminology.

Examples:

Good

ObjectRegistry
CapabilityRegistry
PlatformObject

Avoid

ObjMgr
CapSys
DataThing

---

# Single Responsibility

Classes should have one responsibility.

Functions should perform one task.

Large functions should be decomposed.

---

# Type Hints

Use Python type hints whenever practical.

---

# Documentation

Public classes and methods require docstrings.

Complex logic requires explanatory comments.

Comments should explain *why*, not *what*.

---

# Errors

Raise meaningful exceptions.

Never silently ignore failures.

---

# Testing

Every new capability should include appropriate automated tests.

---

# Imports

Prefer explicit imports.

Avoid wildcard imports.

---

# Dependencies

Minimize external dependencies.

Prefer the Python standard library where practical.

---

# Engineering Goal

Readable code is preferred over clever code.

Maintainability is preferred over brevity.

---

End of Document