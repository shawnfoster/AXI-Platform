"""
AXI Platform Runtime

API Result

Deterministic result payload for the M18 Runtime API.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from Runtime.CLI.result import CLIResult
from Runtime.exceptions import RegistryError


@dataclass(frozen=True, slots=True)
class APIResult:
    """
    Successful Runtime API result payload.
    """

    operation: str
    status: str
    payload: Any

    def __post_init__(self) -> None:
        """
        Validate result envelope fields.
        """
        if not isinstance(self.operation, str) or not self.operation:
            raise RegistryError(
                "Invalid API result: operation is required"
            )

        if not isinstance(self.status, str) or not self.status:
            raise RegistryError(
                "Invalid API result: status is required"
            )

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the Runtime API result envelope.
        """
        result = CLIResult(
            command=self.operation,
            status=self.status,
            payload=self.payload,
        ).to_dict()
        return {
            "operation": result["command"],
            "status": result["status"],
            "payload": result["payload"],
        }
