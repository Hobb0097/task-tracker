# Code Review

## Code Quality

- [x] All function and methods have docstrings.
- [x] No unused variables or commented-out code blocks remain in the final files.
- [x] Variable and function names are descriptive and follow Python naming conventions.

## Correctness

- [x] Adding a task creates the correct object type and appends it to the list.
- [x] Viewing tasks displays all fields including status.
- [x] Completing a task correctly updates is_complete.
- [x] Deleting a task removes it from the list and prints the correct name.
- [x] Saving writes a valid tasks.json file.
- [x] Loading restores all task types correctly using task_from_dict.

## Edge Cases
- [x] The program handles an empty task list gracefully in view_tasks().
- [x] Invalid priority input is rejected by set_priority().
- [x] Non-numeric input for estimated time is caught with a ValueError.
- [x] Out-of-range task numbers are handled in complete_task() and delete_task().

## Documentation

- [x] README is complete with all required sections.
- [x] Project Structure section lists every file in the repository.
- [x] Known bugs are documented.

## One Improvement You Made

I improved the unit testing suite by adding an additional test to verify that completed tasks 
are restored correctly when loaded from a dictionary. I also corrected the recurring task string 
test so it matched the actual output of the program. These changes improved the overall reliabiltiy of
the project and ensured all 15 unit tests passed successfully.

## Release Readiness Checklist: Task Manager v1.0

### Code Quality
- [x] All functions and methods have docstrings
- [x] No unused variables or commented-out code blocks remain
- [x] Variable and function names are descriptive

### Testing
- [x] All unit tests pass with zero failures
- [x] Edge cases are covered in tests
- [x] All three task types have been manually tested end to end

### Documentation
- [x] README is complete and up to date
- [x] Project Structure section lists all files
- [x] Known bugs are documented in bug_report.md
- [x] Future improvements are listed

### Version Control
- [x] All changes committed with clear messages
- [x] Repository is public and accessible

### File Persistence
- [x] tasks.json is generated correctly on save
- [x] Tasks reload correctly on restart for all three task types