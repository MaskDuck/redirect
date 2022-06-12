from __future__ import annotations
from logging import getLogger

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self
    from typing import Union

_log = getLogger("redirect")

class RedirectServerException(Exception):
    """Base class for every redirect server exception."""
    def __init__(self: Self, message: Union[str, int]):
        _log.error(message)
        
        

class EnvironmentVariableNotFound(Exception):
    """Raised when an required environment variable can't be found."""
    def __init__(
        self: Self,
        *,
        key_not_found: str,
        message: str = """Error code {}: The enviroment variable {} wasn't found.
        Please double-check your .env file and environment variable setting.""",
        error_code: int = 40401
    ):
        super().__init__(message.format(error_code, key_not_found))


class RedirectNotFound(Exception):
    """Raised when I can't found the destination for the redirect."""
    def __init__(
        self: Self,
        *,
        redirect_name: str,
        message: str = "Error code {}: Redirect name {} doesn't reach to any destination.",
        error_code: int = 40402
    ):
        _log.info(message.format(error_code, redirect_name))