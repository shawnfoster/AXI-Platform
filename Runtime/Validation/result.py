"""
AXI Platform Runtime

Validation Result

Immutable validation result returned by the AXI Validation Framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


VALIDATION_STATUSES = frozenset({"valid", "invalid"})
VALIDATION_SEVERITIES = frozenset({"info", "warning", "error"})


@dataclass(frozen=True, slots=True)
class ValidationResult:
    """
    Immutable validation result.
    """

    status: str
    severity: str
    rule_id: str
    message: str
    source: str
    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def __post_init__(self) -> None:
        """
        Validate immutable result fields.
        """
        if self.status not in VALIDATION_STATUSES:
            raise ValueError(
                f"Invalid validation status: '{self.status}'"
            )

        if self.severity not in VALIDATION_SEVERITIES:
            raise ValueError(
                f"Invalid validation severity: '{self.severity}'"
            )

        if not isinstance(self.rule_id, str) or not self.rule_id:
            raise ValueError("Validation rule_id is required")

        if not isinstance(self.message, str) or not self.message:
            raise ValueError("Validation message is required")

        if not isinstance(self.source, str) or not self.source:
            raise ValueError("Validation source is required")

        if not isinstance(self.timestamp, datetime):
            raise ValueError(
                "Validation timestamp must be a datetime value"
            )
