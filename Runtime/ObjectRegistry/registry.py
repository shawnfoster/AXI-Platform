"""
AXI Platform Runtime

Object Registry

Registry of PlatformObjects.
"""

from __future__ import annotations

from collections.abc import Iterable

from Runtime.ObjectModel.platform_object import PlatformObject
from Runtime.Registry.base_registry import BaseRegistry


class ObjectRegistry(BaseRegistry[PlatformObject]):
    """
    Registry of PlatformObjects.
    """

    def register(self, obj: PlatformObject) -> None:
        """
        Register a PlatformObject using its object_id.
        """
        super().register(obj.object_id, obj)

    def load(self, objects: Iterable[PlatformObject]) -> None:
        """
        Bulk load PlatformObjects.
        """
        for obj in objects:
            self.register(obj)