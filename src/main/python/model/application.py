"""
Represents a PC application to be monitored, like vsCode or something
"""

class Application:
    def __init__(self, aid, name, exe):
        self._applicationID = aid
        self._application_name = name
        self._exe_name = exe

    def get_application_id(self):
        return self._applicationID

    def get_application_name(self):
        return self._application_name

    def set_application_name(self, n):
        self._application_name = n

    def get_exe_name(self):
        return self._exe_name

    def set_exe_name(self, n):
        self._exe_name = n
