AXI Pipeline Runtime
====================

The Pipeline Runtime implements the governed `M16` orchestration
boundary for deterministic stage execution.

Published runtime APIs:

- `register_stage()`
- `unregister_stage()`
- `execute()`
- `execute_stage()`
- `validate_pipeline()`
- `list_stages()`
- `pause()`
- `resume()`
- `stop()`

The runtime:

- preserves deterministic execution order
- validates pipeline definitions against published governance
- resolves stage dependencies before execution
- starts and stops registered engines through `EngineRegistry`
- publishes lifecycle events through `EventBus`
