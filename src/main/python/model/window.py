"""
Represents an open window
"""

class Window:
    def __init__(self, wid, title, applicationID):
        self._windowID = wid
        self._window_title = title
        self._applicationID = applicationID

    def get_windowID(self):
        return self._windowID

    def get_window_title(self):
            return self._window_title

    def get_applicationID(self):
         return self._applicationID

    def set_window_title(self, title):
         self._window_title = title

    def set_applicationID(self, aid):
         self._applicationID = aid

         