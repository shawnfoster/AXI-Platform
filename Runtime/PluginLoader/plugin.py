"""
AXI Platform Runtime

Plugin

Runtime representation of a managed AXI plugin.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from Runtime.PluginLoader.manifest import PluginManifest
from Runtime.Validation import ValidationResult
from Runtime.exceptions import RegistryError


@dataclass(slots=True)
class Plugin:
    """
    Runtime plugin record managed by the Plugin Loader.
    """

    manifest: PluginManifest
    path: Path | None = None
    manifest_path: Path | None = None
    lifecycle_state: str = ""
    validation_results: tuple[ValidationResult, ...] = field(
        default_factory=tuple
    )
    dependency_order: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        """
        Validate plugin state.
        """
        if not isinstance(self.manifest, PluginManifest):
            raise RegistryError(
                "Invalid plugin definition: manifest is required"
            )

        if not self.lifecycle_state:
            self.lifecycle_state = self.manifest.lifecycle_state

    @property
    def plugin_id(self) -> str:
        """
        Return the managed plugin identifier.
        """
        return self.manifest.plugin_id

    @property
    def name(self) -> str:
        """
        Return the managed plugin name.
        """
        return self.manifest.name

    @property
    def version(self) -> str:
        """
        Return the managed plugin version.
        """
        return self.manifest.version

    @property
    def author(self) -> str:
        """
        Return the managed plugin author.
        """
        return self.manifest.author

    @property
    def description(self) -> str:
        """
        Return the managed plugin description.
        """
        return self.manifest.description

    @property
    def capabilities(self) -> tuple[str, ...]:
        """
        Return declared capability identifiers.
        """
        return self.manifest.capabilities

    @property
    def dependencies(self) -> tuple[str, ...]:
        """
        Return declared dependency identifiers.
        """
        return self.manifest.dependencies

    def to_manifest_dict(self) -> dict[str, Any]:
        """
        Serialize the manifest payload with current lifecycle state.
        """
        data = self.manifest.to_dict()

        if self.lifecycle_state or "lifecycle_state" in data:
            data["lifecycle_state"] = self.lifecycle_state

        return data

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the runtime plugin record.
        """
        data = self.to_manifest_dict()
        data["path"] = str(self.path) if self.path is not None else None
        data["manifest_path"] = (
            str(self.manifest_path)
            if self.manifest_path is not None
            else None
        )
        data["dependency_order"] = list(self.dependency_order)
        data["validation_results"] = [
            {
                "status": result.status,
                "severity": result.severity,
                "rule_id": result.rule_id,
                "message": result.message,
                "source": result.source,
                "timestamp": result.timestamp.isoformat(),
            }
            for result in self.validation_results
        ]
        return data

    @classmethod
    def from_manifest(
        cls,
        manifest: PluginManifest,
        *,
        path: Path | None = None,
        manifest_path: Path | None = None,
    ) -> "Plugin":
        """
        Build a runtime plugin record from a manifest.
        """
        return cls(
            manifest=manifest,
            path=path,
            manifest_path=manifest_path,
        )
