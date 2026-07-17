from __future__ import annotations

import json
from pathlib import Path

from Runtime.CLI import RuntimeCLI, main
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


def test_runtime_cli_main_executes_shell_command_with_context_file(
    tmp_path: Path,
    capsys,
) -> None:
    context_path = tmp_path / "runtime-context.json"
    context_path.write_text(
        json.dumps(
            {
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
            }
        ),
        encoding="utf-8",
    )

    exit_code = main(
        [
            "execute",
            "--context",
            str(context_path),
        ],
        runtime_cli=RuntimeCLI(),
    )

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["command"] == "execute"
    assert payload["status"] == "ok"
    assert payload["payload"]["pipeline"]["runtime_state"] == "Completed"
    assert captured.err == ""


def test_runtime_cli_main_reports_errors_to_stderr(
    tmp_path: Path,
    capsys,
) -> None:
    context_path = tmp_path / "invalid-context.json"
    context_path.write_text(
        json.dumps(
            {
                "pipeline": {
                    "stages": [
                        build_stage(
                            "stage-a",
                            execution_order=1,
                            engine="OBJ-999999",
                        ).to_dict()
                    ],
                    "runtime_state": "Initialized",
                    "metadata": {"runtime": "local"},
                },
            }
        ),
        encoding="utf-8",
    )

    exit_code = main(
        [
            "execute",
            "--context",
            str(context_path),
        ],
        runtime_cli=RuntimeCLI(),
    )

    captured = capsys.readouterr()
    payload = json.loads(captured.err)

    assert exit_code == 1
    assert payload["command"] == "execute"
    assert payload["status"] == "error"
    assert "failed validation" in payload["error"]
    assert captured.out == ""
