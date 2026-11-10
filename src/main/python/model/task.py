"""
Represents a task that the User us currently supposed to be working on in the stay-on-task system.
"""

from enum import Enum

class Task_Status(Enum):
    READY = 1
    IN_PROGRESS = 2
    COMPLETED = 3 

class Task:
    def __init__(self, id, title, desc, start, end=None, status=Task_Status.READY, allowed_applications=None):
        self._taskID = id
        self._title = title
        self._description = desc
        self._start_time = start
        self._end_time = end
        self._status = status # enumeration class Task_Status
        self._allowed_applications = set(allowed_applications or ()) # application IDs

    def get_task_id(self):
        return self._taskID

    def get_title(self):
        return self._title

    def set_title(self, n):
        self._title = n

    def get_description(self):
        return self._description

    def set_description(self, n):
        self._description = n

    def get_start_time(self):
        return self._start_time

    def set_start_time(self, n):
        self._start_time = n

    def get_end_time(self):
        return self._end_time

    def set_end_time(self, n):
        self._end_time = n

    def get_status(self):
        return self._status

    def set_status(self, n):
        self._status = n


    def add_allowed_application(self, aid):
        self._allowed_applications.add(aid)

    def remove_allowed_application(self, aid):
        self._allowed_applications.discard(aid)

    def get_allowed_application(self, aid):
        return aid if aid in self._allowed_applications else None

    def is_application_allowed(self, aid):
        return aid in self._allowed_applications
