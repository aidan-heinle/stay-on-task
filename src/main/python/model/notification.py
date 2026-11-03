"""
Represents one system notification
"""

class Notification:
    def __init__(self, nid, message, ts):
        self._notificationID = nid
        self._message = message
        self._timestamp = ts