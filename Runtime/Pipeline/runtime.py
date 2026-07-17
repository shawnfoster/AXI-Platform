"""
AXI Platform Runtime

Pipeline Runtime State

Lifecycle state helpers for the M16 Pipeline Runtime.
"""

from __future__ import annotations

from Runtime.exceptions import RegistryError

INITIALIZED = "Initialized"
VALIDATING = "Validating"
READY = "Ready"
RUNNING = "Running"
PAUSED = "Paused"
COMPLETED = "Completed"
FAILED = "Failed"
CANCELLED = "Cancelled"

VALID_RUNTIME_STATES = frozenset(
    {
        INITIALIZED,
        VALIDATING,
        READY,
        RUNNING,
        PAUSED,
        COMPLETED,
        FAILED,
        CANCELLED,
    }
)

_OPERATION_TRANSITIONS = {
    "pause": (frozenset({RUNNING}), PAUSED),
    "resume": (frozenset({PAUSED}), RUNNING),
    "stop": (frozenset({RUNNING, PAUSED}), CANCELLED),
}


def ensure_runtime_state(state: str) -> str:
    """
    Validate a published pipeline runtime state.
    """
    if state not in VALID_RUNTIME_STATES:
        raise RegistryError(
            f"Invalid pipeline runtime state: '{state}'"
        )

    return state


def can_validate(state: str) -> bool:
    """
    Determine whether pipeline validation may begin from a state.
    """
    ensure_runtime_state(state)
    return state not in {RUNNING, PAUSED}


def can_execute(state: str) -> bool:
    """
    Determine whether pipeline execution may begin from a state.
    """
    ensure_runtime_state(state)
    return state in {
        INITIALIZED,
        READY,
        COMPLETED,
        FAILED,
        CANCELLED,
    }


def transition_runtime(current_state: str, operation: str) -> str:
    """
    Validate a public runtime lifecycle operation.
    """
    ensure_runtime_state(current_state)

    if operation not in _OPERATION_TRANSITIONS:
        raise RegistryError(
            f"Invalid pipeline lifecycle operation: '{operation}'"
        )

    allowed_states, next_state = _OPERATION_TRANSITIONS[operation]

    if current_state not in allowed_states:
        raise RegistryError(
            "Invalid lifecycle transition: "
            f"cannot {operation} pipeline from '{current_state}'"
        )

    return next_state
