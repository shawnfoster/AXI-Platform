"""
AXI Platform Runtime

Validation Rules

Rule definitions used by the AXI Validation Framework.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from Runtime.Validation.result import ValidationResult

if TYPE_CHECKING:
    from Runtime.Validation.validator import Validator


RULE_TARGET_OBJECT = "object"
RULE_TARGET_METADATA = "metadata"
RULE_TARGET_SCHEMA = "schema"
RULE_TARGET_CONTRACT = "contract"
RULE_TARGET_DEPENDENCIES = "dependencies"
RULE_TARGET_RUNTIME = "runtime"

VALID_RULE_TARGETS = frozenset(
    {
        RULE_TARGET_OBJECT,
        RULE_TARGET_METADATA,
        RULE_TARGET_SCHEMA,
        RULE_TARGET_CONTRACT,
        RULE_TARGET_DEPENDENCIES,
        RULE_TARGET_RUNTIME,
    }
)


@dataclass(slots=True)
class ValidationRule:
    """
    Runtime validation rule definition.
    """

    rule_id: str
    target_type: str
    handler: callable
    order: int = 100
    enabled: bool = True

    def __post_init__(self) -> None:
        """
        Validate rule configuration.
        """
        if not isinstance(self.rule_id, str) or not self.rule_id:
            raise ValueError("Validation rule_id is required")

        if self.target_type not in VALID_RULE_TARGETS:
            raise ValueError(
                f"Invalid validation target type: '{self.target_type}'"
            )

        if not callable(self.handler):
            raise ValueError("Validation handler must be callable")

        if not isinstance(self.order, int):
            raise ValueError("Validation rule order must be an integer")

        if not isinstance(self.enabled, bool):
            raise ValueError("Validation rule enabled flag must be bool")

    def execute(
        self,
        target: Any,
        validator: "Validator",
    ) -> list[ValidationResult]:
        """
        Execute the rule for a target.
        """
        results = self.handler(target, validator)

        if isinstance(results, ValidationResult):
            return [results]

        if not isinstance(results, Iterable):
            raise ValueError(
                f"Validation rule '{self.rule_id}' did not return results"
            )

        return list(results)
