# Dependency Resolver

This package provides the AXI runtime dependency model and deterministic
dependency resolver.

- `Dependency` is an immutable edge between two runtime identifiers.
- `DependencyResolver` stores dependency relationships, validates known
  runtime identifiers, resolves dependency order, detects circular
  references, and can publish narrow dependency lifecycle notifications
  through the runtime Event Bus.
