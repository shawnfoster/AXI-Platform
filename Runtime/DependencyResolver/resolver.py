"""
AXI Platform Runtime

Dependency Resolver

Deterministic dependency graph resolver for runtime identifiers.
"""

from __future__ import annotations

from Runtime.CapabilityRegistry import CapabilityRegistry
from Runtime.DependencyResolver.dependency import Dependency
from Runtime.EventBus import Event, EventBus
from Runtime.ObjectModel.platform_object import PlatformObject
from Runtime.ObjectRegistry import ObjectRegistry
from Runtime.Registry.base_registry import BaseRegistry
from Runtime.ServiceRegistry import ServiceRegistry
from Runtime.exceptions import DependencyError


class DependencyResolver:
    """
    Deterministic dependency resolver.
    """

    def __init__(
        self,
        *,
        object_registry: ObjectRegistry | None = None,
        capability_registry: CapabilityRegistry | None = None,
        service_registry: ServiceRegistry | None = None,
        event_bus: EventBus | None = None,
    ) -> None:
        """Initialize the dependency resolver."""
        self._dependencies = BaseRegistry[Dependency]()
        self._object_registry = object_registry
        self._capability_registry = capability_registry
        self._service_registry = service_registry
        self._event_bus = event_bus

    def register_dependency(self, dependency: Dependency) -> None:
        """
        Register a dependency relationship.
        """
        self._validate_dependency_instance(dependency)
        self._validate_identifier_exists(dependency.source)
        self._validate_identifier_exists(dependency.target)

        self._dependencies.register(dependency.dependency_id, dependency)

        try:
            self.validate_dependencies()
        except Exception:
            self._dependencies.unregister(dependency.dependency_id)
            raise

        self._publish_event(
            "dependency.registered",
            {
                "dependency_id": dependency.dependency_id,
                "source": dependency.source,
                "target": dependency.target,
            },
        )

    def unregister_dependency(self, dependency_id: str) -> None:
        """
        Remove a dependency relationship.
        """
        dependency = self._dependencies.get(dependency_id)

        if dependency is None:
            return

        self._dependencies.unregister(dependency_id)
        self._publish_event(
            "dependency.unregistered",
            {
                "dependency_id": dependency.dependency_id,
                "source": dependency.source,
                "target": dependency.target,
            },
        )

    def resolve(
        self,
        source: str | PlatformObject,
    ) -> list[str]:
        """
        Resolve dependencies for a single runtime identifier.
        """
        source_id = Dependency.normalize_reference(source)
        self._validate_identifier_exists(source_id)
        self.validate_dependencies()

        ordered: list[str] = []
        visiting = {source_id}
        visited: set[str] = set()
        self._visit_dependencies(
            source_id,
            visiting,
            visited,
            ordered,
        )

        self._publish_event(
            "dependency.resolved",
            {
                "source": source_id,
                "resolved": tuple(ordered),
            },
        )
        return ordered

    def resolve_all(self) -> list[str]:
        """
        Resolve the full dependency graph in deterministic order.
        """
        self.validate_dependencies()

        ordered: list[str] = []
        visiting: set[str] = set()
        visited: set[str] = set()

        for node_id in self._graph_nodes():
            self._visit_node(node_id, visiting, visited, ordered)

        self._publish_event(
            "dependency.resolved_all",
            {
                "resolved": tuple(ordered),
            },
        )
        return ordered

    def validate_dependencies(self) -> bool:
        """
        Validate every registered dependency.
        """
        for dependency in self.list_dependencies():
            self._validate_identifier_exists(dependency.source)
            self._validate_identifier_exists(dependency.target)

        visiting: set[str] = set()
        visited: set[str] = set()
        ordered: list[str] = []

        for node_id in self._graph_nodes():
            self._visit_node(node_id, visiting, visited, ordered)

        return True

    def list_dependencies(self) -> list[Dependency]:
        """
        Return registered dependencies in deterministic order.
        """
        return [
            self._require_dependency(dependency_id)
            for dependency_id in self._dependencies.keys()
        ]

    def _require_dependency(self, dependency_id: str) -> Dependency:
        """
        Retrieve a registered dependency.
        """
        dependency = self._dependencies.get(dependency_id)

        if dependency is None:
            raise DependencyError(
                f"Dependency registry is inconsistent: '{dependency_id}'"
            )

        return dependency

    @staticmethod
    def _validate_dependency_instance(dependency: Dependency) -> None:
        """
        Validate a dependency instance before registration.
        """
        if not isinstance(dependency, Dependency):
            raise DependencyError(
                "Invalid dependency definition: expected Dependency"
            )

    def _validate_identifier_exists(self, identifier: str) -> None:
        """
        Ensure an identifier exists in the available runtime foundations.
        """
        if self._identifier_exists(identifier):
            return

        raise DependencyError(
            f"Missing dependency target: '{identifier}'"
        )

    def _identifier_exists(self, identifier: str) -> bool:
        """
        Determine whether an identifier is known to the runtime.
        """
        if self._object_registry is not None and self._object_registry.exists(
            identifier
        ):
            return True

        if self._service_registry is not None and self._service_registry.has_service(
            identifier
        ):
            return True

        if self._capability_registry is not None and self._capability_registry.exists(
            identifier
        ):
            return True

        return False

    def _dependencies_for(self, source_id: str) -> list[Dependency]:
        """
        Return direct dependencies for a source identifier.
        """
        return [
            dependency
            for dependency in self.list_dependencies()
            if dependency.source == source_id
        ]

    def _graph_nodes(self) -> list[str]:
        """
        Return every node participating in the dependency graph.
        """
        nodes = {
            dependency.source
            for dependency in self.list_dependencies()
        }
        nodes.update(
            dependency.target
            for dependency in self.list_dependencies()
        )
        return sorted(nodes)

    def _visit_dependencies(
        self,
        source_id: str,
        visiting: set[str],
        visited: set[str],
        ordered: list[str],
    ) -> None:
        """
        Resolve transitive dependencies for a single source node.
        """
        for dependency in self._dependencies_for(source_id):
            self._visit_node(
                dependency.target,
                visiting,
                visited,
                ordered,
            )

    def _visit_node(
        self,
        node_id: str,
        visiting: set[str],
        visited: set[str],
        ordered: list[str],
    ) -> None:
        """
        Perform deterministic DFS for cycle detection and ordering.
        """
        if node_id in visited:
            return

        if node_id in visiting:
            raise DependencyError(
                f"Circular dependency detected: '{node_id}'"
            )

        visiting.add(node_id)

        for dependency in self._dependencies_for(node_id):
            self._visit_node(
                dependency.target,
                visiting,
                visited,
                ordered,
            )

        visiting.remove(node_id)
        visited.add(node_id)
        ordered.append(node_id)

    def _publish_event(
        self,
        event_type: str,
        payload: dict[str, object],
    ) -> None:
        """
        Publish a dependency lifecycle event when an event bus exists.
        """
        if self._event_bus is None:
            return

        self._event_bus.publish(
            Event(
                event_type=event_type,
                source="Runtime.DependencyResolver",
                payload=payload,
            )
        )
