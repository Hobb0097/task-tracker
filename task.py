# Task script - The task class for the Task Manager application.
# Thomas Hobbs

class Task:
    """
    Represents a single task.
    """
    def __init__(self, name, priority, estimated_time):
        """
        Initialize a task object.
        """
        self.name = name
        self.estimated_time = estimated_time
        self.__priority = priority
        self.__is_complete = False
        
    def get_priority(self):
        """
        Return the task priority
        """
        return self.__priority
    
    def set_priority(self, new_priority):
        """
        Update the task priority if it is valid.
        """
        valid_priorities = ["high", "medium", "low"]
        
        if new_priority.lower() in valid_priorities:
            self.__priority = new_priority.lower()
        else:
            print("Invalid priority. Choose high, medium, or low.")
            
    def get_is_complete(self):
        """
        Return the completion status.
        """
        return self.__is_complete
    
    def mark_complete(self):
        """
        Mark the task as complete.
        """
        self.__is_complete = True
        
    def to_dict(self):
        """
        Convert the Task object into a dictionary for JSON.
        """
        return {
            "name": self.name,
            "priority": self.__priority,
            "estimated_time": self.estimated_time,
            "is_complete": self.__is_complete
        }
        
    @classmethod
    def from_dict(cls, data):
        """
        Create a Task object from a dictionary.
        """
        task = cls(
            data["name"],
            data["priority"],
            data["estimated_time"]
        )
        
        if data.get("is_complete"):
            task.mark_complete()
            
        return task
        
    def __str__(self):
        """
        Return a readable string representation of the task.
        """
        status = "Done" if self.__is_complete else "Pending"
        
        return (
            f"{self.name} | "
            f"Priority: {self.__priority} | "
            f"Status: {status} | "
            f"Est. Time: {self.estimated_time} mins"
        )
