"""
AXI Platform Runtime

Pipeline Runtime

Deterministic runtime orchestration for the M16 pipeline milestone.
"""

from __future__ import annotations

from collections import deque
from collections.abc import Iterable, Mapping
from typing import Any

from Runtime.ApplicationRegistry import ApplicationRegistry
from Runtime.CapabilityRegistry import CapabilityRegistry
from Runtime.DependencyResolver import Dependency, DependencyResolver
from Runtime.EngineRegistry import EngineRegistry
from Runtime.EventBus import Event, EventBus
from Runtime.ObjectRegistry import ObjectRegistry
from Runtime.Pipeline.execution import StageExecution
from Runtime.Pipeline.runtime import (
    CANCELLED,
    COMPLETED,
    FAILED,
    INITIALIZED,
    PAUSED,
    READY,
    RUNNING,
    VALIDATING,
    can_execute,
    can_validate,
    transition_runtime,
)
from Runtime.Pipeline.stage import PipelineStage
from Runtime.PluginLoader import PluginLoader
from Runtime.Registry import BaseRegistry
from Runtime.ServiceRegistry import ServiceRegistry
from Runtime.Validation import ValidationResult, Validator
from Runtime.exceptions import DependencyError, ObjectNotFoundError, RegistryError

StageInput = PipelineStage | Mapping[str, Any]


class _PipelineDependencyResolver(DependencyResolver):
    """
    Pipeline-local dependency resolver that accepts managed stage IDs.
    """

    def __init__(
        self,
        *,
        stage_ids: Iterable[str],
        object_registry: ObjectRegistry | None = None,
        capability_registry: CapabilityRegistry | None = None,
        service_registry: ServiceRegistry | None = None,
    ) -> None:
        super().__init__(
            object_registry=object_registry,
            capability_registry=capability_registry,
            service_registry=service_registry,
        )
        self._stage_ids = set(stage_ids)

    def _identifier_exists(self, identifier: str) -> bool:
        """
        Resolve identifiers from managed stages first.
        """
        return (
            identifier in self._stage_ids
            or super()._identifier_exists(identifier)
        )


