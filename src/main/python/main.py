from model import *
from controller import *

"""
def main():
    preferences = Preference(1, 30)
    user = User(1, "Aidan", preferences.get_preference_id())
    application = Application(1, "Visual Studio Code", "Code.exe")
    window = Window(1, "main.py - Visual Studio Code", application.get_application_id())
    task = Task(1, "Finish project", "Work on stay-on-task", "9:00 AM")
    session = Session(1, "9:00 AM", task.get_task_id())
    notification = Notification(1, "Time to focus!", "9:30 AM")

    task.set_status(Task_Status.IN_PROGRESS)
    session.set_session_end_time("9:30 AM")
    session.set_session_duration(30)
    notification.set_message("Focus session complete!")

    print(f"User: {user.get_user_name()}")
    print(f"Application: {application.get_application_name()}")
    print(f"Window: {window.get_window_title()}")
    print(f"Task: {task.get_title()} ({task.get_status().name})")
    print(f"Session duration: {session.get_session_duration()} minutes")
    print(f"Notifications enabled: {preferences.get_do_notify()}")
    print(f"Notification: {notification.get_message()}")
"""

def main():
    notif = Notification(1, "Time to focus!", "Focus assistant", "9:30 AM")
    nc = NotificationController()
    nc.add_notification(notif)
    nc.send_notification(1)

    window_controller = WindowController()
    current_window = window_controller.get_current_window()

    if current_window:
        print(f"Current window ID: {current_window.get_windowID()}")
        print(f"Current window title: {current_window.get_window_title()}")

if __name__ == "__main__":
    main()
