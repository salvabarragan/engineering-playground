import pytest
from src.task_manager import TaskManager
from src.task import Task


@pytest.fixture
def task_manager():
    return TaskManager()


@pytest.fixture
def task():
    return Task(name="Study maths", date="01/01/2027", category="School")


class TestTaskManager:
    def test_task_manager_creation(self, task_manager):
        assert task_manager.tasks == []

    def test_add_task(self, task_manager, task):
        task_manager.add_task(task)
        assert task_manager.tasks == [task]

    def test_remove_task(self, task_manager, task):
        task_manager.add_task(task)
        assert task_manager.tasks == [task]
        task_manager.remove_task(task)
        assert task_manager.tasks == []

    def test_error_remove_task(self, task_manager, task):
        with pytest.raises(ValueError):
            task_manager.remove_task(task)
