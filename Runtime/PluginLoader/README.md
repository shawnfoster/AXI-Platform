# AXI Plugin Loader

`Runtime/PluginLoader/` implements the governed `M13 Plugin Loader`
runtime boundary.

The loader:

- discovers plugin manifests from loader-managed roots
- validates manifests against `AXI-SCH-009`
- validates dependency references through `DependencyResolver`
- loads, unloads, reloads, and lists loader-managed plugins
- preserves manifest metadata and exposes lifecycle state

The implementation does not introduce:

- a new plugin `PlatformObject` type
- a new registry hierarchy
- remote or distributed discovery
- behavior beyond the published `M13` lifecycle boundary
