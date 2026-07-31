# Task Tracker script - This program uses functions to to collect task information and display a summary to the user.
# Thomas Hobbs

# Global Variables - always define global variables outside all functions.
APP_NAME = "Task Tracker"
APP_VERSION = "1.0"

def greet_user():
    """Print a welcome message when the Task Tracker starts."""
    print(f"Welcome to {APP_NAME}!")
    print(f"Version: {APP_VERSION}")
    
    

def get_task_input():
    """Collect a task name from the user and return it."""
    # task is defined as a local variable as it is defined inside a function
    task = input("Enter a task name (or type 'quit' to stop): ")
    return task
    
def get_priority_input():
    """ Collect a task priority from the user and return it."""
    # priority is defined as a local variable as it is defined inside a function
    priority = input("Enter task priority (high, medium, or low): ")
    
    # If no priority is entered, user 'Low' as default.
    if priority == "":
        return "low"
    
    return priority
    
def check_priority(priority ="low"):
    # 'Low' is set as the default priority if the user enters no priority.
    """
    Check the task priority and return an appropriate message.
    
    Args:
        priority: The priority level entered by the user.
        
    Returns:
        A message describing the selected priority.
    """
    
    if priority.lower() == "high":
        message = "Urgent: handle this task first."
    elif priority.lower() == "medium":
        message = "Schedule this task soon."
    # 'Low' is set as default priority    
    elif priority.lower() == "low":
        message = "This task can be handled when time allows."
    else:
        message = "Priority not recognized. Please enter high, medium, or low."
        
    # message is defined as a local variable as it is defined inside a function
    return message

def run_tracker():
    """Run the Task Tracker program until the user chooses to quit."""
    greet_user()
    
    while True:
        task = get_task_input()
        
        if task.lower() == "quit":
            print("Goodbye!")
            break
            
        priority = get_priority_input()
        message = check_priority(priority)
        
        print(f"Task: {task}")
        print(message)
        
run_tracker()
