"""
AXI Platform Runtime

Exceptions

Canonical runtime exceptions used throughout the AXI Platform.
"""


class AXIRuntimeError(Exception):
    """Base exception for all AXI runtime errors."""


class RegistryError(AXIRuntimeError):
    """Base registry exception."""


class DuplicateRegistrationError(RegistryError):
    """Raised when attempting to register an existing object."""


class ObjectNotFoundError(RegistryError):
    """Raised when an object cannot be located."""


class CapabilityError(AXIRuntimeError):
    """Base capability exception."""


class CapabilityNotFoundError(CapabilityError):
    """Raised when a capability cannot be located."""


class DependencyError(AXIRuntimeError):
    """Raised when dependency resolution fails."""