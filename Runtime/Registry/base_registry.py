"""
AXI Platform Runtime

Base Registry

Generic registry implementation used by all runtime registries.

Author: AXI Platform
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Generic, TypeVar

from Runtime.exceptions import DuplicateRegistrationError

T = TypeVar("T")


class BaseRegistry(Generic[T]):
    """
    Generic keyed registry.

    This class provides the common runtime behavior shared by all
    AXI registries. Specialized registries should inherit from this
    class and expose domain-specific registration methods.
    """

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._items: dict[str, T] = {}

    def register(self, key: str, item: T) -> None:
        """
        Register an item using a unique key.

        Raises:
            DuplicateRegistrationError:
                If the key already exists.
        """
        if key in self._items:
            raise DuplicateRegistrationError(
                f"Duplicate registry key: '{key}'"
            )

        self._items[key] = item

    def unregister(self, key: str) -> None:
        """
        Remove an item from the registry.

        Missing keys are ignored.
        """
        self._items.pop(key, None)

    def get(self, key: str) -> T | None:
        """
        Retrieve an item by key.

        Returns:
            The registered item or None.
        """
        return self._items.get(key)

    def exists(self, key: str) -> bool:
        """
        Determine whether a key exists.
        """
        return key in self._items

    def keys(self) -> list[str]:
        """
        Return all registry keys.
        """
        return sorted(self._items.keys())

    def values(self) -> list[T]:
        """
        Return all registered items.
        """
        return list(self._items.values())

    def items(self) -> list[tuple[str, T]]:
        """
        Return all registry entries.
        """
        return list(self._items.items())

    def count(self) -> int:
        """
        Return the number of registered items.
        """
        return len(self._items)

    def clear(self) -> None:
        """
        Remove every registered item.
        """
        self._items.clear()

    def load(self, items: Iterable[tuple[str, T]]) -> None:
        """
        Bulk-load registry entries.

        Existing duplicate keys will raise
        DuplicateRegistrationError.
        """
        for key, item in items:
            self.register(key, item)

    def __contains__(self, key: str) -> bool:
        """
        Support:

            if "OBJ-000001" in registry
        """
        return key in self._items

    def __len__(self) -> int:
        """
        Support:

            len(registry)
        """
        return len(self._items)

    def __iter__(self):
        """
        Iterate over registry values.

            for obj in registry:
                ...
        """
        return iter(self._items.values())

    def __repr__(self) -> str:
        """
        Developer representation.
        """
        return (
            f"{self.__class__.__name__}"
            f"(count={len(self._items)})"
        )