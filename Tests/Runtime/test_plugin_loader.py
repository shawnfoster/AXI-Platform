from __future__ import annotations

import json
from pathlib import Path

import pytest

from Runtime.CapabilityRegistry import Capability, CapabilityRegistry
from Runtime.EventBus import Event, EventBus, Subscriber
from Runtime.PluginLoader import PluginLoader
from Runtime.exceptions import (
    DuplicateRegistrationError,
    RegistryError,
)


def build_capability(i: int) -> Capability:
    return Capability(
        capability_id=f"CAP-{i:03d}",
        name=f"Capability {i}",
        description=f"Capability description {i}",
        version="1.0",
        status="Approved",
    )


def build_manifest(
    plugin_id: str,
    *,
    dependencies: list[str] | None = None,
    capabilities: list[str] | None = None,
) -> dict[str, object]:
    return {
        "plugin_id": plugin_id,
        "name": f"Plugin {plugin_id}",
        "version": "1.0.0",
        "author": "AXI Platform",
        "description": f"Runtime plugin {plugin_id}",
        "capabilities": capabilities or [],
        "dependencies": dependencies or [],
        "lifecycle_state": "Discovered",
    }


def write_plugin(
    root: Path,
    directory_name: str,
    manifest: dict[str, object],
) -> Path:
    plugin_dir = root / directory_name
    plugin_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = plugin_dir / "plugin.json"
    manifest_path.write_text(
        json.dumps(manifest),
        encoding="utf-8",
    )
    return manifest_path


def test_plugin_loader_discovers_plugins_in_deterministic_order(
    tmp_path: Path,
) -> None:
    plugin_root = tmp_path / "plugins"
    write_plugin(plugin_root, "beta", build_manifest("plugin-beta"))
    write_plugin(plugin_root, "alpha", build_manifest("plugin-alpha"))

    loader = PluginLoader(plugin_roots=[plugin_root])

    discovered = loader.discover_plugins()

    assert [plugin.plugin_id for plugin in discovered] == [
        "plugin-alpha",
        "plugin-beta",
    ]
    assert all(plugin.manifest_path is not None for plugin in discovered)


def test_plugin_loader_rejects_duplicate_discovered_plugin_ids(
    tmp_path: Path,
) -> None:
    plugin_root = tmp_path / "plugins"
    write_plugin(plugin_root, "first", build_manifest("plugin-dup"))
    write_plugin(plugin_root, "second", build_manifest("plugin-dup"))

    loader = PluginLoader(plugin_roots=[plugin_root])

    with pytest.raises(DuplicateRegistrationError):
        loader.discover_plugins()


def test_plugin_loader_validates_manifest_schema_failures() -> None:
    loader = PluginLoader()

    results = loader.validate_plugin(
        {
            "plugin_id": "plugin-invalid",
            "version": "1.0.0",
            "author": "AXI Platform",
            "description": "Invalid manifest",
            "capabilities": [],
            "dependencies": [],
        }
    )

    assert any(
        result.rule_id == "schema.evaluate"
        and result.status == "invalid"
        for result in results
    )


def test_plugin_loader_validates_plugin_dependencies_against_discovered_plugins(
    tmp_path: Path,
) -> None:
    plugin_root = tmp_path / "plugins"
    write_plugin(
        plugin_root,
        "base",
        build_manifest("plugin-base"),
    )
    write_plugin(
        plugin_root,
        "dependent",
        build_manifest(
            "plugin-dependent",
            dependencies=["plugin-base"],
        ),
    )

    loader = PluginLoader(plugin_roots=[plugin_root])
    loader.discover_plugins()

    plugin = loader.load_plugin("plugin-dependent")

    assert plugin.lifecycle_state == "Loaded"
    assert plugin.dependency_order == ("plugin-base",)
    assert [loaded.plugin_id for loaded in loader.list_plugins()] == [
        "plugin-dependent"
    ]


def test_plugin_loader_validates_dependencies_against_runtime_registries() -> None:
    capability_registry = CapabilityRegistry()
    capability = build_capability(1)
    capability_registry.register(capability)
    loader = PluginLoader(
        capability_registry=capability_registry,
    )

    plugin = loader.load_plugin(
        build_manifest(
            "plugin-capability",
            dependencies=[capability.capability_id],
        )
    )

    assert plugin.dependency_order == (capability.capability_id,)


def test_plugin_loader_rejects_unresolved_dependencies() -> None:
    loader = PluginLoader()

    results = loader.validate_plugin(
        build_manifest(
            "plugin-missing-dependency",
            dependencies=["plugin-unknown"],
        )
    )

    assert any(
        result.rule_id == "dependencies.validate"
        and result.status == "invalid"
        for result in results
    )

    with pytest.raises(RegistryError):
        loader.load_plugin(
            build_manifest(
                "plugin-missing-dependency",
                dependencies=["plugin-unknown"],
            )
        )


def test_plugin_loader_unloads_and_reloads_plugins_and_publishes_events(
    tmp_path: Path,
) -> None:
    plugin_root = tmp_path / "plugins"
    write_plugin(plugin_root, "reloadable", build_manifest("plugin-reload"))
    event_bus = EventBus()
    received: list[Event] = []

    event_bus.subscribe(
        Subscriber(
            subscriber_id="SUB-PLUGIN",
            event_types=(
                "plugin.loaded",
                "plugin.unloaded",
                "plugin.reloaded",
            ),
            handler=lambda event: received.append(event),
        )
    )

    loader = PluginLoader(
        plugin_roots=[plugin_root],
        event_bus=event_bus,
    )
    loader.discover_plugins()
    loader.load_plugin("plugin-reload")

    unloaded = loader.unload_plugin("plugin-reload")
    reloaded = loader.load_plugin(unloaded)
    loader.reload_plugin(reloaded.plugin_id)

    assert unloaded.lifecycle_state == "Loaded"
    assert reloaded.lifecycle_state == "Loaded"
    assert [event.event_type for event in received] == [
        "plugin.loaded",
        "plugin.unloaded",
        "plugin.loaded",
        "plugin.unloaded",
        "plugin.loaded",
        "plugin.reloaded",
    ]
