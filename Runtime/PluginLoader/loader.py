"""
AXI Platform Runtime

Plugin Loader

Loader-managed plugin discovery, validation, loading, and lifecycle
tracking for the AXI runtime.
"""

from __future__ import annotations

import json
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

from Runtime.CapabilityRegistry import CapabilityRegistry
from Runtime.DependencyResolver import Dependency, DependencyResolver
from Runtime.EventBus import Event, EventBus
from Runtime.ObjectRegistry import ObjectRegistry
from Runtime.PluginLoader.manifest import PluginManifest
from Runtime.PluginLoader.plugin import Plugin
from Runtime.Registry import BaseRegistry
from Runtime.ServiceRegistry import ServiceRegistry
from Runtime.Validation import ValidationResult, Validator
from Runtime.exceptions import (
    DependencyError,
    ObjectNotFoundError,
    RegistryError,
)

PluginInput = str | Plugin | PluginManifest | Mapping[str, Any]


class _PluginDependencyResolver(DependencyResolver):
    """
    Loader-local dependency resolver that accepts managed plugin IDs.
    """

    def __init__(
        self,
        *,
        plugin_ids: Iterable[str],
        object_registry: ObjectRegistry | None = None,
        capability_registry: CapabilityRegistry | None = None,
        service_registry: ServiceRegistry | None = None,
    ) -> None:
        super().__init__(
            object_registry=object_registry,
            capability_registry=capability_registry,
            service_registry=service_registry,
        )
        self._plugin_ids = set(plugin_ids)

    def _identifier_exists(self, identifier: str) -> bool:
        """
        Resolve identifiers from loader-managed plugins first.
        """
        return (
            identifier in self._plugin_ids
            or super()._identifier_exists(identifier)
        )


