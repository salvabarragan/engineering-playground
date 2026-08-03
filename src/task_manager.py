from .task import Task


class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task: Task):
        try:
            self.tasks.remove(task)
        except ValueError:
            raise ValueError("The task is not in the list")

    def get_tasks(self, order: str | None = None) -> list[Task]:
        """
        Order can be: date, name. If it is empty, tasks are given in the order of creation.
        """
        if order is None:
            given_tasks = self.tasks
        elif order == "date":
            given_tasks = sorted(self.tasks, key=lambda x: x.date)
        elif order == "name":
            given_tasks = sorted(self.tasks, key=lambda x: x.name)
        else:
            raise ValueError(f"'{order}' is not an option.")
        return given_tasks

    def __str__(self):
        return "\n".join(f"{task}" for task in self.get_tasks())
