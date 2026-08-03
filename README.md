# Task Tracker

The Task Tracker is a simple Python application that allows users to enter task information such as the task name,
priority, estimated completion time, and urgency. This project will be expanded upon over this two week period to 
provide additional task management functionality.


## Project Structure

- task_input.py: Collects basic task information from the user using variables and input/output.
- task_priority.py: Adds priority logic using conditionals and a while loop.
- task_tracker.py: Refactored version using functions, scope, and docstrings.
- task_manager.py: Main Task Manager application that stores tasks using a list of dictionaries and allows users to add, view, complete, and delete tasks.
- data_model.md: Documents the task dictionary structure, maps requirements to the code, and lists assumptions about the data model.

## Week 2 Progress
To resolve the problem of tasks disappearing every time the program closed, a file persistence was added.
By saving the task list to a JSON file, users can continue working with the same tasks each time they run the application.
Witout catching a FileNotFoundError, the program would crash the first time it tried to load tasks before
the saved file existed. Error handling also connects to the QA mindset because it helps make the program reliable by
preventing unexpected user input or missing files from causing the application to fail.

## Creation Details

Author: Thomas Hobbs

Created: 29/07/2026