class PluginLoader:
    """
    AXI runtime plugin loader.
    """

    def __init__(
        self,
        *,
        plugin_roots: Iterable[str | Path] = (),
        manifest_filename: str = "plugin.json",
        object_registry: ObjectRegistry | None = None,
        capability_registry: CapabilityRegistry | None = None,
        service_registry: ServiceRegistry | None = None,
        event_bus: EventBus | None = None,
        validator: Validator | None = None,
    ) -> None:
        """
        Initialize the plugin loader.
        """
        if not isinstance(manifest_filename, str) or not manifest_filename:
            raise ValueError("manifest_filename must be a non-empty string")

        self._plugin_roots = tuple(Path(root) for root in plugin_roots)
        self._manifest_filename = manifest_filename
        self._object_registry = object_registry
        self._capability_registry = capability_registry
        self._service_registry = service_registry
        self._event_bus = event_bus
        self._validator = validator or Validator(
            object_registry=object_registry,
            capability_registry=capability_registry,
            service_registry=service_registry,
            event_bus=event_bus,
        )
        self._discovered = BaseRegistry[Plugin]()
        self._plugins = BaseRegistry[Plugin]()

    def discover_plugins(self) -> list[Plugin]:
        """
        Discover plugin manifests under loader-managed plugin roots.
        """
        discovered = BaseRegistry[Plugin]()

        for manifest_path in self._iter_manifest_paths():
            plugin = self._plugin_from_path(manifest_path)
            loaded_plugin = self._plugins.get(plugin.plugin_id)

            if loaded_plugin is not None:
                plugin.lifecycle_state = loaded_plugin.lifecycle_state
                plugin.validation_results = loaded_plugin.validation_results
                plugin.dependency_order = loaded_plugin.dependency_order

            discovered.register(plugin.plugin_id, plugin)
            self._publish_event(
                "plugin.discovered",
                plugin,
                manifest_path=manifest_path,
            )

        self._discovered = discovered
        return self._ordered_plugins(self._discovered)

    def validate_plugin(
        self,
        plugin: PluginInput,
    ) -> list[ValidationResult]:
        """
        Validate a plugin manifest and its dependencies.
        """
        candidate, manifest_data, source = self._normalize_for_validation(
            plugin
        )
        results = self._validator.validate_schema(
            manifest_data,
            "AXI-SCH-009",
        )
        results.extend(
            self._validator.validate_metadata(
                manifest_data,
                source=source,
            )
        )

        if self._has_invalid_results(results):
            self._apply_validation_results(candidate, results)
            return results

        if candidate is None:
            candidate = Plugin.from_manifest(
                PluginManifest.from_dict(manifest_data)
            )

        try:
            dependency_resolver = self._build_dependency_resolver(candidate)
        except DependencyError as exc:
            results.append(
                ValidationResult(
                    status="invalid",
                    severity="error",
                    rule_id="dependencies.validate",
                    message=str(exc),
                    source=source,
                )
            )
            self._apply_validation_results(candidate, results)
            return results

        results.extend(
            self._validator.validate_dependencies(dependency_resolver)
        )

        if not self._has_invalid_results(results):
            candidate.dependency_order = tuple(
                dependency_resolver.resolve(candidate.plugin_id)
            )

        self._apply_validation_results(candidate, results)
        return results

    def load_plugin(
        self,
        plugin: PluginInput,
    ) -> Plugin:
        """
        Validate and load a plugin into loader-managed runtime state.
        """
        candidate = self._resolve_plugin(plugin)
        results = self.validate_plugin(candidate)
        self._raise_for_invalid_results(candidate.plugin_id, results)
        candidate.lifecycle_state = "Loaded"
        self._plugins.register(candidate.plugin_id, candidate)
        self._remember_plugin(candidate)
        self._publish_event("plugin.loaded", candidate)
        return candidate

    def unload_plugin(self, plugin_id: str) -> Plugin:
        """
        Unload a managed plugin by identifier.
        """
        plugin = self._require_loaded_plugin(plugin_id)
        plugin.lifecycle_state = "Unloaded"
        self._plugins.unregister(plugin_id)
        self._remember_plugin(plugin)
        self._publish_event("plugin.unloaded", plugin)
        return plugin

    def reload_plugin(self, plugin_id: str) -> Plugin:
        """
        Reload a managed plugin using unload and load boundaries.
        """
        plugin = self._require_loaded_plugin(plugin_id)
        self.unload_plugin(plugin_id)
        reloaded = self.load_plugin(plugin)
        self._publish_event("plugin.reloaded", reloaded)
        return reloaded

    def list_plugins(self) -> list[Plugin]:
        """
        Return loaded plugins in deterministic identifier order.
        """
        return self._ordered_plugins(self._plugins)

    def _normalize_for_validation(
        self,
        plugin: PluginInput,
    ) -> tuple[Plugin | None, dict[str, Any], str]:
        """
        Normalize plugin input for schema and dependency validation.
        """
        if isinstance(plugin, Plugin):
            return (
                plugin,
                plugin.manifest.to_dict(),
                plugin.plugin_id or "Plugin",
            )

        if isinstance(plugin, str):
            resolved = self._resolve_known_plugin(plugin)
            return (
                resolved,
                resolved.manifest.to_dict(),
                resolved.plugin_id,
            )

        if isinstance(plugin, PluginManifest):
            return (
                (
                    Plugin.from_manifest(plugin)
                    if plugin.plugin_id
                    else None
                ),
                plugin.to_dict(),
                plugin.plugin_id or "PluginManifest",
            )

        if isinstance(plugin, Mapping):
            manifest_data = dict(plugin)
            plugin_id = manifest_data.get("plugin_id")
            candidate = None

            if isinstance(plugin_id, str) and plugin_id:
                candidate = Plugin.from_manifest(
                    PluginManifest.from_dict(manifest_data)
                )

            return (
                candidate,
                manifest_data,
                plugin_id if isinstance(plugin_id, str) and plugin_id else "PluginManifest",
            )

        raise RegistryError(
            "Invalid plugin input: expected identifier, Plugin, "
            "PluginManifest, or mapping"
        )

    def _resolve_plugin(self, plugin: PluginInput) -> Plugin:
        """
        Resolve a plugin input to a concrete runtime plugin record.
        """
        if isinstance(plugin, Plugin):
            if not plugin.plugin_id:
                raise RegistryError(
                    "Invalid plugin manifest: plugin_id is required"
                )
            return plugin

        if isinstance(plugin, str):
            return self._resolve_known_plugin(plugin)

        if isinstance(plugin, PluginManifest):
            if not plugin.plugin_id:
                raise RegistryError(
                    "Invalid plugin manifest: plugin_id is required"
                )
            return Plugin.from_manifest(plugin)

        if isinstance(plugin, Mapping):
            manifest = PluginManifest.from_dict(plugin)

            if not manifest.plugin_id:
                raise RegistryError(
                    "Invalid plugin manifest: plugin_id is required"
                )

            return Plugin.from_manifest(manifest)

        raise RegistryError(
            "Invalid plugin input: expected identifier, Plugin, "
            "PluginManifest, or mapping"
        )

    def _resolve_known_plugin(self, plugin_id: str) -> Plugin:
        """
        Resolve a known plugin from loader-managed state.
        """
        plugin = self._plugins.get(plugin_id)

        if plugin is None:
            plugin = self._discovered.get(plugin_id)

        if plugin is None:
            raise ObjectNotFoundError(
                f"Plugin not found: '{plugin_id}'"
            )

        return plugin

    def _require_loaded_plugin(self, plugin_id: str) -> Plugin:
        """
        Resolve a loaded plugin or raise if it is missing.
        """
        plugin = self._plugins.get(plugin_id)

        if plugin is None:
            raise ObjectNotFoundError(
                f"Plugin not loaded: '{plugin_id}'"
            )

        return plugin

    def _build_dependency_resolver(
        self,
        plugin: Plugin,
    ) -> DependencyResolver:
        """
        Build a dependency resolver for a plugin candidate.
        """
        plugin_ids = set(self._discovered.keys())
        plugin_ids.update(self._plugins.keys())
        plugin_ids.add(plugin.plugin_id)

        resolver = _PluginDependencyResolver(
            plugin_ids=plugin_ids,
            object_registry=self._object_registry,
            capability_registry=self._capability_registry,
            service_registry=self._service_registry,
        )

        for dependency_id in plugin.dependencies:
            resolver.register_dependency(
                Dependency(
                    source=plugin.plugin_id,
                    target=dependency_id,
                )
            )

        return resolver

    def _plugin_from_path(self, manifest_path: Path) -> Plugin:
        """
        Build a plugin record from a manifest file.
        """
        try:
            with manifest_path.open("r", encoding="utf-8") as manifest_file:
                payload = json.load(manifest_file)
        except json.JSONDecodeError as exc:
            raise RegistryError(
                f"Invalid plugin manifest JSON: '{manifest_path}'"
            ) from exc

        if not isinstance(payload, Mapping):
            raise RegistryError(
                f"Invalid plugin manifest: '{manifest_path}' must be a mapping"
            )

        manifest = PluginManifest.from_dict(payload)

        if not manifest.plugin_id:
            raise RegistryError(
                f"Invalid plugin manifest: '{manifest_path}' is missing plugin_id"
            )

        return Plugin.from_manifest(
            manifest,
            path=manifest_path.parent,
            manifest_path=manifest_path,
        )

    def _iter_manifest_paths(self) -> list[Path]:
        """
        Return deterministic manifest paths under managed plugin roots.
        """
        manifest_paths: set[Path] = set()

        for root in self._plugin_roots:
            if root.is_file() and root.name == self._manifest_filename:
                manifest_paths.add(root.resolve())
                continue

            if not root.is_dir():
                continue

            manifest_paths.update(
                path.resolve()
                for path in root.rglob(self._manifest_filename)
                if path.is_file()
            )

        return sorted(manifest_paths)

    @staticmethod
    def _ordered_plugins(registry: BaseRegistry[Plugin]) -> list[Plugin]:
        """
        Return registry entries in deterministic identifier order.
        """
        ordered: list[Plugin] = []

        for plugin_id in registry.keys():
            plugin = registry.get(plugin_id)

            if plugin is None:
                raise RegistryError(
                    f"Plugin registry is inconsistent: '{plugin_id}'"
                )

            ordered.append(plugin)

        return ordered

    @staticmethod
    def _has_invalid_results(
        results: Iterable[ValidationResult],
    ) -> bool:
        """
        Determine whether any validation result is invalid.
        """
        return any(result.status == "invalid" for result in results)

    @staticmethod
    def _raise_for_invalid_results(
        plugin_id: str,
        results: Iterable[ValidationResult],
    ) -> None:
        """
        Reject a plugin load when validation fails.
        """
        invalid_messages = [
            f"{result.rule_id}: {result.message}"
            for result in results
            if result.status == "invalid"
        ]

        if invalid_messages:
            raise RegistryError(
                f"Plugin validation failed for '{plugin_id}': "
                + "; ".join(invalid_messages)
            )

    @staticmethod
    def _apply_validation_results(
        plugin: Plugin | None,
        results: list[ValidationResult],
    ) -> None:
        """
        Preserve validation results on a plugin record when available.
        """
        if plugin is None:
            return

        plugin.validation_results = tuple(results)

    def _remember_plugin(self, plugin: Plugin) -> None:
        """
        Store or replace a discovered plugin record.
        """
        if self._discovered.exists(plugin.plugin_id):
            self._discovered.update(plugin.plugin_id, plugin)
            return

        self._discovered.register(plugin.plugin_id, plugin)

    def _publish_event(
        self,
        event_type: str,
        plugin: Plugin,
        *,
        manifest_path: Path | None = None,
    ) -> None:
        """
        Publish a plugin lifecycle event when an event bus exists.
        """
        if self._event_bus is None:
            return

        payload: dict[str, object] = {
            "plugin_id": plugin.plugin_id,
            "name": plugin.name,
            "version": plugin.version,
            "lifecycle_state": plugin.lifecycle_state,
        }

        if plugin.path is not None:
            payload["path"] = str(plugin.path)

        if plugin.manifest_path is not None:
            payload["manifest_path"] = str(plugin.manifest_path)
        elif manifest_path is not None:
            payload["manifest_path"] = str(manifest_path)

        if plugin.dependency_order:
            payload["dependency_order"] = plugin.dependency_order

        self._event_bus.publish(
            Event(
                event_type=event_type,
                source="Runtime.PluginLoader",
                payload=payload,
            )
        )
