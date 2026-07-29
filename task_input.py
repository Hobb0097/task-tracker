# Task Tracker
# Created by Thomas Hobbs
# Created 29/07/2026
# Updated 29/07/2026
# This script is designed to collect task information and display a summary to the user.

print("Welcome to Task Tracker")
print("Please enter your task details below.")
print()

# Collect task information
task_name = input("Enter task name: ")
priority = input("Enter priority level (high, medium, low): ")
estimated_time = int(input("Estimated time to complete (in minutes): "))
urgent = input("Is tis task urgent? (yes/no): ")

# Placeholder: completion percentage will be calculated later
completion_rate = 0.0

# Placeholder: task completion status, starts as False
is_complete = False

# Display task summary
print()
print("Task Summary")
print("Task:", task_name)
print("Priority:", priority)
print("Estimated Time:", estimated_time, "minutes")
print("Urgent:", urgent)
