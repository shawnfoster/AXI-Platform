# AXI Runtime API

`Runtime/API/` implements the governed `M18 Runtime API` boundary.

The API:

- validates operation payloads against `AXI-SCH-014`
- reuses the published Runtime CLI and upstream Plugin Loader,
  Application Registry, Engine Registry, and Pipeline Runtime behavior
- exposes deterministic inspection, validation, execution, and pipeline
  lifecycle control
- preserves the in-process local programmatic boundary governed by
  `ADR-0013`

The implementation does not introduce:

- a new runtime orchestration layer
- networking or server infrastructure
- persisted runtime sessions
- any post-`M18` functionality
