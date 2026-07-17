from __future__ import annotations

import pytest

from Runtime.ApplicationRegistry import Application, ApplicationRegistry
from Runtime.EngineRegistry import Engine, EngineRegistry
from Runtime.EventBus import Event, EventBus, Subscriber
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


def build_engine_registry(*engine_numbers: int) -> EngineRegistry:
    registry = EngineRegistry()

    for engine_number in engine_numbers:
        registry.register_engine(build_engine(engine_number))

    return registry


def test_pipeline_registers_lists_and_serializes_stages() -> None:
    pipeline = Pipeline(
        engine_registry=build_engine_registry(1, 2),
        metadata={"runtime": "local"},
    )
    stage_b = build_stage(
        "stage-b",
        execution_order=2,
        engine="OBJ-000002",
    )
    stage_a = build_stage(
        "stage-a",
        execution_order=1,
        engine="OBJ-000001",
    )

    pipeline.register_stage(stage_b)
    pipeline.register_stage(stage_a)

    restored = PipelineStage.from_dict(stage_a.to_dict())

    assert [stage.stage_id for stage in pipeline.list_stages()] == [
        "stage-a",
        "stage-b",
    ]
    assert restored.to_dict() == stage_a.to_dict()
    assert pipeline.runtime_state == "Initialized"


def test_pipeline_executes_in_dependency_safe_deterministic_order_and_publishes_events() -> None:
    event_bus = EventBus()
    received: list[Event] = []
    plugin_loader = PluginLoader()
    plugin_loader.load_plugin(build_manifest("plugin-runtime"))
    application_registry = ApplicationRegistry()
    application_registry.register_application(build_application(600))
    engine_registry = build_engine_registry(1, 2)
    pipeline = Pipeline(
        engine_registry=engine_registry,
        application_registry=application_registry,
        plugin_loader=plugin_loader,
        event_bus=event_bus,
        metadata={"runtime": "local"},
    )

    event_bus.subscribe(
        Subscriber(
            subscriber_id="SUB-PIPELINE",
            event_types=(
                "pipeline.validated",
                "pipeline.started",
                "pipeline.stage.started",
                "pipeline.stage.completed",
                "pipeline.completed",
            ),
            handler=lambda event: received.append(event),
        )
    )

    pipeline.register_stage(
        build_stage(
            "stage-b",
            execution_order=1,
            engine="OBJ-000002",
            dependencies=["stage-a"],
        )
    )
    pipeline.register_stage(
        build_stage(
            "stage-a",
            execution_order=2,
            engine="OBJ-000001",
        )
    )

    executions = pipeline.execute()

    assert [execution.stage_id for execution in executions] == [
        "stage-a",
        "stage-b",
    ]
    assert pipeline.runtime_state == "Completed"
    assert {
        stage.stage_id: stage.status for stage in pipeline.list_stages()
    } == {
        "stage-a": "Completed",
        "stage-b": "Completed",
    }
    assert engine_registry.lookup_engine("OBJ-000001").lifecycle_state == "Stopped"
    assert engine_registry.lookup_engine("OBJ-000002").lifecycle_state == "Stopped"
    assert [event.event_type for event in received] == [
        "pipeline.validated",
        "pipeline.started",
        "pipeline.stage.started",
        "pipeline.stage.completed",
        "pipeline.stage.started",
        "pipeline.stage.completed",
        "pipeline.completed",
    ]
    assert received[0].payload["loaded_plugins"] == ("plugin-runtime",)
    assert received[0].payload["registered_applications"] == (
        "OBJ-000600",
    )
    assert received[0].payload["registered_engines"] == (
        "OBJ-000001",
        "OBJ-000002",
    )


def test_pipeline_register_stage_rejects_missing_engine_reference() -> None:
    pipeline = Pipeline(engine_registry=build_engine_registry(1))

    with pytest.raises(RegistryError):
        pipeline.register_stage(
            build_stage(
                "stage-missing-engine",
                execution_order=1,
                engine="OBJ-999999",
            )
        )


def test_pipeline_validation_rejects_circular_dependencies() -> None:
    pipeline = Pipeline(
        engine_registry=build_engine_registry(1, 2),
        metadata={"runtime": "local"},
    )
    pipeline.register_stage(
        build_stage(
            "stage-a",
            execution_order=1,
            engine="OBJ-000001",
            dependencies=["stage-b"],
        )
    )
    pipeline.register_stage(
        build_stage(
            "stage-b",
            execution_order=2,
            engine="OBJ-000002",
            dependencies=["stage-a"],
        )
    )

    results = pipeline.validate_pipeline()

    assert any(
        result.rule_id == "dependencies.validate"
        and result.status == "invalid"
        for result in results
    )
    assert pipeline.runtime_state == "Failed"

    with pytest.raises(RegistryError):
        pipeline.execute()


