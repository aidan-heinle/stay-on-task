from datetime import datetime

from controller import (
    ApplicationController, NotificationController, TaskController, WindowController,
)
from model import Application, Preference, Task, Task_Status
from service.activity_monitor import ActivityMonitor


def main():
    # Add executable names here until the GUI provides app selection.
    allowed_executables = ["Code.exe"]
    applications = ApplicationController()
    task = Task(1, "Work on project", "Focus on stay-on-task", datetime.now())
    for aid, exe in enumerate(allowed_executables, start=1):
        applications.add_application(Application(aid, exe, exe))
        task.add_allowed_application(aid)

    tasks = TaskController()
    tasks.add_task(task)
    tasks.set_current_task(task.get_task_id())
    task.set_status(Task_Status.IN_PROGRESS)

    preferences = Preference(1, freq=30, do_notify=True)
    monitor = ActivityMonitor(
        tasks, WindowController(), applications, NotificationController(), preferences,
        poll_interval=1, grace_period=5,
    )
    print(f"Monitoring task: {task.get_title()}")
    print(f"Allowed apps: {', '.join(allowed_executables)}")
    print("Checking every second; reminders after 5 seconds, then every 30 seconds.")
    print("Press Ctrl+C to stop.")
    try:
        monitor.run()
    except KeyboardInterrupt:
        pass
    finally:
        monitor.stop()
        task.set_status(Task_Status.READY)
        print("Monitoring stopped.")


if __name__ == "__main__":
    main()
