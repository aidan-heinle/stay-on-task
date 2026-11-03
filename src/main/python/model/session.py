"""
Represents a session, i.e a period of time spent focusing on one task
"""

class Session:
    def __init__(self, id, start, tid, end=None, duration=None):
        self._sessionID = id,
        self._session_start_time = start,
        self._session_end_time = end,
        self._session_duration = duration,
        self._taskID = tid

    def get_session_id(self):
        return self._sessionID

    def get_session_start_time(self):
        return self._session_start_time

    def set_session_start_time(self, n):
        self._session_start_time = n

    def get_session_end_time(self):
        return self._session_end_time

    def set_session_end_time(self, n):
        self._session_end_time = n

    def get_session_duration(self):
        return self._session_duration

    def set_session_duration(self, n):
        self._session_duration = n

    def get_task_id(self):
        return self._taskID

    def set_task_id(self, n):
        self._taskID = n
