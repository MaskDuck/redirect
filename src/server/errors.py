from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing_extensions import Self

class RedirectServerException(Exception):
    """Base class for every redirect server exception."""

class EnvironmentVariableNotFound(Exception):
    """Raised when an required environment variable can't be found."""
    def __init__(
        self: Self,
        *,
        key_not_found: str,
        message: str = """Error code {}: The enviroment variable {} wasn't found.
        Please double-check your .env file and environment variable setting.""",
        error_code: int = 40001
    ):
        super().__init__(message.format(error_code, key_not_found))
