"""
Represents one system notification
"""

class Notification:
    def __init__(self, nid, message, title, ts):
        self._notificationID = nid
        self._message = message
        self._title = title
        self._timestamp = ts

    def get_notification_id(self):
        return self._notificationID

    def get_message(self):
        return self._message

    def set_message(self, n):
        self._message = n

    def get_timestamp(self):
        return self._timestamp

    def set_timestamp(self, n):
        self._timestamp = n

    def get_title(self):
        return self._title
