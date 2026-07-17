"""
AXI Platform Runtime

Application Lifecycle

Registry-local lifecycle helpers for the M14 application APIs.
"""

from __future__ import annotations

from Runtime.exceptions import RegistryError

REGISTERED = "Registered"
RUNNING = "Running"
STOPPED = "Stopped"

_TRANSITIONS = {
    "start": (frozenset({REGISTERED, STOPPED}), RUNNING),
    "stop": (frozenset({RUNNING}), STOPPED),
    "restart": (frozenset({RUNNING}), RUNNING),
}


def transition_lifecycle(current_state: str, operation: str) -> str:
    """
    Validate an application lifecycle operation and return the next state.
    """
    allowed_states, next_state = _TRANSITIONS[operation]

    if current_state not in allowed_states:
        raise RegistryError(
            "Invalid lifecycle transition: "
            f"cannot {operation} application from '{current_state}'"
        )

    return next_state
