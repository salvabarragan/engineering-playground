import pytest
from src.task_manager import TaskManager
from src.task import Task


@pytest.fixture
def empty_task_manager():
    return TaskManager()


@pytest.fixture
def task():
    return Task(name="Study maths", date="01/01/2027", category="School")


@pytest.fixture
def tasks_list():
    tasks_list = [
        Task(name="Buy milk", date="26/01/2027", category="Food"),
        Task(name="Water the plants", date="05/12/2027", category="Home"),
        Task(name="Order my room", date="30/06/2027", category="Home"),
        Task(name="Study language", date="25/01/2027", category="School"),
        Task(name="Clean bathroom", date="16/02/2027", category="Home"),
    ]

    return tasks_list


@pytest.fixture
def task_manager(empty_task_manager, tasks_list):
    for task in tasks_list:
        empty_task_manager.add_task(task)

    return empty_task_manager


class TestTaskManager:
    def test_task_manager_creation(self, empty_task_manager):
        assert empty_task_manager.tasks == []

    def test_add_task(self, empty_task_manager, task):
        empty_task_manager.add_task(task)
        assert empty_task_manager.tasks == [task]

    def test_remove_task(self, empty_task_manager, task):
        empty_task_manager.add_task(task)
        assert empty_task_manager.tasks == [task]
        empty_task_manager.remove_task(task)
        assert empty_task_manager.tasks == []

    def test_error_remove_task(self, empty_task_manager, task):
        with pytest.raises(ValueError):
            empty_task_manager.remove_task(task)

    def test_get_tasks(self, task_manager, tasks_list):
        assert (
            task_manager.get_tasks() == tasks_list
        )  # It does not recieve order, so the order does not changes.

    def test_get_tasks_date_order(self, task_manager, tasks_list):
        assert task_manager.get_tasks(order="date") == sorted(
            tasks_list, key=lambda x: x.date
        )

    def test_get_tasks_name_order(self, task_manager, tasks_list):
        assert task_manager.get_tasks(order="name") == sorted(
            tasks_list, key=lambda x: x.name
        )

    def test_get_tasks_error(self, task_manager, tasks_list):
        with pytest.raises(ValueError):
            task_manager.get_tasks(order="hello")
