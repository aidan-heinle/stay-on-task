import logging
import time
from datetime import datetime
from threading import Event

from model import Notification, Task_Status

class ActivityMonitor:
    def __init__(self, task_controller, window_controller, application_controller,
                 notification_controller, preferences, poll_interval=1,
                 grace_period=5, clock=time.monotonic):
        self.tasks = task_controller
        self.windows = window_controller
        self.applications = application_controller
        self.notifications = notification_controller
        self.preferences = preferences
        self.poll_interval = poll_interval
        self.grace_period = grace_period
        self.clock = clock
        self._stop_event = Event()
        self._task = None
        self._off_task_since = None
        self._last_notification = None
        self._notification_id = 0

    def _reset_distraction(self):
        self._off_task_since = None
        self._last_notification = None

    def check_activity(self):
        """Check once; return idle, unknown, allowed, or disallowed."""
        task = self.tasks.get_current_task()
        if task is not self._task:
            self._task = task
            self._reset_distraction()
        if task is None or task.get_status() != Task_Status.IN_PROGRESS:
            self._reset_distraction()
            return "idle"

        window = self.windows.get_current_window()
        exe = (self.applications.get_exe_name_by_pid(window.get_process_id())
               if window else None)
        if not exe:
            # Require a fresh grace period after an unreadable foreground app.
            self._off_task_since = None
            return "unknown"

        app = self.applications.get_application_by_exe(exe)
        if app and task.is_application_allowed(app.get_application_id()):
            self._reset_distraction()
            return "allowed"

        now = self.clock()
        if self._off_task_since is None:
            self._off_task_since = now
        if not self.preferences.get_do_notify():
            return "disallowed"
        # Reminder frequency is measured in seconds.
        cooldown = self.preferences.get_reminder_frequency()
        if (now - self._off_task_since >= self.grace_period
                and (self._last_notification is None
                     or now - self._last_notification >= cooldown)):
            self._last_notification = now
            self._notification_id += 1
            notification = Notification(
                self._notification_id,
                f'{exe} is not allowed for "{task.get_title()}". Time to refocus!',
                "Stay On Task", datetime.now())
            self.notifications.add_notification(notification)
            try:
                self.notifications.send_notification(self._notification_id)
            except Exception:
                # A desktop notification failure should not stop monitoring.
                logging.exception("Could not send focus reminder")
                self.notifications.remove_notifications(self._notification_id)
        return "disallowed"

    def run(self):
        """Run until stop() is called or the console receives Ctrl+C."""
        while not self._stop_event.is_set():
            self.check_activity()
            self._stop_event.wait(self.poll_interval)

    def stop(self):
        self._stop_event.set()
