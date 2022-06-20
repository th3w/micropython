# MicroPython uasyncio module
# MIT license; Copyright (c) 2019 Damien P. George

from .core import *

__version__ = (3, 0, 0)

_attrs = {
    "wait_for": "funcs",
    "wait_for_ms": "funcs",
    "gather": "funcs",
    "Event": "event",
    "ThreadSafeFlag": "event",
    "Lock": "lock",
    "open_connection": "stream",
    "start_server": "stream",
    "run_server": "stream",
    "StreamReader": "stream",
    "StreamWriter": "stream",
    "TaskGroup": "taskgroup",
}


# Lazy loader, effectively does:
#   global attr
#   from .mod import attr
def __getattr__(attr):
    mod = _attrs.get(attr, None)
    if mod is None:
        value = __import__(attr, None, None, True, 1)
    else:
        value = getattr(__import__(mod, None, None, True, 1), attr)
    globals()[attr] = value
    return value
