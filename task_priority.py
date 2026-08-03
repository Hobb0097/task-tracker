# Task Priority script - This program uses priority logic and loops to keep the program running.
# Thomas Hobbs

# Display welcome message.
print("Welcome to Task Tracker Priority Checker!")
print()

# Program keeps running until iser types quit when asked for a task name.
while True:
    task_name = input("Enter a task name (or type 'quit' to stop): ")
    
    if task_name.lower() == "quit":
        print("Session ended. Goodbye!")
        break
        
    # Check that the task name contains at least one character.
    if len(task_name) > 0:
        priority = input("Enter priority (high, medium, low): ")
        
        # Display a message depending on priority level
        if priority.lower() == "high":
            print("Urgent: handle this task first.")
        elif priority.lower() == "medium":
            print("Schedule this task soon.")
        elif priority.lower() == "low":
            print("This task can be handled when time allows.")
        else:
            print("Priority not recognized. Please enter high, medium, or low.")
        
        print()
        
    else:
        print("Task name cannot be empty.")
        print()
