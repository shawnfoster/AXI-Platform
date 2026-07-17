from __future__ import annotations

import pytest

from Runtime.ApplicationRegistry import Application, ApplicationRegistry
from Runtime.CLI import RuntimeCLI
from Runtime.EngineRegistry import Engine, EngineRegistry
from Runtime.EventBus import EventBus, Subscriber
from Runtime.Pipeline import Pipeline, PipelineStage
from Runtime.PluginLoader import PluginLoader
from Runtime.exceptions import RegistryError


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


def build_application(i: int) -> Application:
    return Application(
        object_id=f"OBJ-{i:06d}",
        namespace="AXI-APP",
        object_type="Application",
        name=f"Application {i}",
        description=f"Application description {i}",
        version="1.0.0",
        status="Approved",
        owner="Platform",
        provenance={"created_by": "test"},
        metadata={
            "lifecycle_state": "Registered",
            "runtime": "local",
        },
    )


def build_manifest(plugin_id: str) -> dict[str, object]:
    return {
        "plugin_id": plugin_id,
        "name": f"Plugin {plugin_id}",
        "version": "1.0.0",
        "author": "AXI Platform",
        "description": f"Runtime plugin {plugin_id}",
        "capabilities": [],
        "dependencies": [],
        "lifecycle_state": "Discovered",
    }


def build_stage(
    stage_id: str,
    *,
    execution_order: int,
    engine: str,
    dependencies: list[str] | None = None,
) -> PipelineStage:
    return PipelineStage(
        stage_id=stage_id,
        name=f"Stage {stage_id}",
        description=f"Pipeline stage {stage_id}",
        execution_order=execution_order,
        dependencies=dependencies or [],
        engine=engine,
        metadata={"kind": "test"},
    )


def build_runtime_context() -> dict[str, object]:
    plugin_a = build_manifest("plugin-beta")
    plugin_b = build_manifest("plugin-alpha")
    application_a = build_application(2).to_dict()
    application_b = build_application(1).to_dict()
    engine_a = build_engine(2).to_dict()
    engine_b = build_engine(1).to_dict()
    stage_b = build_stage(
        "stage-b",
        execution_order=2,
        engine="OBJ-000002",
        dependencies=["stage-a"],
    ).to_dict()
    stage_a = build_stage(
        "stage-a",
        execution_order=1,
        engine="OBJ-000001",
    ).to_dict()

    return {
        "plugins": [plugin_a, plugin_b],
        "applications": [application_a, application_b],
        "engines": [engine_a, engine_b],
        "pipeline": {
            "stages": [stage_b, stage_a],
            "runtime_state": "Initialized",
            "metadata": {"runtime": "local"},
        },
    }


def build_live_cli() -> tuple[RuntimeCLI, Pipeline]:
    event_bus = EventBus()
    plugin_loader = PluginLoader(event_bus=event_bus)
    plugin_loader.load_plugin(build_manifest("plugin-runtime"))
    application_registry = ApplicationRegistry(
        plugin_loader=plugin_loader,
        event_bus=event_bus,
    )
    application_registry.register_application(build_application(600))
    engine_registry = EngineRegistry(
        plugin_loader=plugin_loader,
        application_registry=application_registry,
        event_bus=event_bus,
    )
    engine_registry.register_engine(build_engine(1))
    engine_registry.register_engine(build_engine(2))
    pipeline = Pipeline(
        plugin_loader=plugin_loader,
        application_registry=application_registry,
        engine_registry=engine_registry,
        event_bus=event_bus,
        metadata={"runtime": "local"},
    )
    pipeline.register_stage(
        build_stage(
            "stage-b",
            execution_order=2,
            engine="OBJ-000002",
            dependencies=["stage-a"],
        )
    )
    pipeline.register_stage(
        build_stage(
            "stage-a",
            execution_order=1,
            engine="OBJ-000001",
        )
    )

    return (
        RuntimeCLI(
            plugin_loader=plugin_loader,
            application_registry=application_registry,
            engine_registry=engine_registry,
            pipeline=pipeline,
        ),
        pipeline,
    )


def test_runtime_cli_inspect_targets_are_deterministic() -> None:
    cli = RuntimeCLI()
    runtime_context = build_runtime_context()

    plugins = cli.run(
        {
            "command": "inspect",
            "target": "plugins",
            "runtime_context": runtime_context,
        }
    )
    applications = cli.run(
        {
            "command": "inspect",
            "target": "applications",
            "runtime_context": runtime_context,
        }
    )
    engines = cli.run(
        {
            "command": "inspect",
            "target": "engines",
            "runtime_context": runtime_context,
        }
    )
    stages = cli.run(
        {
            "command": "inspect",
            "target": "stages",
            "runtime_context": runtime_context,
        }
    )
    runtime_state = cli.run(
        {
            "command": "inspect",
            "target": "runtime",
            "runtime_context": runtime_context,
        }
    )

    assert [item["plugin_id"] for item in plugins.payload["items"]] == [
        "plugin-alpha",
        "plugin-beta",
    ]
    assert [
        item["application_id"] for item in applications.payload["items"]
    ] == [
        "OBJ-000001",
        "OBJ-000002",
    ]
    assert [item["engine_id"] for item in engines.payload["items"]] == [
        "OBJ-000001",
        "OBJ-000002",
    ]
    assert [item["stage_id"] for item in stages.payload["items"]] == [
        "stage-a",
        "stage-b",
    ]
    assert runtime_state.payload["runtime"]["runtime_state"] == "Initialized"


