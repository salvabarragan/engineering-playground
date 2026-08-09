import datetime as dt


class Task:
    def __init__(self, name: str, date: str, category: str):
        if name.strip():
            self.name = name.strip()
        else:
            raise ValueError("'Name' cannot be empty")

        self.date = self._check_date(date)

        if category.strip():
            self.category = category.strip()
        else:
            self.category = None

        self.is_done = False

    def _check_date(self, date: str) -> dt.datetime:
        try:
            return dt.datetime.strptime(date, "%d/%m/%Y")
        except ValueError:
            raise

    def complete_task(self):
        self.is_done = True

    def modify_task(
        self, new_name: str, new_date: str, new_category: str, new_is_done: str
    ):
        """
        Updates the task. Empty string arguments leave the corresponding fields unchanged.
        """
        if new_name:
            self.name = new_name

        if new_date:
            self.date = self._check_date(new_date)

        if new_category:
            self.category = new_category

        if new_is_done:
            if new_is_done == "y":
                self.is_done = True
            elif new_is_done == "n":
                self.is_done = False
            else:
                raise ValueError("It must be 'Y' or 'N'.")

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.date.strftime('%d/%m/%Y')} ({
            'Done' if self.is_done else 'Undone'
        })"
