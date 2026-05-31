# Task Tracker CLI

A simple command-line task tracker built in Python.

This project is my implementation of the Task Tracker project from roadmap.sh. It allows users to create, update, delete, and manage tasks directly from the terminal while storing all task data in a JSON file.
## Features

* Add tasks
* Update existing tasks
* Delete tasks
* Mark tasks as:

  * To-Do
  * In Progress
  * Done
* List all tasks
* List tasks filtered by status
* Automatic task ID generation
* Persistent storage using JSON
* Creation and last-updated timestamps
* Human-readable status display
* Automatic creation and validation of `data.json`


---

## Project Structure

```text
Task-Tracker/
│
├── Task-cli.py
├── Tasks.py
├── data.json
└── README.md
```

---

## Requirements

* Python 3.x

No third-party packages are required.

---

## Usage

### Add a Task

```bash
python3 Task-cli.py add "Buy groceries"
```

Output:

```text
Task created successfully, ID=1
```

---

### Update a Task

```bash
python3 Task-cli.py update 1 "Buy groceries and cook dinner"
```

---

### Delete a Task

```bash
python3 Task-cli.py delete 1
```

---

### Mark a Task as In Progress

```bash
python3 Task-cli.py mark-in-progress 1
```

---

### Mark a Task as Done

```bash
python3 Task-cli.py mark-done 1
```

---

### Mark a Task as Todo

```bash
python3 Task-cli.py mark-todo 1
```

---

### List All Tasks

```bash
python3 Task-cli.py list
```

---

### List Done Tasks

```bash
python3 Task-cli.py list done
```

---

### List Todo Tasks

```bash
python3 Task-cli.py list todo
```

---

### List In Progress Tasks

```bash
python3 Task-cli.py list in-progress
```

---
## Example Output

```text
========================Task=========================
Title:Buy groceries
Progress:Done
Created At:Sat May 30 23:50:29 2026
Updated At:Sat May 30 23:51:32 2026
=======================End Of Task=========================
```


---

## Data Storage

All tasks are stored in `data.json`.

Example:

```json
{
    "1": [
        "Buy groceries",
        "d",
        1780185029.12,
        1780185092.47
    ]
}
```
### Status Codes

Internally, tasks use the following status codes:

| Code | Status      |
| ---- | ----------- |
| t    | To-Do       |
| ip   | In Progress |
| d    | Done        |

When tasks are displayed, the codes are automatically converted into human-readable status names.


---

## Task Properties

Each task stores:

* ID
* Title
* Status
* Creation timestamp
* Last updated timestamp

---

## Concepts Practiced

This project helped me learn:

* Python classes
* Static methods
* File handling
* JSON serialization/deserialization
* Command-line argument parsing (`sys.argv`)
* CRUD operations
* Data persistence
* Error handling
* Basic CLI application design

---

## Roadmap.sh Project

Project URL:

https://roadmap.sh/projects/task-tracker

---

## Future Improvements

* Task priorities
* Due dates
* Search functionality
* Colored terminal output
* Better status display
* Packaging as an installable `task-cli` command

---

## License

This project is open source and available under the MIT License.
