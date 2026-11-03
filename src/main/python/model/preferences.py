"""
Represents user preferences in stay-on-task
"""

class Preference:
    def __init__(self, pid, freq, do_notify=True):
        self._preferenceID = pid
        self._reminder_frequency = freq
        self._do_notify = do_notify

    def get_preference_id(self):
        return self._preferenceID

    def get_reminder_frequency(self):
        return self._reminder_frequency

    def set_reminder_frequency(self, n):
        self._reminder_frequency = n

    def get_do_notify(self):
        return self._do_notify

    def set_do_notify(self, n):
        self._do_notify = n
