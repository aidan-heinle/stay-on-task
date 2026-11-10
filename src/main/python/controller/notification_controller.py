from plyer import notification as system_notification

class NotificationController:
    def __init__(self):
        self._notifications = []

    def add_notification(self, n):
        self._notifications.append(n)

    # removes notification by ID, returns bool for success.
    def remove_notifications(self, nid):
        for notification in self._notifications:
            if notification.get_notification_id() == nid:
                self._notifications.remove(notification)
                return True

        return False

    # sends notification to system by ID, returns a bool for success.
    def send_notification(self, nid):
        for notification in self._notifications:
                    if notification.get_notification_id() == nid:

                        system_notification.notify(
                             title = notification.get_title(),
                             message = notification.get_message(),
                             timeout = 5 # default for now
                        )

                        self._notifications.remove(notification)
                        return True
        
        return False
