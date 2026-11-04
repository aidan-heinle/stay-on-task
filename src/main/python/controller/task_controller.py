class TaskController:
    def __init__(self):
        self._tasks = []
        self._current_task = None


    def add_task(self, task):
        self._tasks.append(task)


    def remove_task(self, tid):
        for task in self._tasks:
            if task.get_taskID == tid:
                self._tasks.remove(task)
                return True

        return False

    def get_task(self, tid):
        pass

    def set_current_task(self, tid):
        pass

    def get_current_task(self, tid):
        pass
