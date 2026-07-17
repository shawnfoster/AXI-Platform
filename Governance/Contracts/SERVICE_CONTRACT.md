# AXI Service Contract

**Version:** 1.0.0
**Status:** Approved
**Authority:** AXI Platform Governance

---

# Purpose

Define the current runtime contract for AXI services and the Service
Registry.

This contract is derived from the implemented repository behavior in:

- `Runtime/ServiceRegistry/service.py`
- `Runtime/ServiceRegistry/registry.py`
- `Governance/WorkQueue/M9-Service-Registry.md`
- `Governance/Schemas/AXI-SCH-007_Platform_Object.json`

---

# Repository Evidence

The repository currently publishes the following service-runtime
evidence:

- `Service` subclasses `PlatformObject`.
- `Service.service_id` returns `object_id`.
- `Service.lifecycle_state` reads and writes
  `metadata["lifecycle_state"]`.
- `ServiceRegistry.register()` accepts only `Service` instances.
- `ServiceRegistry.register()` rejects services whose `namespace` is not
  `AXI-SVC`.
- `ServiceRegistry.register()` rejects services whose `object_type` is
  not `Service`.
- `ServiceRegistry.register()` rejects empty metadata.
- `ServiceRegistry.register()` rejects missing or empty
  `lifecycle_state`.
- `ServiceRegistry.register()` rejects unresolved capability references
  when a `CapabilityRegistry` is present.
- `ServiceRegistry.resolve_service()` raises `ObjectNotFoundError` for a
  missing identifier.
- `ServiceRegistry.list_services()` returns deterministic identifier
  order.
- `M9 Service Registry` requires registration, lookup, removal,
  duplicate detection, updates, and validation failures to be tested.

---

# Scope

This contract applies to:

- `Service` runtime objects
- `ServiceRegistry`
- future validation of service registrations

`AXI-SCH-007 Platform Object` is relevant because `Service` inherits
`PlatformObject`, but the current runtime does not perform full JSON
Schema validation for services.

---

# Contract Statements

A conforming AXI runtime service shall preserve the repository-backed
runtime rules below:

- namespace `AXI-SVC`
- object type `Service`
- `service_id` exposed through `object_id`
- metadata present at registration time
- `metadata.lifecycle_state` present at registration time
- capability references resolved through `CapabilityRegistry` when one
  is present

The Service Registry shall provide the public operations already
governed by `M9`:

- `register_service(service)`
- `unregister_service(service_id)`
- `resolve_service(service_id)`
- `has_service(service_id)`
- `list_services()`
- `update_service(service)`

The registry shall preserve the following current runtime behavior:

- duplicate service identifiers are rejected
- invalid service objects are rejected
- missing metadata is rejected
- missing `lifecycle_state` metadata is rejected
- unknown capability references are rejected when capability validation
  is available
- listed services are returned in deterministic identifier order

---

# Implementation Guidance

If the validation framework validates this contract, the
repository-backed checks include:

- namespace other than `AXI-SVC`
- object type other than `Service`
- missing or empty metadata
- missing or empty `lifecycle_state`
- capability references that do not resolve

Full schema validation against `AXI-SCH-007` would require separate,
published validation behavior and is not currently runtime-enforced.

---

# Related

- `Governance/WorkQueue/M9-Service-Registry.md`
- `Governance/Schemas/AXI-SCH-007_Platform_Object.json`
- `Runtime/ServiceRegistry/service.py`
- `Runtime/ServiceRegistry/registry.py`
