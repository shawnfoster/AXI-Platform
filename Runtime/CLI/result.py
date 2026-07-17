"""
AXI Platform Runtime

CLI Result

Deterministic result payload for the M17 Runtime CLI.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

from Runtime.exceptions import RegistryError


def _serialize_value(value: Any) -> Any:
    """
    Convert nested runtime values to JSON-friendly structures.
    """
    if isinstance(value, Mapping):
        return {
            str(key): _serialize_value(nested_value)
            for key, nested_value in value.items()
        }

    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return [_serialize_value(item) for item in value]

    return value


@dataclass(frozen=True, slots=True)
class CLIResult:
    """
    Successful Runtime CLI result payload.
    """

    command: str
    status: str
    payload: Any

    def __post_init__(self) -> None:
        """
        Validate result envelope fields.
        """
        if not isinstance(self.command, str) or not self.command:
            raise RegistryError(
                "Invalid CLI result: command is required"
            )

        if not isinstance(self.status, str) or not self.status:
            raise RegistryError(
                "Invalid CLI result: status is required"
            )

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the Runtime CLI result envelope.
        """
        return {
            "command": self.command,
            "status": self.status,
            "payload": _serialize_value(self.payload),
        }
