Project source : https://roadmap.sh/projects/task-tracker

# Todo List Manager

This project is a simple CLI-based todo list manager that allows users to manage tasks stored in a JSON file. It supports various operations like adding tasks, updating tasks, deleting tasks, and tracking their progress. The tasks are stored in a JSON file named `todo.json`, and the program utilizes Python's built-in modules such as `json`, `os`, and `argparse`.

## Features

- **Add a task**: Allows the user to add a new task to the list.
- **List all tasks**: Displays all tasks with their current status.
- **Update a task**: Modify the description of an existing task.
- **Delete a task**: Removes a task from the list by its ID.
- **Update task progress**: Change the progress of a task (Todo, In Progress, Done).
- **List tasks by status**: View tasks filtered by their progress status.

## Requirements

- Python 3.x
- No external dependencies are required for this project.

## Usage

### Commands

1. **Add a task**
python todo.py add "Your task description"

2. **List all tasks**
python todo.py list

3. **Update a task**
python todo.py update <task_id> "New task description"

4. **Delete a task**
python todo.py delete <task_id>

5. **Update a task progress**
python todo.py updateprogress <task_id> <progress_status>

6. **List tasks by status**
python todo.py liststatus

### File Format
The tasks are stored in a JSON file named todo.json with the following structure:

```
{
    "tasks": [
        {
            "id": 1,
            "task": "Example task",
            "progression": "Todo"
        },
        ...
    ]
}
```

