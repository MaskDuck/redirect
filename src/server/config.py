from os import getenv
from contextlib import suppress
from typing import TYPE_CHECKING
from __future__ import annotations

from errors import EnvironmentVariableNotFound
with suppress(ImportError):
    import dotenv
    dotenv.load_dotenv()

if TYPE_CHECKING:
    from typing import Any, Optional

def _force_getenv(key: str, default: Any, raise_if_none: bool = False):
    result: Optional[str] = getenv(key, default=default)
    if (result == None) and (raise_if_none):
        raise EnvironmentVariableNotFound(key_not_found=key)
    return result

# required
MONGODB_URL = _force_getenv("MONGODB_URL", raise_if_none=True)

# optional
AUTHORIZATION_KEY = _force_getenv("AUTHORIZATION_KEY")



