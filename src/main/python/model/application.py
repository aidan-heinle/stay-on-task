"""
Represents a PC application to be monitored, like vsCode or something
"""

class Application:
    def __init__(self, aid, name, exe):
        self._applicationID = aid
        self._application_name = name
        self._exe_name = exe

    