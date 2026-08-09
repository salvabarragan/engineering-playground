# Engineering Playground

## Description

Engineering Playground is a simple task manager whose goal is to learn how a real software project works, how to write documentation, how to use Git and GitHub, and how to build a strong portfolio.

## Features

This task manager has the following features:
- Create tasks (with name, date, and category).
- View tasks (in a specific order: date or name).
- Modify tasks.
- Remove tasks.
- Date validation (to prevent invalid dates).

## Installation
- Clone the repository.

```bash
git clone https://github.com/salvabarragan/engineering-playground.git
```

- Make sure Python 3.10 or later is installed.

```bash
py --version
```

- Install the requirements.
```bash
py -m pip install -r requirements.txt
```

- Run the application.

```bash
py -m src.main
```

## Usage

The menu shows 5 options:

```text
----------------
Task Manager
----------------
Menu:
1. Create task.
2. View tasks.
3. Remove task.
4. Modify task.
5. Exit.
Choose an option (1-5):
```

The options work as follows:

### Create task

If the first option is selected (1 + Enter), it will show:

```text
Task name:
Task date:
Task category (optional):
```

For the task name, any name is valid as long as it is not empty or made up only of whitespace. The date must be entered in the following format: `DD/MM/YYYY`. For the category, any name is valid. If it is omitted or contains only whitespace, its value will be `None`.

### View tasks

If the second option is selected (2 + Enter), it will show:

```text
If you want to view them in a special order (date or name), type it:
```

There are 3 possible options: `date`, `name`, or nothing. If `date` is chosen, tasks will be sorted by date. If `name` is chosen, tasks will be sorted by name. If nothing is given, tasks will be displayed in the order in which they were created.

If there are no tasks, it will show:

```text
There are no tasks.

Press any key to exit...
```

### Remove task

If the third option is selected (3 + Enter), it will show:

```text
Example 1 (Example) - 01/01/0001 (Undone)
Example 2 (Example) - 02/02/0002 (Undone)
Example 3 (Example) - 03/03/0003 (Undone)

Select a task by its task number:
```

There are 3 tasks, so the first one has the number 1, and so on. Once the task number is selected, the application will return to the menu and the task will be removed.

If the number given is not valid, it will show:

```text
...
Error: Task number is out of range.
Press Enter to continue...
```

If there are no tasks, it will show:

```text
There are no tasks.
Press Enter to continue...
```

### Modify task

If the fourth option is selected (4 + Enter), it will show:

```text
Example 1 (Example) - 01/01/0001 (Undone)
Example 2 (Example) - 02/02/0002 (Undone)
Example 3 (Example) - 03/03/0003 (Undone)

Select a task by its task number:
```

Task selection works in the same way as [Remove task](#remove-task).

After selecting a task, it will show:

```text
Example 1 (Example) - 01/01/0001 (Undone)

New name:
New date:
New category:
Is it done? (Y-N):
```

The name, date, and category rules and validation work in the same way as [Create task](#create-task). If a field is left empty, its current value will not be modified.

The `Is it done? (Y-N)` option modifies the task's completion status. If `Y` is given, the task will be shown as `Done`; if `N` is given, it will be shown as `Undone`.

### Exit

If the fifth option is selected (5 + Enter), the program will stop immediately.

## Tests

Make sure that all the [Installation](#installation) steps have been followed.

Run the tests with:

```bash
pytest -v
```

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
