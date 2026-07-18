"""
AXI Platform Runtime

Runtime API

Local programmatic surface for the governed M18 Runtime API.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from Runtime.ApplicationRegistry import ApplicationRegistry
from Runtime.CLI import RuntimeCLI
from Runtime.EngineRegistry import EngineRegistry
from Runtime.Pipeline import Pipeline
from Runtime.PluginLoader import PluginLoader
from Runtime.Validation import ValidationResult, Validator
from Runtime.exceptions import RegistryError

from .operation import APIOperation
from .result import APIResult

SUPPORTED_OPERATIONS = frozenset(
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
LIFECYCLE_OPERATIONS = frozenset({"pause", "resume", "stop"})


class RuntimeAPI:
    """
    Governed local programmatic surface for the AXI runtime.
    """

    def __init__(
        self,
        *,
        runtime_cli: RuntimeCLI | None = None,
        plugin_loader: PluginLoader | None = None,
        application_registry: ApplicationRegistry | None = None,
        engine_registry: EngineRegistry | None = None,
        pipeline: Pipeline | None = None,
        validator: Validator | None = None,
    ) -> None:
        """
        Initialize the Runtime API.
        """
        self._validator = validator or Validator()
        self._runtime_cli = runtime_cli or RuntimeCLI(
            plugin_loader=plugin_loader,
            application_registry=application_registry,
            engine_registry=engine_registry,
            pipeline=pipeline,
            validator=self._validator,
        )

    def invoke(
        self,
        operation: APIOperation | Mapping[str, Any],
    ) -> APIResult:
        """
        Validate and execute a Runtime API operation.
        """
        candidate = self._normalize_operation(operation)
        result = self._runtime_cli.run(candidate.to_cli_command())
        return APIResult(
            operation=candidate.operation,
            status=result.status,
            payload=result.payload,
        )

    def _normalize_operation(
        self,
        operation: APIOperation | Mapping[str, Any],
    ) -> APIOperation:
        """
        Normalize, validate, and enforce API operation semantics.
        """
        if isinstance(operation, APIOperation):
            candidate = operation
        elif isinstance(operation, Mapping):
            candidate = APIOperation.from_dict(operation)
        else:
            raise RegistryError(
                "Invalid API operation: expected APIOperation or mapping"
            )

        self._raise_for_invalid_results(
            "API operation",
            self._validator.validate_schema(
                candidate.to_dict(),
                "AXI-SCH-014",
            ),
        )

        if candidate.operation not in SUPPORTED_OPERATIONS:
            raise RegistryError(
                f"Unsupported API operation: '{candidate.operation}'"
            )

        if candidate.operation == "inspect":
            if not candidate.target:
                raise RegistryError(
                    "Invalid API operation: inspect requires target"
                )

            if candidate.target not in INSPECT_TARGETS:
                raise RegistryError(
                    f"Unsupported inspect target: '{candidate.target}'"
                )
        elif candidate.target:
            raise RegistryError(
                "Invalid API operation: target is supported only for inspect"
            )

        if candidate.operation == "execute-stage":
            if not candidate.stage_id:
                raise RegistryError(
                    "Invalid API operation: execute-stage requires stage_id"
                )
        elif candidate.stage_id:
            raise RegistryError(
                "Invalid API operation: stage_id is supported only for execute-stage"
            )

        if (
            candidate.operation in LIFECYCLE_OPERATIONS
            and candidate.runtime_context
        ):
            raise RegistryError(
                "Invalid API operation: lifecycle operations require a caller-managed Pipeline instance"
            )

        return candidate

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
