import os, subprocess
from .task import Task
from .task_manager import TaskManager


def clear_screen():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def create_task(task_manager):
    while True:
        clear_screen()
        task_name = input("Task name: ")
        task_date = input("Task date: ")
        task_category = input("Task category (optional): ")
        try:
            task_manager.add_task(Task(task_name, task_date, task_category))
        except ValueError as e:
            clear_screen()
            print(f"Error: {e}")
            input("Press Enter to continue...")
        else:
            break


def view_tasks(task_manager):
    while True:  # TODO: In case it is empty, show that there are no tasks.
        clear_screen()
        order = input(
            "If you want to view them in an special order (date or name), type it: "
        )
        if not order.strip():
            order = None
        try:
            tasks = task_manager.get_tasks(order)
        except ValueError as e:
            print(f"Error: {e}")
            input("Press Enter to continue...")
        else:
            break
    clear_screen()
    for task in tasks:
        print(task)
    input("Press any key to exit...")


def main():
    task_manager = TaskManager()

    while True:
        clear_screen()
        print(
            "----------------\nTask Manager\n----------------\nMenu:\n1. Create task.\n2. View tasks.\n3. Remove task.\n4. Modify task.\n5. Exit."
        )
        option = input("Choose an option (1-5): ")
        match option:
            case "1":
                create_task(task_manager)
            case "2":
                view_tasks(task_manager)
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
            case _:
                print("Invalid option.")
                input("Press Enter to continue...")


if __name__ == "__main__":
    main()
