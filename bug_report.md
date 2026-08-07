# Bug Report

## BUG-01

**Description:** The application allows users to create a task with an empty task name.

**Steps to Reproduce:**
1. Run `task_manager.py`
2. Choose add
3. Press Enter without entering a task name.
4. Complete the remaining prompts.

**Expected Behavior:** The program should reject the empty task name and request valid input.

**Actual Behavior:** A task is created with a blank name.

## BUG-02

**Description:** The application does not allow users to edit an existing task after it has been created.

**Steps to Reproduce:**
1. Run `task_manager.py`
2. Create a task
3. Attempt to modify its priority or estimated time.

**Expected Behavior:** The application should provide an edit option to update task information.

**Actual Behavior:** The only available options are to complete or delete the task.
					 Users mush recreate the task to make changes.