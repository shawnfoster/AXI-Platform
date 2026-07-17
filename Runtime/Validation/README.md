AXI Validation Framework
========================

This package implements the governed M12 runtime validation framework.

Published scope
---------------

- Validates `PlatformObject` instances, service objects, and engine
  objects
- Validates metadata
- Validates published schemas listed in `SCHEMA_REGISTRY`
- Validates published contracts used by the current runtime
- Validates dependency resolver state
- Validates current runtime foundations

Current authoritative validation inputs
---------------------------------------

- `AXI-SCH-007`
- `AXI-SCH-008`
- `AXI-SCH-011`
- `REGISTER_CONTRACT`
- `SERVICE_CONTRACT`
- `ENGINE_CONTRACT`

Public APIs
-----------

- `validate()`
- `validate_object()`
- `validate_metadata()`
- `validate_schema()`
- `validate_contract()`
- `validate_dependencies()`
- `validate_runtime()`

Rule engine support is provided through:

- `Validator`
- `ValidationRule`
- immutable `ValidationResult`

Out of scope
------------

- unpublished schemas
- unpublished contracts
- pipeline runtime and future scheduling behavior beyond published
  validation inputs
