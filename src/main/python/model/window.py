"""
Represents an open window
"""

class Window:
    def __init__(self, wid, title, process_id):
        self._windowID = wid
        self._window_title = title
        self._process_id = process_id

    def get_windowID(self):
        return self._windowID

    def get_window_title(self):
            return self._window_title

    def get_process_id(self):
         return self._process_id

    def set_window_title(self, title):
         self._window_title = title

    def set_process_id(self, pid):
         self._process_id = pid

