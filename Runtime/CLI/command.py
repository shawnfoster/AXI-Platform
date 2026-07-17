"""
AXI Platform Runtime

CLI Command

Validated command payload for the M17 Runtime CLI.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

from Runtime.exceptions import RegistryError


@dataclass(frozen=True, slots=True)
class CLICommand:
    """
    Immutable Runtime CLI command payload.
    """

    command: str
    target: str = ""
    stage_id: str = ""
    runtime_context: Mapping[str, Any] = field(default_factory=dict)
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Validate and normalize command payload state.
        """
        if not isinstance(self.command, str) or not self.command:
            raise RegistryError(
                "Invalid CLI command: command is required"
            )

        if not isinstance(self.target, str):
            raise RegistryError(
                "Invalid CLI command: target must be a string"
            )

        if not isinstance(self.stage_id, str):
            raise RegistryError(
                "Invalid CLI command: stage_id must be a string"
            )

        if not isinstance(self.runtime_context, Mapping):
            raise RegistryError(
                "Invalid CLI command: runtime_context must be a mapping"
            )

        if not isinstance(self.metadata, Mapping):
            raise RegistryError(
                "Invalid CLI command: metadata must be a mapping"
            )

        object.__setattr__(self, "runtime_context", dict(self.runtime_context))
        object.__setattr__(self, "metadata", dict(self.metadata))

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the published CLI command payload.
        """
        data: dict[str, Any] = {
            "command": self.command,
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

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "CLICommand":
        """
        Build a command payload from mapping-shaped input.
        """
        if not isinstance(data, Mapping):
            raise RegistryError(
                "Invalid CLI command: command payload must be a mapping"
            )

        return cls(
            command=str(data.get("command", "")),
            target=str(data.get("target", "")),
            stage_id=str(data.get("stage_id", "")),
            runtime_context=dict(data.get("runtime_context", {})),
            metadata=dict(data.get("metadata", {})),
        )
