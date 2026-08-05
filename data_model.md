# Data Model

## Section 1: Task Dictionary Structure

| Field Name | Data Type | Description | Default Value |
|------------|-----------|-------------|---------------|
| name | str | The name of the task | User input |
| priority | str | Priority level (high, medium, or low) | User input |
| is_complete | bool | Indicates whether the task is complete | False |
| estimated_time | int | Estimated time to complete the task in minutes | User input |

---

## Section 2: Requirements Mapping

| Functional Requirement | Data Field or Function | How It Is Fulfilled |
|------------------------|------------------------|---------------------|
|Add a task | add_task() | Creates a task dictionary and appends it to the task list. |
| View all tasks | view_tasks() | Displays every task with its details. |
| Mark a task complete | complete_task() | Sets the is_complete field to True. |
| Delete a task | delete_task() | Removes the selected task from the list using pop(). |

---

## Section 3: Assumptions

- Tasks are stored only while the program is running and are not saved to a file.
- Estimated time is entered as a whole number representing minutes.
- Priority values are limited to **high**, **medium**, or **low**.
- New tasks always begin with **is_complete = False**.

## Week 2 Day 3 Update: OOP Refactor
The task manager was refactored to use a Task Class instead of storing tasks as dictionaries.
Each task is now represented as an object that contains both its data and the methods with that data.
Encapsulation protects important values like priority and completion status by making them private and
providing getter and setter methods for controlled access. The to_dict() and from_dict() allow Task objects
to be converted into dictionaries when saving to JSON and recreated as Task objects when loading the application.

## Creation Details

Author: Thomas Hobbs

Created: 3/08/2026