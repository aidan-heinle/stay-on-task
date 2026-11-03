"""
Represents user preferences in stay-on-task
"""

class Preference:
    def __init__(self, pid, freq, do_notify=True):
        self._preferenceID = pid
        self._reminder_frequency = freq
        self._do_notify = do_notify