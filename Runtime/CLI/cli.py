"""
AXI Platform Runtime

Runtime CLI

Local command surface for the governed M17 Runtime CLI.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from Runtime.ApplicationRegistry import Application, ApplicationRegistry
from Runtime.EngineRegistry import Engine, EngineRegistry
from Runtime.Pipeline import Pipeline
from Runtime.Pipeline.runtime import ensure_runtime_state
from Runtime.PluginLoader import PluginLoader
from Runtime.Validation import ValidationResult, Validator
from Runtime.exceptions import RegistryError

from .command import CLICommand
from .result import CLIResult

SUPPORTED_COMMANDS = frozenset(
    {
        "inspect",
        "validate",
        "execute",
        "execute-stage",
        "pause",
        "resume",
        "stop",
    }
)
INSPECT_TARGETS = frozenset(
    {
        "plugins",
        "applications",
        "engines",
        "stages",
        "runtime",
    }
)
LIFECYCLE_COMMANDS = frozenset({"pause", "resume", "stop"})


@dataclass(slots=True)
class _RuntimeComponents:
    """
    Connected runtime component bundle used by one CLI command.
    """

    plugin_loader: PluginLoader
    application_registry: ApplicationRegistry
    engine_registry: EngineRegistry
    pipeline: Pipeline


class RuntimeCLI:
    """
    Governed local command surface for the AXI runtime.
    """

    def __init__(
        self,
        *,
        plugin_loader: PluginLoader | None = None,
        application_registry: ApplicationRegistry | None = None,
        engine_registry: EngineRegistry | None = None,
        pipeline: Pipeline | None = None,
        validator: Validator | None = None,
    ) -> None:
        """
        Initialize the Runtime CLI.
        """
        self._plugin_loader = plugin_loader
        self._application_registry = application_registry
        self._engine_registry = engine_registry
        self._pipeline = pipeline
        self._validator = validator or Validator()

    def run(
        self,
        command: CLICommand | Mapping[str, Any],
    ) -> CLIResult:
        """
        Validate and execute a Runtime CLI command.
        """
        candidate = self._normalize_command(command)
        components = self._resolve_components(candidate)

        if candidate.command == "inspect":
            payload = self._inspect(candidate, components)
        elif candidate.command == "validate":
            payload = self._validate(components.pipeline)
        elif candidate.command == "execute":
            payload = self._execute(components.pipeline)
        elif candidate.command == "execute-stage":
            payload = self._execute_stage(
                components.pipeline,
                candidate.stage_id,
            )
        elif candidate.command == "pause":
            payload = self._pause(components.pipeline)
        elif candidate.command == "resume":
            payload = self._resume(components.pipeline)
        elif candidate.command == "stop":
            payload = self._stop(components.pipeline)
        else:
            raise RegistryError(
                f"Unsupported CLI command: '{candidate.command}'"
            )

        return CLIResult(
            command=candidate.command,
            status="ok",
            payload=payload,
        )

    def _normalize_command(
        self,
        command: CLICommand | Mapping[str, Any],
    ) -> CLICommand:
        """
        Normalize, validate, and enforce CLI command semantics.
        """
        if isinstance(command, CLICommand):
            candidate = command
        elif isinstance(command, Mapping):
            candidate = CLICommand.from_dict(command)
        else:
            raise RegistryError(
                "Invalid CLI command: expected CLICommand or mapping"
            )

        self._raise_for_invalid_results(
            "CLI command",
            self._validator.validate_schema(
                candidate.to_dict(),
                "AXI-SCH-013",
            ),
        )

        if candidate.command not in SUPPORTED_COMMANDS:
            raise RegistryError(
                f"Unsupported CLI command: '{candidate.command}'"
            )

        if candidate.command == "inspect":
            if not candidate.target:
                raise RegistryError(
                    "Invalid CLI command: inspect requires target"
                )

            if candidate.target not in INSPECT_TARGETS:
                raise RegistryError(
                    f"Unsupported inspect target: '{candidate.target}'"
                )
        elif candidate.target:
            raise RegistryError(
                "Invalid CLI command: target is supported only for inspect"
            )

        if candidate.command == "execute-stage":
            if not candidate.stage_id:
                raise RegistryError(
                    "Invalid CLI command: execute-stage requires stage_id"
                )
        elif candidate.stage_id:
            raise RegistryError(
                "Invalid CLI command: stage_id is supported only for execute-stage"
            )

        if (
            candidate.command in LIFECYCLE_COMMANDS
            and candidate.runtime_context
        ):
            raise RegistryError(
                "Invalid CLI command: lifecycle commands require a caller-managed Pipeline instance"
            )

        return candidate

    def _resolve_components(
        self,
        command: CLICommand,
    ) -> _RuntimeComponents:
        """
        Resolve the runtime component bundle used for one command.
        """
        if command.command in LIFECYCLE_COMMANDS:
            if self._pipeline is None:
                raise RegistryError(
                    f"CLI command '{command.command}' requires a caller-managed Pipeline instance"
                )

            return self._build_default_components()

        if command.runtime_context:
            return self._build_context_components(command.runtime_context)

        return self._build_default_components()

    def _build_default_components(self) -> _RuntimeComponents:
        """
        Build the connected runtime component bundle from injected defaults.
        """
        plugin_loader = self._plugin_loader or PluginLoader()
        application_registry = self._application_registry or ApplicationRegistry(
            plugin_loader=plugin_loader,
        )
        engine_registry = self._engine_registry or EngineRegistry(
            plugin_loader=plugin_loader,
            application_registry=application_registry,
        )
        pipeline = self._pipeline or Pipeline(
            plugin_loader=plugin_loader,
            application_registry=application_registry,
            engine_registry=engine_registry,
        )

        return _RuntimeComponents(
            plugin_loader=plugin_loader,
            application_registry=application_registry,
            engine_registry=engine_registry,
            pipeline=pipeline,
        )

    def _build_context_components(
        self,
        runtime_context: Mapping[str, Any],
    ) -> _RuntimeComponents:
        """
        Build a temporary runtime component bundle from published payloads.
        """
        plugin_loader = PluginLoader()
        for manifest in runtime_context.get("plugins", []):
            plugin_loader.load_plugin(manifest)

        application_registry = ApplicationRegistry(
            plugin_loader=plugin_loader,
        )
        for payload in runtime_context.get("applications", []):
            if not isinstance(payload, Mapping):
                raise RegistryError(
                    "Invalid runtime_context: applications must contain mappings"
                )

            try:
                application = Application.from_dict(dict(payload))
            except KeyError as exc:
                raise RegistryError(
                    "Invalid runtime_context application payload: "
                    "full Application.to_dict() payload is required"
                ) from exc

            application_registry.register_application(application)

        engine_registry = EngineRegistry(
            plugin_loader=plugin_loader,
            application_registry=application_registry,
        )
        for payload in runtime_context.get("engines", []):
            if not isinstance(payload, Mapping):
                raise RegistryError(
                    "Invalid runtime_context: engines must contain mappings"
                )

            try:
                engine = Engine.from_dict(dict(payload))
            except KeyError as exc:
                raise RegistryError(
                    "Invalid runtime_context engine payload: "
                    "full Engine.to_dict() payload is required"
                ) from exc

            engine_registry.register_engine(engine)

        pipeline_payload = runtime_context.get("pipeline", {})
        if pipeline_payload and not isinstance(pipeline_payload, Mapping):
            raise RegistryError(
                "Invalid runtime_context: pipeline must be a mapping"
            )

        self._raise_for_invalid_results(
            "runtime_context.pipeline",
            self._validator.validate_schema(
                dict(pipeline_payload or {}),
                "AXI-SCH-012",
            )
            if pipeline_payload
            else [],
        )

        pipeline = Pipeline(
            plugin_loader=plugin_loader,
            application_registry=application_registry,
            engine_registry=engine_registry,
            metadata=dict((pipeline_payload or {}).get("metadata", {})),
        )

        for stage in (pipeline_payload or {}).get("stages", []):
            pipeline.register_stage(stage)

        if pipeline_payload:
            pipeline._runtime_state = ensure_runtime_state(
                str(pipeline_payload.get("runtime_state", pipeline.runtime_state))
            )

        return _RuntimeComponents(
            plugin_loader=plugin_loader,
            application_registry=application_registry,
            engine_registry=engine_registry,
            pipeline=pipeline,
        )

    def _inspect(
        self,
        command: CLICommand,
        components: _RuntimeComponents,
    ) -> dict[str, object]:
        """
        Execute a deterministic runtime inspection command.
        """
        target = command.target

        if target == "plugins":
            return {
                "target": target,
                "items": [
                    plugin.to_dict()
                    for plugin in components.plugin_loader.list_plugins()
                ],
            }

        if target == "applications":
            return {
                "target": target,
                "items": [
                    application.to_dict()
                    for application in components.application_registry.list_applications()
                ],
            }

        if target == "engines":
            return {
                "target": target,
                "items": [
                    engine.to_dict()
                    for engine in components.engine_registry.list_engines()
                ],
            }

        if target == "stages":
            return {
                "target": target,
                "items": [
                    stage.to_dict()
                    for stage in components.pipeline.list_stages()
                ],
            }

        if target == "runtime":
            return {
                "target": target,
                "runtime": components.pipeline.to_dict(),
            }

        raise RegistryError(f"Unsupported inspect target: '{target}'")

    def _validate(self, pipeline: Pipeline) -> dict[str, object]:
        """
        Validate the current pipeline definition.
        """
        results = pipeline.validate_pipeline()
        return {
            "results": self._serialize_validation_results(results),
            "pipeline": pipeline.to_dict(),
        }

    def _execute(self, pipeline: Pipeline) -> dict[str, object]:
        """
        Execute the full pipeline.
        """
        executions = pipeline.execute()
        return {
            "executions": [execution.to_dict() for execution in executions],
            "pipeline": pipeline.to_dict(),
        }

    def _execute_stage(
        self,
        pipeline: Pipeline,
        stage_id: str,
    ) -> dict[str, object]:
        """
        Execute one stage closure.
        """
        executions = pipeline.execute_stage(stage_id)
        return {
            "stage_id": stage_id,
            "executions": [execution.to_dict() for execution in executions],
            "pipeline": pipeline.to_dict(),
        }

    def _pause(self, pipeline: Pipeline) -> dict[str, object]:
        """
        Pause a caller-managed active pipeline.
        """
        pipeline.pause()
        return {
            "runtime_state": pipeline.runtime_state,
            "pipeline": pipeline.to_dict(),
        }

    def _resume(self, pipeline: Pipeline) -> dict[str, object]:
        """
        Resume a caller-managed paused pipeline.
        """
        pipeline.resume()
        return {
            "runtime_state": pipeline.runtime_state,
            "pipeline": pipeline.to_dict(),
        }

    def _stop(self, pipeline: Pipeline) -> dict[str, object]:
        """
        Stop a caller-managed running or paused pipeline.
        """
        pipeline.stop()
        return {
            "runtime_state": pipeline.runtime_state,
            "pipeline": pipeline.to_dict(),
        }

    @staticmethod
    def _serialize_validation_results(
        results: list[ValidationResult],
    ) -> list[dict[str, str]]:
        """
        Serialize runtime validation results.
        """
        return [
            {
                "status": result.status,
                "severity": result.severity,
                "rule_id": result.rule_id,
                "message": result.message,
                "source": result.source,
                "timestamp": result.timestamp.isoformat(),
            }
            for result in results
        ]

    @staticmethod
    def _raise_for_invalid_results(
        source: str,
        results: list[ValidationResult],
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
            f"{source} failed validation: " + "; ".join(invalid_messages)
        )


def build_parser() -> argparse.ArgumentParser:
    """
    Build the Runtime CLI shell parser.
    """
    parser = argparse.ArgumentParser(prog="axi-runtime")
    subparsers = parser.add_subparsers(dest="command", required=True)

    inspect_parser = subparsers.add_parser("inspect")
    inspect_parser.add_argument(
        "target",
        choices=sorted(INSPECT_TARGETS),
    )
    inspect_parser.add_argument(
        "--context",
        dest="context_path",
        default="",
    )

    for name in ("validate", "execute", "pause", "resume", "stop"):
        subparser = subparsers.add_parser(name)
        subparser.add_argument(
            "--context",
            dest="context_path",
            default="",
        )

    execute_stage_parser = subparsers.add_parser("execute-stage")
    execute_stage_parser.add_argument("stage_id")
    execute_stage_parser.add_argument(
        "--context",
        dest="context_path",
        default="",
    )

    return parser


def main(
    argv: list[str] | None = None,
    *,
    runtime_cli: RuntimeCLI | None = None,
) -> int:
    """
    Execute one shell-facing Runtime CLI command.
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    command_payload: dict[str, object] = {
        "command": args.command,
    }

    if hasattr(args, "target"):
        command_payload["target"] = args.target

    if hasattr(args, "stage_id"):
        command_payload["stage_id"] = args.stage_id

    context_path = getattr(args, "context_path", "")
    if context_path:
        command_payload["runtime_context"] = _load_runtime_context(
            Path(context_path)
        )

    cli = runtime_cli or RuntimeCLI()

    try:
        result = cli.run(command_payload)
    except Exception as exc:
        json.dump(
            {
                "command": args.command,
                "status": "error",
                "error": str(exc),
            },
            sys.stderr,
            sort_keys=True,
        )
        sys.stderr.write("\n")
        return 1

    json.dump(result.to_dict(), sys.stdout, sort_keys=True)
    sys.stdout.write("\n")
    return 0


def _load_runtime_context(path: Path) -> dict[str, object]:
    """
    Load a runtime context mapping from JSON.
    """
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise RegistryError(
            f"Runtime context file not found: '{path}'"
        ) from exc
    except json.JSONDecodeError as exc:
        raise RegistryError(
            f"Invalid runtime context JSON: {exc.msg}"
        ) from exc

    if not isinstance(payload, Mapping):
        raise RegistryError(
            "Invalid runtime context JSON: root value must be an object"
        )

    return dict(payload)
