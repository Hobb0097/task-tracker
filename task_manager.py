# Task Manager script - This program stores tasks using a list of dictionaires and allows users to add, view, complete, and delete tasks.
# Thomas Hobbs

# Global list - stores all task dictionaries.
tasks = []

def add_task(name, priority, estimated_time):
    """
    Creates a new task dictionary and adds it to the tasks list.
    """
    task = {
        "name": name,
        "priority": priority.lower(),
        "is_complete": False,
        "estimated_time": estimated_time
    }
    
    tasks.append(task)
    print(f"\nTask added: {name}")
    
def view_tasks():
    """
    Displays all tasks in the task list.
    """
    if len(tasks) == 0:
        print("\nNo tasks found.")
        return
        
    print()
    
    for index, task in enumerate(tasks, start=1):
        status = "Complete" if task["is_complete"] else "Pending"
        
        print(
            f"{index}. {task['name']} | "
            f"Priority: {task['priority']} | "
            f"Status: {status} | "
            f"Est. Time: {task['estimated_time']} mins"
        )
        
def complete_task(index):
    """
    Marks a task as complete using its list index.
    """
    if 0 <= index < len(tasks):
        tasks[index]["is_complete"] = True
        print(f"\nTask marked complete: {tasks[index]['name']}")
    else:
        print("\nError: Invalid task number.")
        
def delete_task(index):
    """
    Deletes a task from the list using pop().
    """
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"\nTask deleted: {removed_task['name']}")
    else:
        print("\nError: Invalid task number.")
        
def run_manager():
    """
    Runs the main Task manager menu until the user quits.
    """
    print("Welcome to the Task Manager!")
    
    while True:
        print("\nOptions: add | view | complete | delete | quit")
        
        option = input("Choose an option: ").lower()
        
        if option == "add":
            name = input("Task name: ")
            
            priority = input(
                "Priority (high, medium, low): "
            ).lower()
            
            while priority not in ["high", "medium", "low"]:
                print("Invalid priority.")
                priority = input(
                    "Priority (high, medium, low): "
                ).lower()
            
            while True:
                try:
                    estimated_time = int(
                        input("Estimated time in minutes: ")
                    )
                    
                    if estimated_time > 0:
                        break
                    
                    print("Please enter a positive number.")
                    
                except ValueError:
                    print("Please enter a whole number.")
                    
            add_task(name, priority, estimated_time)
            
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

        elif option == "quit":
            print("\nGoodbye!")
            break
                
        else:
            print("\nUnrecognized option. Please try again.")
                
                
run_manager()