class Pipeline:
    """
    Deterministic AXI pipeline runtime.
    """

    def __init__(
        self,
        *,
        object_registry: ObjectRegistry | None = None,
        capability_registry: CapabilityRegistry | None = None,
        service_registry: ServiceRegistry | None = None,
        plugin_loader: PluginLoader | None = None,
        application_registry: ApplicationRegistry | None = None,
        engine_registry: EngineRegistry | None = None,
        event_bus: EventBus | None = None,
        validator: Validator | None = None,
        metadata: Mapping[str, Any] | None = None,
    ) -> None:
        """
        Initialize the pipeline runtime.
        """
        if metadata is not None and not isinstance(metadata, Mapping):
            raise RegistryError(
                "Invalid pipeline metadata: metadata must be a mapping"
            )

        self._stages = BaseRegistry[PipelineStage]()
        self._object_registry = object_registry
        self._capability_registry = capability_registry
        self._service_registry = service_registry
        self._plugin_loader = plugin_loader
        self._application_registry = application_registry
        self._engine_registry = engine_registry
        self._event_bus = event_bus
        self._validator = validator or Validator(
            object_registry=object_registry,
            capability_registry=capability_registry,
            service_registry=service_registry,
            event_bus=event_bus,
        )
        self._metadata = dict(metadata or {})
        self._runtime_state = INITIALIZED
        self._pending_stage_ids: deque[str] = deque()
        self._active_stage_id: str | None = None
        self._execution_history: list[StageExecution] = []
        self._last_validation_results: tuple[ValidationResult, ...] = ()

    @property
    def runtime_state(self) -> str:
        """
        Return the current published pipeline runtime state.
        """
        return self._runtime_state

    @property
    def metadata(self) -> dict[str, Any]:
        """
        Return mutable pipeline metadata.
        """
        return self._metadata

    @property
    def execution_history(self) -> tuple[StageExecution, ...]:
        """
        Return the preserved execution history.
        """
        return tuple(self._execution_history)

    @property
    def last_validation_results(self) -> tuple[ValidationResult, ...]:
        """
        Return the most recent validation results.
        """
        return self._last_validation_results

    def register_stage(self, stage: StageInput) -> PipelineStage:
        """
        Register a stage by stage identifier.
        """
        self._ensure_mutable()
        candidate = self._normalize_stage(stage)
        self._raise_for_invalid_results(
            candidate.stage_id,
            self._stage_validation_results(candidate),
        )
        self._stages.register(candidate.stage_id, candidate)
        self._reset_after_structure_change()
        self._publish_event("pipeline.stage.registered", stage=candidate)
        return candidate

    def unregister_stage(self, stage_id: str) -> None:
        """
        Remove a stage by identifier.
        """
        self._ensure_mutable()
        stage = self._stages.get(stage_id)

        if stage is None:
            return

        self._stages.unregister(stage_id)
        self._reset_after_structure_change()
        self._publish_event("pipeline.stage.unregistered", stage=stage)

    def list_stages(self) -> list[PipelineStage]:
        """
        Return stages in deterministic declared order.
        """
        return self._ordered_stage_values(self._stages.values())

    def validate_pipeline(self) -> list[ValidationResult]:
        """
        Validate the current pipeline definition.
        """
        if not can_validate(self._runtime_state):
            raise RegistryError(
                "Invalid lifecycle transition: "
                f"cannot validate pipeline from '{self._runtime_state}'"
            )

        self._runtime_state = VALIDATING
        results = self._pipeline_validation_results()
        self._last_validation_results = tuple(results)

        if self._has_invalid_results(results):
            self._runtime_state = FAILED
            self._publish_event("pipeline.validation_failed")
            return results

        self._runtime_state = READY
        for stage in self.list_stages():
            if stage.status not in {COMPLETED, CANCELLED}:
                stage.status = READY

        self._publish_event("pipeline.validated")
        return results

    def execute(self) -> list[StageExecution]:
        """
        Execute every registered stage in deterministic order.
        """
        self._prepare_new_execution()
        results = self.validate_pipeline()
        self._raise_for_invalid_results("pipeline", results)

        self._runtime_state = RUNNING
        self._pending_stage_ids = deque(self._resolve_execution_plan())
        self._publish_event("pipeline.started")
        executions = self._continue_execution()
        self._raise_for_failed_execution(executions)
        return executions

    def execute_stage(self, stage_id: str) -> list[StageExecution]:
        """
        Execute a stage and its transitive stage dependencies.
        """
        self._prepare_new_execution()
        results = self.validate_pipeline()
        self._raise_for_invalid_results(stage_id, results)
        self._require_stage(stage_id)

        self._runtime_state = RUNNING
        self._pending_stage_ids = deque(
            self._resolve_execution_plan(
                target_stage_ids=self._collect_stage_closure(stage_id)
                | {stage_id}
            )
        )
        self._publish_event("pipeline.started")
        executions = self._continue_execution()
        self._raise_for_failed_execution(executions)
        return executions

    def pause(self) -> str:
        """
        Pause an active pipeline execution.
        """
        self._runtime_state = transition_runtime(
            self._runtime_state,
            "pause",
        )

        if self._active_stage_id is not None:
            active_stage = self._stages.get(self._active_stage_id)

            if active_stage is not None and active_stage.status == RUNNING:
                active_stage.status = PAUSED

        self._publish_event("pipeline.paused")
        return self._runtime_state

    def resume(self) -> list[StageExecution]:
        """
        Resume a paused pipeline execution.
        """
        self._runtime_state = transition_runtime(
            self._runtime_state,
            "resume",
        )
        self._publish_event("pipeline.resumed")
        executions = self._continue_execution()
        self._raise_for_failed_execution(executions)
        return executions

    def stop(self) -> str:
        """
        Cancel an active or paused pipeline execution.
        """
        previous_state = self._runtime_state
        self._runtime_state = transition_runtime(
            self._runtime_state,
            "stop",
        )

        if previous_state == PAUSED:
            for stage_id in list(self._pending_stage_ids):
                stage = self._stages.get(stage_id)

                if stage is not None and stage.status == PAUSED:
                    stage.status = CANCELLED

            self._pending_stage_ids.clear()
            self._active_stage_id = None

        self._publish_event("pipeline.stopped")
        return self._runtime_state

    def to_dict(self) -> dict[str, object]:
        """
        Serialize the published pipeline schema payload.
        """
        return self._schema_payload(self.list_stages())

    def _ensure_mutable(self) -> None:
        """
        Reject structural mutation during active execution.
        """
        if self._runtime_state in {RUNNING, PAUSED}:
            raise RegistryError(
                "Invalid lifecycle transition: "
                f"cannot modify pipeline from '{self._runtime_state}'"
            )

    def _prepare_new_execution(self) -> None:
        """
        Reset transient execution state for a new execution attempt.
        """
        if not can_execute(self._runtime_state):
            raise RegistryError(
                "Invalid lifecycle transition: "
                f"cannot execute pipeline from '{self._runtime_state}'"
            )

        self._runtime_state = INITIALIZED
        self._pending_stage_ids.clear()
        self._active_stage_id = None

        for stage in self.list_stages():
            stage.status = INITIALIZED

    def _reset_after_structure_change(self) -> None:
        """
        Reset runtime state after stage registration changes.
        """
        self._runtime_state = INITIALIZED
        self._pending_stage_ids.clear()
        self._active_stage_id = None
        self._last_validation_results = ()

    def _normalize_stage(self, stage: StageInput) -> PipelineStage:
        """
        Normalize supported stage inputs.
        """
        if isinstance(stage, PipelineStage):
            return stage

        if isinstance(stage, Mapping):
            return PipelineStage.from_dict(stage)

        raise RegistryError(
            "Invalid stage registration: expected PipelineStage"
        )

    def _require_stage(self, stage_id: str) -> PipelineStage:
        """
        Resolve a registered stage.
        """
        stage = self._stages.get(stage_id)

        if stage is None:
            raise ObjectNotFoundError(
                f"Stage not found: '{stage_id}'"
            )

        return stage

    def _stage_validation_results(
        self,
        stage: PipelineStage,
    ) -> list[ValidationResult]:
        """
        Validate a single stage registration input.
        """
        results = self._validator.validate_schema(
            self._schema_payload([stage]),
            "AXI-SCH-012",
        )
        results.extend(
            self._validator.validate_metadata(
                stage.metadata,
                source=stage.stage_id,
            )
        )
        results.extend(self._engine_validation_results([stage]))
        return results

    def _pipeline_validation_results(self) -> list[ValidationResult]:
        """
        Validate the full pipeline definition.
        """
        stages = self.list_stages()
        results = self._validator.validate_contract(
            self,
            "PIPELINE_CONTRACT",
        )
        results.extend(
            self._validator.validate_metadata(
                self.metadata,
                source="Pipeline",
            )
        )
        results.extend(
            self._validator.validate_schema(
                self._schema_payload(stages),
                "AXI-SCH-012",
            )
        )

        for stage in stages:
            results.extend(
                self._validator.validate_metadata(
                    stage.metadata,
                    source=stage.stage_id,
                )
            )

        results.extend(self._engine_validation_results(stages))
        try:
            dependency_resolver = self._build_dependency_resolver(stages)
        except DependencyError as exc:
            results.append(
                self._invalid_result(
                    "dependencies.validate",
                    str(exc),
                    "Pipeline",
                )
            )
        else:
            results.extend(
                self._validator.validate_dependencies(
                    dependency_resolver
                )
            )

        try:
            self._resolve_execution_plan()
        except DependencyError as exc:
            results.append(
                self._invalid_result(
                    "pipeline.execution_order",
                    str(exc),
                    "Pipeline",
                )
            )
        else:
            results.append(
                self._valid_result(
                    "pipeline.execution_order",
                    "Pipeline execution order is deterministic",
                    "Pipeline",
                )
            )

        return results

    def _engine_validation_results(
        self,
        stages: Iterable[PipelineStage],
    ) -> list[ValidationResult]:
        """
        Validate stage engine references through the Engine Registry boundary.
        """
        stages = list(stages)

        if not stages:
            return []

        if self._engine_registry is None:
            return [
                self._invalid_result(
                    "pipeline.engine_registry",
                    "EngineRegistry integration is required for stage execution",
                    "Pipeline",
                )
            ]

        results: list[ValidationResult] = []
        validated_engines: set[str] = set()

        for stage in stages:
            if not self._engine_registry.exists(stage.engine):
                results.append(
                    self._invalid_result(
                        "pipeline.engine_registry",
                        (
                            "Stage engine reference does not resolve: "
                            f"{stage.engine}"
                        ),
                        stage.stage_id,
                    )
                )
                continue

            if stage.engine in validated_engines:
                continue

            validated_engines.add(stage.engine)
            engine = self._engine_registry.lookup_engine(stage.engine)

            if engine is None:
                results.append(
                    self._invalid_result(
                        "pipeline.engine_registry",
                        (
                            "Stage engine reference does not resolve: "
                            f"{stage.engine}"
                        ),
                        stage.stage_id,
                    )
                )
                continue

            results.extend(
                self._validator.validate_contract(
                    engine,
                    "ENGINE_CONTRACT",
                    capability_registry=self._capability_registry,
                )
            )

        return results

    def _build_dependency_resolver(
        self,
        stages: Iterable[PipelineStage],
    ) -> DependencyResolver:
        """
        Build the published dependency resolver surface for stage graph validation.
        """
        ordered_stages = list(stages)
        resolver = _PipelineDependencyResolver(
            stage_ids=(stage.stage_id for stage in ordered_stages),
            object_registry=self._object_registry,
            capability_registry=self._capability_registry,
            service_registry=self._service_registry,
        )

        for stage in ordered_stages:
            for dependency_id in stage.dependencies:
                resolver.register_dependency(
                    Dependency(stage.stage_id, dependency_id)
                )

        return resolver

    def _resolve_execution_plan(
        self,
        *,
        target_stage_ids: set[str] | None = None,
    ) -> list[str]:
        """
        Resolve the deterministic execution order for the selected stages.
        """
        stages = {
            stage.stage_id: stage
            for stage in self.list_stages()
        }

        if target_stage_ids is None:
            selected_ids = set(stages.keys())
        else:
            selected_ids = set(target_stage_ids)

        for stage_id in selected_ids:
            if stage_id not in stages:
                raise DependencyError(
                    f"Missing dependency target: '{stage_id}'"
                )

        dependents: dict[str, set[str]] = {
            stage_id: set() for stage_id in selected_ids
        }
        in_degree = {stage_id: 0 for stage_id in selected_ids}

        for stage_id in selected_ids:
            stage = stages[stage_id]

            for dependency_id in stage.dependencies:
                if dependency_id not in selected_ids:
                    continue

                dependents.setdefault(dependency_id, set()).add(stage_id)
                in_degree[stage_id] += 1

        ready = sorted(
            [
                stage_id
                for stage_id, degree in in_degree.items()
                if degree == 0
            ],
            key=lambda stage_id: self._stage_sort_key(stages[stage_id]),
        )
        ordered: list[str] = []

        while ready:
            current = ready.pop(0)
            ordered.append(current)

            for dependent_id in sorted(
                dependents.get(current, set()),
                key=lambda stage_id: self._stage_sort_key(stages[stage_id]),
            ):
                in_degree[dependent_id] -= 1

                if in_degree[dependent_id] == 0:
                    ready.append(dependent_id)
                    ready.sort(
                        key=lambda stage_id: self._stage_sort_key(
                            stages[stage_id]
                        )
                    )

        if len(ordered) != len(selected_ids):
            raise DependencyError("Circular pipeline graph detected")

        return ordered

    def _collect_stage_closure(self, stage_id: str) -> set[str]:
        """
        Collect the transitive stage dependency closure for a target stage.
        """
        visited: set[str] = set()

        def visit(candidate_id: str) -> None:
            stage = self._require_stage(candidate_id)

            for dependency_id in stage.dependencies:
                self._require_stage(dependency_id)

                if dependency_id in visited:
                    continue

                visited.add(dependency_id)
                visit(dependency_id)

        visit(stage_id)
        return visited

    def _continue_execution(self) -> list[StageExecution]:
        """
        Execute pending stages until the runtime reaches a terminal or paused state.
        """
        executions: list[StageExecution] = []

        while self._pending_stage_ids:
            if self._runtime_state in {PAUSED, CANCELLED}:
                break

            execution = self._run_stage(self._pending_stage_ids.popleft())
            executions.append(execution)

            if self._runtime_state in {PAUSED, CANCELLED, FAILED}:
                break

        if self._runtime_state == RUNNING and not self._pending_stage_ids:
            self._runtime_state = COMPLETED
            self._publish_event("pipeline.completed")

        return executions

    def _run_stage(self, stage_id: str) -> StageExecution:
        """
        Execute one stage against its registered engine lifecycle.
        """
        stage = self._require_stage(stage_id)
        self._ensure_stage_dependencies_completed(stage)

        execution = StageExecution(
            stage_id=stage.stage_id,
            engine_id=stage.engine,
            status=RUNNING,
            metadata={
                "name": stage.name,
                "execution_order": stage.execution_order,
            },
        )

        stage.status = RUNNING
        self._active_stage_id = stage.stage_id
        self._publish_event(
            "pipeline.stage.started",
            stage=stage,
            execution=execution,
        )

        if self._runtime_state == PAUSED:
            stage.status = PAUSED
            execution.mark_paused()
            self._pending_stage_ids.appendleft(stage.stage_id)
            self._active_stage_id = None
            self._execution_history.append(execution)
            self._publish_event(
                "pipeline.stage.paused",
                stage=stage,
                execution=execution,
            )
            return execution

        if self._runtime_state == CANCELLED:
            stage.status = CANCELLED
            execution.mark_cancelled("Pipeline execution was cancelled")
            self._active_stage_id = None
            self._execution_history.append(execution)
            self._publish_event(
                "pipeline.stage.cancelled",
                stage=stage,
                execution=execution,
                error_message=execution.error,
            )
            return execution

        if self._engine_registry is None:
            message = "EngineRegistry integration is required for stage execution"
            stage.status = FAILED
            self._runtime_state = FAILED
            execution.mark_failed(message)
            self._active_stage_id = None
            self._execution_history.append(execution)
            self._publish_event(
                "pipeline.stage.failed",
                stage=stage,
                execution=execution,
                error_message=message,
            )
            self._publish_event("pipeline.failed", stage=stage)
            return execution

        try:
            self._engine_registry.start_engine(stage.engine)
            self._engine_registry.stop_engine(stage.engine)
        except Exception as exc:
            message = str(exc)
            stage.status = FAILED
            self._runtime_state = FAILED
            execution.mark_failed(message)
            self._active_stage_id = None
            self._execution_history.append(execution)
            self._publish_event(
                "pipeline.stage.failed",
                stage=stage,
                execution=execution,
                error_message=message,
            )
            self._publish_event(
                "pipeline.failed",
                stage=stage,
                error_message=message,
            )
            return execution

        stage.status = COMPLETED
        execution.mark_completed()
        self._active_stage_id = None
        self._execution_history.append(execution)
        self._publish_event(
            "pipeline.stage.completed",
            stage=stage,
            execution=execution,
        )
        return execution

    def _ensure_stage_dependencies_completed(
        self,
        stage: PipelineStage,
    ) -> None:
        """
        Ensure every direct dependency has completed before stage execution.
        """
        incomplete = [
            dependency_id
            for dependency_id in stage.dependencies
            if self._require_stage(dependency_id).status != COMPLETED
        ]

        if incomplete:
            raise DependencyError(
                "Stage dependencies are not satisfied: "
                + ", ".join(sorted(incomplete))
            )

    @staticmethod
    def _ordered_stage_values(
        stages: Iterable[PipelineStage],
    ) -> list[PipelineStage]:
        """
        Order stages by the published deterministic stage key.
        """
        return sorted(
            list(stages),
            key=Pipeline._stage_sort_key,
        )

    @staticmethod
    def _stage_sort_key(stage: PipelineStage) -> tuple[int, str]:
        """
        Return the deterministic stage order key.
        """
        return (stage.execution_order, stage.stage_id)

    def _schema_payload(
        self,
        stages: Iterable[PipelineStage],
    ) -> dict[str, object]:
        """
        Build the published M16 schema payload.
        """
        return {
            "stages": [stage.to_dict() for stage in stages],
            "runtime_state": self._runtime_state,
            "metadata": dict(self.metadata),
        }

    def _raise_for_invalid_results(
        self,
        source: str,
        results: Iterable[ValidationResult],
    ) -> None:
        """
        Raise a registry error when validation results contain failures.
        """
        invalid_messages = [
            f"{result.rule_id}: {result.message}"
            for result in results
            if result.status == "invalid"
        ]

        if not invalid_messages:
            return

        raise RegistryError(
            f"Pipeline '{source}' failed validation: "
            + "; ".join(invalid_messages)
        )

    @staticmethod
    def _has_invalid_results(
        results: Iterable[ValidationResult],
    ) -> bool:
        """
        Determine whether any validation result is invalid.
        """
        return any(result.status == "invalid" for result in results)

    @staticmethod
    def _valid_result(
        rule_id: str,
        message: str,
        source: str,
    ) -> ValidationResult:
        """
        Build a successful validation result.
        """
        return ValidationResult(
            status="valid",
            severity="info",
            rule_id=rule_id,
            message=message,
            source=source,
        )

    @staticmethod
    def _invalid_result(
        rule_id: str,
        message: str,
        source: str,
    ) -> ValidationResult:
        """
        Build a failed validation result.
        """
        return ValidationResult(
            status="invalid",
            severity="error",
            rule_id=rule_id,
            message=message,
            source=source,
        )

    def _raise_for_failed_execution(
        self,
        executions: Iterable[StageExecution],
    ) -> None:
        """
        Raise a registry error when execution ends in the failed state.
        """
        if self._runtime_state != FAILED:
            return

        for execution in reversed(list(executions)):
            if execution.error:
                raise RegistryError(execution.error)

        raise RegistryError("Pipeline execution failed")

    def _publish_event(
        self,
        event_type: str,
        *,
        stage: PipelineStage | None = None,
        execution: StageExecution | None = None,
        error_message: str | None = None,
    ) -> None:
        """
        Publish a pipeline lifecycle event when an event bus exists.
        """
        if self._event_bus is None:
            return

        payload: dict[str, object] = {
            "runtime_state": self.runtime_state,
            "stage_count": self._stages.count(),
            "stages": tuple(
                current_stage.stage_id
                for current_stage in self.list_stages()
            ),
            "pending_stage_ids": tuple(self._pending_stage_ids),
        }

        if self._active_stage_id is not None:
            payload["active_stage_id"] = self._active_stage_id

        if stage is not None:
            payload.update(
                {
                    "stage_id": stage.stage_id,
                    "name": stage.name,
                    "engine": stage.engine,
                    "stage_status": stage.status,
                    "execution_order": stage.execution_order,
                    "dependencies": tuple(stage.dependencies),
                }
            )

        if execution is not None:
            payload["execution"] = execution.to_dict()

        if error_message:
            payload["error"] = error_message

        if self._plugin_loader is not None:
            payload["loaded_plugins"] = tuple(
                plugin.plugin_id
                for plugin in self._plugin_loader.list_plugins()
            )

        if self._application_registry is not None:
            payload["registered_applications"] = tuple(
                application.application_id
                for application in self._application_registry.list_applications()
            )

        if self._engine_registry is not None:
            payload["registered_engines"] = tuple(
                engine.engine_id
                for engine in self._engine_registry.list_engines()
            )

        self._event_bus.publish(
            Event(
                event_type=event_type,
                source="Runtime.Pipeline",
                payload=payload,
            )
        )