def test_runtime_cli_validate_pipeline_returns_results_and_snapshot() -> None:
    cli = RuntimeCLI()
    result = cli.run(
        {
            "command": "validate",
            "runtime_context": build_runtime_context(),
        }
    )

    assert result.command == "validate"
    assert result.status == "ok"
    assert result.payload["pipeline"]["runtime_state"] == "Ready"
    assert all(
        validation_result["status"] == "valid"
        for validation_result in result.payload["results"]
    )


def test_runtime_cli_execute_pipeline_returns_ordered_execution_records() -> None:
    cli = RuntimeCLI()
    result = cli.run(
        {
            "command": "execute",
            "runtime_context": build_runtime_context(),
        }
    )

    assert [execution["stage_id"] for execution in result.payload["executions"]] == [
        "stage-a",
        "stage-b",
    ]
    assert result.payload["pipeline"]["runtime_state"] == "Completed"


def test_runtime_cli_execute_stage_runs_dependency_closure() -> None:
    runtime_context = build_runtime_context()
    runtime_context["engines"].append(build_engine(3).to_dict())
    runtime_context["pipeline"]["stages"].append(
        build_stage(
            "stage-c",
            execution_order=3,
            engine="OBJ-000003",
            dependencies=["stage-b"],
        ).to_dict()
    )
    cli = RuntimeCLI()

    result = cli.run(
        {
            "command": "execute-stage",
            "stage_id": "stage-b",
            "runtime_context": runtime_context,
        }
    )

    assert [execution["stage_id"] for execution in result.payload["executions"]] == [
        "stage-a",
        "stage-b",
    ]
    assert result.payload["pipeline"]["runtime_state"] == "Completed"


def test_runtime_cli_pause_and_resume_preserve_pipeline_lifecycle() -> None:
    cli, pipeline = build_live_cli()
    paused = {"value": False}

    pipeline._event_bus.subscribe(
        Subscriber(
            subscriber_id="SUB-CLI-PAUSE",
            event_types=("pipeline.stage.started",),
            handler=lambda event: (
                cli.run({"command": "pause"})
                if not paused["value"]
                else None
            ),
        )
    )

    def mark_paused(event) -> None:
        paused["value"] = True

    pipeline._event_bus.subscribe(
        Subscriber(
            subscriber_id="SUB-CLI-PAUSED",
            event_types=("pipeline.paused",),
            handler=mark_paused,
        )
    )

    execute_result = cli.run({"command": "execute"})

    assert execute_result.payload["pipeline"]["runtime_state"] == "Paused"
    assert execute_result.payload["executions"][0]["status"] == "Paused"
    assert pipeline.runtime_state == "Paused"

    resume_result = cli.run({"command": "resume"})

    assert resume_result.payload["runtime_state"] == "Completed"
    assert pipeline.runtime_state == "Completed"


def test_runtime_cli_stop_preserves_pipeline_cancellation_behavior() -> None:
    cli, pipeline = build_live_cli()
    stopped = {"value": False}

    def stop_on_first_stage(event) -> None:
        if stopped["value"]:
            return

        stopped["value"] = True
        cli.run({"command": "stop"})

    pipeline._event_bus.subscribe(
        Subscriber(
            subscriber_id="SUB-CLI-STOP",
            event_types=("pipeline.stage.started",),
            handler=stop_on_first_stage,
        )
    )

    result = cli.run({"command": "execute"})

    assert result.payload["pipeline"]["runtime_state"] == "Cancelled"
    assert result.payload["executions"][0]["status"] == "Cancelled"
    assert pipeline.runtime_state == "Cancelled"


def test_runtime_cli_rejects_invalid_commands_and_propagates_runtime_errors() -> None:
    cli = RuntimeCLI()

    with pytest.raises(RegistryError):
        cli.run({"command": "inspect"})

    with pytest.raises(RegistryError):
        cli.run(
            {
                "command": "execute-stage",
                "stage_id": "",
                "runtime_context": build_runtime_context(),
            }
        )

    with pytest.raises(RegistryError):
        cli.run(
            {
                "command": "execute",
                "runtime_context": {
                    "pipeline": {
                        "stages": [
                            build_stage(
                                "stage-a",
                                execution_order=1,
                                engine="OBJ-999999",
                            ).to_dict()
                        ],
                        "runtime_state": "Initialized",
                        "metadata": {},
                    }
                },
            }
        )
