"""
:author @Surge
:contributors @Surge

Execution type enum

:used
    - utils/worker_logs.py
"""

from enum import IntEnum


class ExecutionType(IntEnum):
    TEXT_COMMAND = 1
    SLASH_COMMAND = 2
