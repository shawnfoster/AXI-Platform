"""
AXI Platform Runtime

Stage Execution

Execution record emitted by the M16 Pipeline Runtime.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

from Runtime.Pipeline.runtime import CANCELLED, COMPLETED, FAILED, PAUSED


@dataclass(slots=True)
class StageExecution:
    """
    Immutable-by-convention execution record for a stage attempt.
    """

    stage_id: str
    engine_id: str
    status: str
    started_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )
    completed_at: datetime | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    error: str = ""

    def mark_completed(self) -> None:
        """
        Complete the execution successfully.
        """
        self.status = COMPLETED
        self.completed_at = datetime.now(UTC)

    def mark_paused(self) -> None:
        """
        Mark the execution as paused.
        """
        self.status = PAUSED

    def mark_failed(self, message: str) -> None:
        """
        Mark the execution as failed.
        """
        self.status = FAILED
        self.error = message
        self.completed_at = datetime.now(UTC)

    def mark_cancelled(self, message: str) -> None:
        """
        Mark the execution as cancelled.
        """
        self.status = CANCELLED
        self.error = message
        self.completed_at = datetime.now(UTC)

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the execution record.
        """
        payload = {
            "stage_id": self.stage_id,
            "engine_id": self.engine_id,
            "status": self.status,
            "started_at": self.started_at.isoformat(),
            "metadata": dict(self.metadata),
        }

        if self.completed_at is not None:
            payload["completed_at"] = self.completed_at.isoformat()

        if self.error:
            payload["error"] = self.error

        return payload
