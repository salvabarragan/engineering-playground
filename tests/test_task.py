import pytest
from datetime import datetime
from src.task import Task


@pytest.fixture
def task():
    return Task(name="Study maths", date="01/01/2027", category="School")


class TestTask:
    def test_task_creation(self, task):
        assert task.name == "Study maths"
        assert task.date == datetime.strptime("01/01/2027", "%d/%m/%Y")
        assert task.category == "School"
        assert task.is_done is False

    def test_invalid_date_task_creation(self):
        with pytest.raises(ValueError):
            Task(name="Study maths", date="32/01/2027", category="School")

    def test_invalid_name_task_creation(self):
        with pytest.raises(ValueError):
            Task(name="", date="01/01/2027", category="School")

    def test_complete_task(self, task):
        task.complete_task()
        assert task.is_done is True

    def test_show_task(self, task):
        assert str(task) == "Study maths (School) - 01/01/2027 (Undone)"
