"""
Represents a user in the stay-on-task system.
"""

class User:
    def __init__(self, id, name, settingsID=None):
        self._ID = id
        self._name = name
        self._settingsID = settingsID

    def get_user_id(self):
        return self._ID

    def get_user_name(self):
        return self._name

    def get_settingsID(self):
        return self._settingsID

    def set_settingsID(self, n):
        self._settingsID = n


    
