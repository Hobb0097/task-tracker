# Task Manager script - This program stores tasks using Task objects and allows users to add, view, complete, and delete tasks.
# Thomas Hobbs

# Import the Json module and Task Class
import json
from task import Task, UrgentTask, RecurringTask, task_from_dict

# File used to stores the saved tasks.
TASKS_FILE = "tasks.json"

# Global list - stores all task objects.
tasks = []

def add_task(name, priority, estimated_time):
    """
    Creates a new Task object and adds it to the tasks list.
    """
    task = Task(name, priority, estimated_time)
    tasks.append(task)
    print(f"\nTask added: {name}")
    
def add_urgent_task():
    """
    Creates and adds an urgent task.
    """
    name = input("Task name: ")
    
    try:
        estimated_time = int(
            input("Estimated time in minutes: ")
        )
        
    except ValueError:
        print("Please enter a whole nu,ber for estimated time.")
        return
        
    deadline = input("Deadline (e.g., 2024-12-01): ")
    
    task = UrgentTask(
    name,
    estimated_time,
    deadline
    )

    tasks.append(task)
    
    print(f"\nUrgent task added: {name}")
    
def add_recurring_task():
    """
    Creates and adds a recurring task.
    """
    name = input("Task name: ")
    
    priority = input(
        "Priority (high, medium, low): "
    ).lower()
    
    if priority not in ["high", "medium", "low"]:
        print("Please enter high, medium, or low.")
        return
        
    try:
        estimated_time = int(
            input("Estimated time in minutes: ")
        )
        
    except ValueError:
        print("Please enter a whole number for estimated time.")
        return
        
    frequency = input(
        "Frequency (e.g. daily, weekly): "
    )
    
    task = RecurringTask(
        name,
        priority,
        estimated_time,
        frequency
    )
    
    tasks.append(task)
    
    print(f"\nRecurring task added: {name}")
    
def view_tasks():
    """
    Displays all tasks in the task list.
    """
    if len(tasks) == 0:
        print("\nNo tasks found.")
        return
        
    print()
    
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}") 
        
def complete_task(index):
    """
    Marks a task as complete using its list index.
    """
    if 0 <= index < len(tasks):
        tasks[index].mark_complete()
        print(f"\nTask marked complete: {tasks[index].name}")
    else:
        print("\nError: Invalid task number.")
        
def delete_task(index):
    """
    Deletes a task from the list using pop().
    """
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"\nTask deleted: {removed_task.name}")
    else:
        print("\nError: Invalid task number.")

def save_tasks():
    """
    Saves the current task list to a JSON file.
    """
    with open(TASKS_FILE, "w") as file:
        json.dump(
            [task.to_dict() for task in tasks],
            file,
            indent =4
        )
    print("Tasks saved.")
    
def load_tasks():
    """
    Loads saved tasks from the JSON file.
    """
    global tasks
    
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [task_from_dict(task) for task in json.load(file)]
            
        print(f"Loaded {len(tasks)} task(s).")
        
    except FileNotFoundError:
        tasks = []
        print("No saved file found. Starting with an empty task list.")
        
    except json.JSONDecodeError:
        tasks = []
        print("Save file is corrupted. Starting with an empty task list.")
        
def run_manager():
    """
    Runs the main Task manager menu until the user quits.

    """
    load_tasks()
    print("Welcome to the Task Manager!")
    
    while True:
        print("\nOptions: add | add-urgent | add-recurring | view | complete | delete | save | quit")
        
        option = input("Choose an option: ").lower()
        print()
        
        if option == "add":
            name = input("Task name: ")
            
            priority = input(
                "Priority (high, medium, low): "
            ).lower()
            
            if priority not in ["high", "medium", "low"]:
                print("Please enter high, medium, or low.")
                continue

            try:
                estimated_time = int(
                    input("Estimated time in minutes: ")
                )
                
            except ValueError:
                print("Please enter a whole number for estimated time.")
                continue 
                
            if estimated_time < 0:
                print("Please enter a positive number.")
                continue
                    
            add_task(name, priority, estimated_time)
        
        elif option == "add-urgent":
            add_urgent_task()

        elif option == "add-recurring":
            add_recurring_task() 
            
        elif option == "view":
            view_tasks()
                
        elif option == "complete":
            view_tasks()
                
            if len(tasks) > 0:
                try:
                    number = int(
                        input("Enter task number to mark complete: ")
                    )
                    complete_task(number - 1)
                        
                except ValueError:
                    print("Please enter a valid number.")
                    continue
                        
        elif option == "delete":
            view_tasks()

            if len(tasks) > 0:
                try:
                    number = int(
                        input("Enter task number to delete: ")
                    )
                    delete_task(number - 1)

                except ValueError:
                    print("Please enter a valid number.")
                    continue

        elif option == "save":
            save_tasks()
            
        elif option == "quit":
            save_tasks()
            print("\nGoodbye!")
            break
                
        else:
            print("\nUnrecognized option. Please try again.")
                
                
run_manager()
