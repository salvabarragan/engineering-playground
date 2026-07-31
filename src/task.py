import datetime as dt


class Task:
    def __init__(self, name: str, date: str, category: str):
        if name != "":  # Name cannot be empty
            self.name = name
        else:
            raise ValueError("'Name' cannot be empty")

        try:
            self.date = dt.datetime.strptime(date, "%d/%m/%Y")
        except ValueError:
            raise

        self.category = category  # Tasks do not necessary need a category, is optional
        self.is_done = False

    def complete_task(self):
        self.is_done = True

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.date.strftime('%d/%m/%Y')} ({
            'Done' if self.is_done else 'Undone'
        })"
