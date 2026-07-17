# AXI Runtime CLI

`Runtime/CLI/` implements the governed `M17 Runtime CLI` boundary.

The CLI:

- validates command payloads against `AXI-SCH-013`
- reuses published Plugin Loader, Application Registry, Engine Registry,
  and Pipeline Runtime behavior
- exposes deterministic inspection, validation, execution, and pipeline
  lifecycle control
- preserves the in-process local command boundary governed by
  `ADR-0012`

The implementation does not introduce:

- a new runtime orchestration layer
- remote or cross-process execution control
- persisted runtime sessions
- any `M18 Runtime API` behavior
