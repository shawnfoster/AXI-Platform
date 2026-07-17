"""
AXI Platform Runtime

Service Registry

Registry of AXI runtime services.
"""

from __future__ import annotations

from collections.abc import Iterable

from Runtime.CapabilityRegistry import CapabilityRegistry
from Runtime.Registry.base_registry import BaseRegistry
from Runtime.ServiceRegistry.service import Service
from Runtime.exceptions import (
    CapabilityNotFoundError,
    ObjectNotFoundError,
    RegistryError,
)


class ServiceRegistry(BaseRegistry[Service]):
    """
    Registry of services keyed by service identifier.
    """

    def __init__(
        self,
        capability_registry: CapabilityRegistry | None = None,
    ) -> None:
        """Initialize the service registry."""
        super().__init__()
        self._capability_registry = capability_registry

    def register(self, service: Service) -> None:
        """
        Register a service using its service identifier.
        """
        self._validate_service(service)
        super().register(service.service_id, service)
        self._register_capability_implementations(service)

    def register_service(self, service: Service) -> None:
        """
        Register a service.
        """
        self.register(service)

    def unregister(self, service_id: str) -> None:
        """
        Remove a service by identifier.
        """
        self._clear_capability_implementations(service_id)
        super().unregister(service_id)

    def unregister_service(self, service_id: str) -> None:
        """
        Remove a service by identifier.
        """
        self.unregister(service_id)

    def resolve_service(self, service_id: str) -> Service:
        """
        Resolve a registered service.
        """
        service = self.get(service_id)

        if service is None:
            raise ObjectNotFoundError(
                f"Service not found: '{service_id}'"
            )

        return service

    def has_service(self, service_id: str) -> bool:
        """
        Determine whether a service is registered.
        """
        return self.exists(service_id)

    def list_services(self) -> list[Service]:
        """
        Return services in deterministic identifier order.
        """
        return [self.resolve_service(service_id) for service_id in self.keys()]

    def update(self, service: Service) -> None:
        """
        Replace an existing service definition.
        """
        self._validate_service(service)
        self.resolve_service(service.service_id)
        self._clear_capability_implementations(service.service_id)
        super().update(service.service_id, service)
        self._register_capability_implementations(service)

    def update_service(self, service: Service) -> None:
        """
        Replace an existing service definition.
        """
        self.update(service)

    def load(self, services: Iterable[Service]) -> None:
        """
        Bulk load services.
        """
        for service in services:
            self.register(service)

    def _validate_service(self, service: Service) -> None:
        """
        Validate a service before registration or update.
        """
        if not isinstance(service, Service):
            raise RegistryError(
                "Invalid service registration: expected Service"
            )

        if service.namespace != "AXI-SVC":
            raise RegistryError(
                "Invalid service namespace: expected 'AXI-SVC'"
            )

        if service.object_type != "Service":
            raise RegistryError(
                "Invalid service object_type: expected 'Service'"
            )

        if not service.metadata:
            raise RegistryError(
                "Invalid service metadata: metadata is required"
            )

        if not service.lifecycle_state:
            raise RegistryError(
                "Invalid service metadata: lifecycle_state is required"
            )

        if self._capability_registry is None:
            return

        for capability_id in service.capabilities:
            if not self._capability_registry.exists(capability_id):
                raise CapabilityNotFoundError(
                    f"Capability not found: '{capability_id}'"
                )

    def _register_capability_implementations(self, service: Service) -> None:
        """
        Associate a service to its declared capabilities.
        """
        if self._capability_registry is None:
            return

        for capability_id in service.capabilities:
            self._capability_registry.add_implementation(
                capability_id,
                service,
            )

    def _clear_capability_implementations(self, service_id: str) -> None:
        """
        Remove a service from every capability implementation set.
        """
        if self._capability_registry is None:
            return

        for capability in self._capability_registry:
            capability.remove_object(service_id)
