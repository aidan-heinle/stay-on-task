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