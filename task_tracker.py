# Task Tracker script - This program uses functions to to collect task information and display a summary to the user.
# Thomas Hobbs

def greet_user():
    """Print a welcome message when the Task Tracker starts."""
    print("Welcome to the Task Tracker:")
    

def get_task_input():
    """Collect a task name from the user and return it."""
    task = input("Enter a task name (or type 'quit' to stop): ")
    return task
    
def get_priority_input():
    """ Collect a task priority from the user and return it."""
    priority = input("Enter task priority (high, medium, or low): ")
    return priority
    
def check_priority(priority):
    """
    Check the task priority and return an appropriate message.
    
    Args:
        priority: The priority level entered by the user.
        
    Returns:
        A message describing the selected priority.
    """
    
    if priority.lower() == "high":
        return("Urgent: handle this task first.")
    elif priority.lower() == "medium":
        return("Schedule this task soon.")
    elif priority.lower() == "low":
        return("This task can be handled when time allows.")
    else:
        return("Priority not recognized. Please enter high, medium, or low.")

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
