from __future__ import annotations

from Runtime.API import RuntimeAPI
from Runtime.CLI import RuntimeCLI
from Runtime.EngineRegistry import Engine
from Runtime.Pipeline import PipelineStage


def build_engine(i: int) -> Engine:
    return Engine(
        object_id=f"OBJ-{i:06d}",
        namespace="AXI-ENG",
        object_type="Engine",
        name=f"Engine {i}",
        description=f"Engine description {i}",
        version="1.0.0",
        status="Approved",
        owner="Platform",
        provenance={"created_by": "test"},
        metadata={
            "lifecycle_state": "Registered",
            "runtime": "local",
        },
    )


def build_stage(
    stage_id: str,
    *,
    execution_order: int,
    engine: str,
) -> PipelineStage:
    return PipelineStage(
        stage_id=stage_id,
        name=f"Stage {stage_id}",
        description=f"Pipeline stage {stage_id}",
        execution_order=execution_order,
        engine=engine,
        metadata={"kind": "test"},
    )


def test_runtime_api_reuses_runtime_cli_for_execution() -> None:
    api = RuntimeAPI(runtime_cli=RuntimeCLI())
    result = api.invoke(
        {
            "operation": "execute",
            "runtime_context": {
                "engines": [build_engine(1).to_dict()],
                "pipeline": {
                    "stages": [
                        build_stage(
                            "stage-a",
                            execution_order=1,
                            engine="OBJ-000001",
                        ).to_dict()
                    ],
                    "runtime_state": "Initialized",
                    "metadata": {"runtime": "local"},
                },
            },
        }
    )

    assert result.operation == "execute"
    assert result.status == "ok"
    assert result.payload["pipeline"]["runtime_state"] == "Completed"


def test_runtime_api_result_serialization_uses_api_envelope() -> None:
    api = RuntimeAPI(runtime_cli=RuntimeCLI())
    result = api.invoke(
        {
            "operation": "inspect",
            "target": "runtime",
            "runtime_context": {
                "pipeline": {
                    "stages": [],
                    "runtime_state": "Initialized",
                    "metadata": {"runtime": "local"},
                },
            },
        }
    ).to_dict()

    assert result["operation"] == "inspect"
    assert result["status"] == "ok"
    assert result["payload"]["runtime"]["runtime_state"] == "Initialized"
