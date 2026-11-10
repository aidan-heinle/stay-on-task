class TaskController:
    def __init__(self):
        self._tasks = []
        self._current_task = None


    def add_task(self, task):
        self._tasks.append(task)


    def remove_task(self, tid):
        for task in self._tasks:
            if task.get_task_id() == tid:
                self._tasks.remove(task)
                if self._current_task is task:
                    self._current_task = None
                return True

        return False

    def get_task(self, tid):
        return next((task for task in self._tasks if task.get_task_id() == tid), None)

    def set_current_task(self, tid):
        task = self.get_task(tid)
        if task is None:
            raise ValueError(f"Unknown task ID: {tid}")
        self._current_task = task

    def get_current_task(self):
        return self._current_task
