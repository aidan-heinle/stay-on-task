"""
Represents a task that the User us currently supposed to be working on in the stay-on-task system.
"""

from enum import Enum

class Task_Status(Enum):
    READY = 1
    IN_PROGRESS = 2
    COMPLETED = 3 

class Task:
    def __init__(self, id, title, desc, start, end=None, status=Task_Status.READY):
        self._taskID = id
        self._title = title
        self._description = desc
        self._start_time = start
        self._end_time = end
        self._status = status # enumeration class Task_Status

    