def test_pipeline_execute_stage_runs_only_required_dependency_chain() -> None:
    pipeline = Pipeline(
        engine_registry=build_engine_registry(1, 2, 3),
        metadata={"runtime": "local"},
    )
    pipeline.register_stage(
        build_stage(
            "stage-c",
            execution_order=3,
            engine="OBJ-000003",
        )
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

    executions = pipeline.execute_stage("stage-b")

    assert [execution.stage_id for execution in executions] == [
        "stage-a",
        "stage-b",
    ]
    assert pipeline.runtime_state == "Completed"
    assert {
        stage.stage_id: stage.status for stage in pipeline.list_stages()
    } == {
        "stage-a": "Completed",
        "stage-b": "Completed",
        "stage-c": "Ready",
    }


def test_pipeline_supports_pause_and_resume_via_lifecycle_events() -> None:
    event_bus = EventBus()
    received: list[Event] = []
    pipeline = Pipeline(
        engine_registry=build_engine_registry(1),
        event_bus=event_bus,
        metadata={"runtime": "local"},
    )
    pipeline.register_stage(
        build_stage(
            "stage-a",
            execution_order=1,
            engine="OBJ-000001",
        )
    )

    def pause_once(event: Event) -> None:
        if paused["value"]:
            return

        paused["value"] = True
        pipeline.pause()

    paused = {"value": False}

    event_bus.subscribe(
        Subscriber(
            subscriber_id="SUB-ZZ-PAUSE-CONTROL",
            event_types=("pipeline.stage.started",),
            handler=pause_once,
        )
    )
    event_bus.subscribe(
        Subscriber(
            subscriber_id="SUB-PAUSE-TRACE",
            event_types=(
                "pipeline.validated",
                "pipeline.started",
                "pipeline.stage.started",
                "pipeline.paused",
                "pipeline.stage.paused",
                "pipeline.resumed",
                "pipeline.stage.completed",
                "pipeline.completed",
            ),
            handler=lambda event: received.append(event),
        )
    )

    first_run = pipeline.execute()

    assert pipeline.runtime_state == "Paused"
    assert [execution.status for execution in first_run] == ["Paused"]

    resumed = pipeline.resume()

    assert [execution.stage_id for execution in resumed] == ["stage-a"]
    assert pipeline.runtime_state == "Completed"
    assert [event.event_type for event in received] == [
        "pipeline.validated",
        "pipeline.started",
        "pipeline.stage.started",
        "pipeline.paused",
        "pipeline.stage.paused",
        "pipeline.resumed",
        "pipeline.stage.started",
        "pipeline.stage.completed",
        "pipeline.completed",
    ]


def test_pipeline_supports_stop_during_execution() -> None:
    event_bus = EventBus()
    received: list[Event] = []
    pipeline = Pipeline(
        engine_registry=build_engine_registry(1),
        event_bus=event_bus,
        metadata={"runtime": "local"},
    )
    pipeline.register_stage(
        build_stage(
            "stage-a",
            execution_order=1,
            engine="OBJ-000001",
        )
    )

    def stop_once(event: Event) -> None:
        if stopped["value"]:
            return

        stopped["value"] = True
        pipeline.stop()

    stopped = {"value": False}

    event_bus.subscribe(
        Subscriber(
            subscriber_id="SUB-ZZ-STOP-CONTROL",
            event_types=("pipeline.stage.started",),
            handler=stop_once,
        )
    )
    event_bus.subscribe(
        Subscriber(
            subscriber_id="SUB-STOP-TRACE",
            event_types=(
                "pipeline.validated",
                "pipeline.started",
                "pipeline.stage.started",
                "pipeline.stopped",
                "pipeline.stage.cancelled",
            ),
            handler=lambda event: received.append(event),
        )
    )

    executions = pipeline.execute()

    assert pipeline.runtime_state == "Cancelled"
    assert [execution.status for execution in executions] == ["Cancelled"]
    assert [event.event_type for event in received] == [
        "pipeline.validated",
        "pipeline.started",
        "pipeline.stage.started",
        "pipeline.stopped",
        "pipeline.stage.cancelled",
    ]
