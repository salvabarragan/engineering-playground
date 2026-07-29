from task import Task


class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)
