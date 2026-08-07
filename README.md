# Task Manager

### Project Description

The Task Manager is a command-line Python application that allows users to create, manage, save, and load tasks.
The project demonstrates object oriented programming principles including classes, inheritance, encepsulation,
polymorphism, file persistence using JSON, exception handling, and unit testing. Three task types are supported:
standard tasks, urgent tasks with deadlines, and recurring tasks with repeat frequencies.


## How to Run

1. Clone the repository:
	`git clone <repository-url>`

2. Open the project folder.

3. Run the program:
	`py task_manager.py`
	
	or
	
	`python task_manager.py

4. Follow the on-screen menu to manage your tasks.

## Features

- Create standard tasks.
- Create urgent tasks with deadlines.
- Create recurring tasks with frequencies.
- View all saved tasks.
- Mark tasks as complete.
- Delete tasks.
- Save tasks to a JSON file.
- Automatically load saved tasks when the program starts.
- Object-oriented design using inheritance and polymorphism.
- Unit testing using Python's unittest module.
- Input validation and exception handling

## Project Structure

- **task.py** — Contains the `Task`, `UrgentTask`, and `RecurringTask` classes along with the `task_from_dict()` helper function.
- **task_manager.py** — Main application that manages user interaction and task operations.
- **test_task.py** — Unit tests for all task classes.
- **test_results.txt** — Output showing all unit tests passed.
- **tasks.json** — Stores saved task data.
- **data_model.md** — Documents the application's data model.
- **code_review.md** — Structured self-review and release readiness checklist.
- **bug_report.md** — Documents known bugs.
- **README.md** — Project documentation.

## Known Bugs
- Entering an empty task name is currently allowed and should be validated.
- The application does not allow users to edit an existing task after it has been created.

## Future Improvements
- Add the abiltiy to edit existing tasks.
- Add sorting and filtering by priority, deadline, or completion status.
- Add due date reminders.
- Develop a graphical user interface (GUI) using Tkinter or PyQt.