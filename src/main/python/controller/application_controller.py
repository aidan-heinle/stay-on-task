
import psutil

class ApplicationController:

    def __init__(self):
        self._applications = []

    def add_application(self, app):
        self._applications.append(app)

    def get_application(self, aid):
        for app in self._applications:
            if app.get_application_id() == aid:
                return app
        return None

    def get_application_by_exe(self, exe):
        for app in self._applications:
            if app.get_exe_name().lower() == exe.lower():
                return app
        return None

    def get_application_by_pid(self, pid):
        exe = self.get_exe_name_by_pid(pid)
        return self.get_application_by_exe(exe) if exe else None

    def get_exe_name_by_pid(self, pid):
        """None means the process could not be read, not an unregistered app."""
        try:
            process = psutil.Process(pid)
            return process.name()

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return None
