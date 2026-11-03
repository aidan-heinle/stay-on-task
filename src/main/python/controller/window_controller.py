import win32gui
import win32process

from model.window import Window

class WindowController:
    def __init__(self):
        self._windows = []

    def get_current_window_id(self):
        return win32gui.GetForegroundWindow()

    def get_current_window(self):
        window_id = self.get_current_window_id()
        if not window_id:
            return None

        title = win32gui.GetWindowText(window_id)
        _, process_id = win32process.GetWindowThreadProcessId(window_id)

        return Window(window_id, title, process_id)

    
