import fastapi
import logging


_log = logging.getLogger("redirect")

_log.setLevel(logging.INFO)
_log.addHandler(logging.StreamHandler())