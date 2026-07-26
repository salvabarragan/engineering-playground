import datetime as dt


class Task:
    def __init__(self, name: str, date: str, category: str):
        self.name = name
        try:
            self.date = dt.datetime.strptime(date, "%d/%m/%Y")
        except ValueError:
            raise

        self.category = category
        self.is_done = False

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.date.strftime('%d/%m/%Y')} ({
            'Done' if self.is_done else 'Undone'
        })"
        