from .task import Task


class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task: Task):
        try:
            self.tasks.remove(task)
        except:
            raise ValueError("The task is not in the list")
