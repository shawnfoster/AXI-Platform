"""
AXI Platform Runtime

API Operation

Validated operation payload for the M18 Runtime API.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

from Runtime.CLI.command import CLICommand
from Runtime.exceptions import RegistryError


@dataclass(frozen=True, slots=True)
class APIOperation:
    """
    Immutable Runtime API operation payload.
    """

    operation: str
    target: str = ""
    stage_id: str = ""
    runtime_context: Mapping[str, Any] = field(default_factory=dict)
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Validate and normalize operation payload state.
        """
        if not isinstance(self.operation, str) or not self.operation:
            raise RegistryError(
                "Invalid API operation: operation is required"
            )

        if not isinstance(self.target, str):
            raise RegistryError(
                "Invalid API operation: target must be a string"
            )

        if not isinstance(self.stage_id, str):
            raise RegistryError(
                "Invalid API operation: stage_id must be a string"
            )

        if not isinstance(self.runtime_context, Mapping):
            raise RegistryError(
                "Invalid API operation: runtime_context must be a mapping"
            )

        if not isinstance(self.metadata, Mapping):
            raise RegistryError(
                "Invalid API operation: metadata must be a mapping"
            )

        object.__setattr__(self, "runtime_context", dict(self.runtime_context))
        object.__setattr__(self, "metadata", dict(self.metadata))

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the published API operation payload.
        """
        data: dict[str, Any] = {
            "operation": self.operation,
        }

        if self.target:
            data["target"] = self.target

        if self.stage_id:
            data["stage_id"] = self.stage_id

        if self.runtime_context:
            data["runtime_context"] = dict(self.runtime_context)

        if self.metadata:
            data["metadata"] = dict(self.metadata)

        return data

    def to_cli_command(self) -> CLICommand:
        """
        Adapt this API operation into the governed CLI command model.
        """
        return CLICommand(
            command=self.operation,
            target=self.target,
            stage_id=self.stage_id,
            runtime_context=self.runtime_context,
            metadata=self.metadata,
        )

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "APIOperation":
        """
        Build an API operation payload from mapping-shaped input.
        """
        if not isinstance(data, Mapping):
            raise RegistryError(
                "Invalid API operation: operation payload must be a mapping"
            )

        return cls(
            operation=str(data.get("operation", "")),
            target=str(data.get("target", "")),
            stage_id=str(data.get("stage_id", "")),
            runtime_context=dict(data.get("runtime_context", {})),
            metadata=dict(data.get("metadata", {})),
        )
