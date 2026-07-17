"""
AXI Platform Runtime

Pipeline Stage

Runtime representation of an AXI pipeline stage.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

from Runtime.Pipeline.runtime import INITIALIZED, ensure_runtime_state
from Runtime.exceptions import RegistryError


@dataclass(slots=True)
class PipelineStage:
    """
    Runtime pipeline stage definition.
    """

    stage_id: str
    name: str
    description: str = ""
    execution_order: int = 0
    dependencies: list[str] = field(default_factory=list)
    engine: str = ""
    status: str = INITIALIZED
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Validate and normalize stage state.
        """
        if not isinstance(self.stage_id, str) or not self.stage_id:
            raise RegistryError(
                "Invalid stage definition: stage_id is required"
            )

        if not isinstance(self.name, str) or not self.name:
            raise RegistryError(
                "Invalid stage definition: name is required"
            )

        if not isinstance(self.description, str):
            raise RegistryError(
                "Invalid stage definition: description must be a string"
            )

        if not isinstance(self.execution_order, int) or isinstance(
            self.execution_order,
            bool,
        ):
            raise RegistryError(
                "Invalid stage definition: "
                "execution_order must be an integer"
            )

        if not isinstance(self.engine, str) or not self.engine:
            raise RegistryError(
                "Invalid stage definition: engine is required"
            )

        if not isinstance(self.dependencies, list | tuple):
            raise RegistryError(
                "Invalid stage definition: dependencies must be a sequence"
            )

        normalized_dependencies = list(self.dependencies)

        if any(
            not isinstance(dependency_id, str) or not dependency_id
            for dependency_id in normalized_dependencies
        ):
            raise RegistryError(
                "Invalid stage definition: "
                "dependencies must contain non-empty strings"
            )

        if len(normalized_dependencies) != len(set(normalized_dependencies)):
            raise RegistryError(
                "Invalid stage definition: dependencies must be unique"
            )

        if not isinstance(self.metadata, Mapping):
            raise RegistryError(
                "Invalid stage definition: metadata must be a mapping"
            )

        self.dependencies = normalized_dependencies
        self.metadata = dict(self.metadata)
        self.status = ensure_runtime_state(self.status)

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the published stage payload.
        """
        return {
            "stage_id": self.stage_id,
            "name": self.name,
            "description": self.description,
            "execution_order": self.execution_order,
            "dependencies": list(self.dependencies),
            "engine": self.engine,
            "status": self.status,
            "metadata": dict(self.metadata),
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "PipelineStage":
        """
        Deserialize a stage payload.
        """
        return cls(
            stage_id=str(data["stage_id"]),
            name=str(data["name"]),
            description=str(data.get("description", "")),
            execution_order=data.get("execution_order", 0),
            dependencies=list(data.get("dependencies", [])),
            engine=str(data["engine"]),
            status=str(data.get("status", INITIALIZED)),
            metadata=dict(data.get("metadata", {})),
        )
