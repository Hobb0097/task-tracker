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
            "type": "Task",
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
    
class UrgentTask(Task):
    """
    Represents an urgent task with a deadline.
    """
    
    def __init__(self, name, estimated_time, deadline):
        """
        Initialize an urgent task with a fixed high priority.
        """
        super().__init__(name, "high", estimated_time)
        self.deadline = deadline
    
    def __str__(self):
        """
        Return a readable string representation of the urgent task.
        """
        status = "Done" if self.get_is_complete() else "Pending"
        
        return (
            f"[URGENT] {self.name} | "
            f"Status: {status} | "
            f"Est. Time: {self.estimated_time} mins | "
            f"Deadline: {self.deadline}"
        )
        
    def to_dict(self):
        """
        Convert the urgent task into a dictionary for JSON.
        """
        task_dict = super().to_dict()
        task_dict["type"] = "UrgentTask"
        task_dict["deadline"] = self.deadline
        
        return task_dict
        
class RecurringTask(Task):
    """
    Represents a recurring task that can be reset after completion.
    """
    
    def __init__(self, name, priority, estimated_time, frequency):
        """
        Initialize a recurring task.
        """
        super().__init__(name, priority, estimated_time)
        self.frequency = frequency
        
    def __str__(self):
        """
        Return a readable string representation of the recurring task.
        """
        status = "Done" if self.get_is_complete() else "Pending"
        
        return (
            f"[RECURRING: {self.frequency}] {self.name} | "
            f"Priority: {self.get_priority()} | "
            f"Status: {status} | "
            f"Est. Time: {self.estimated_time} mins"
        )
        
    def reset(self):
        """
        Reset the recurring task so it can be completed again.
        """
        self._Task__is_complete = False
        print(f"Task '{self.name}' has been reset for {self.frequency} recurrence.")
        
    def to_dict(self):
        """
        Convert the recurring task into a dictionary for JSON.
        """
        task_dict = super().to_dict()
        task_dict["type"] = "RecurringTask"
        task_dict["frequency"] = self.frequency
        
        return task_dict

def task_from_dict(data):
    """
    Create the correct task object based on the task type.
    """
    task_type = data.get("type")

    if task_type == "UrgentTask":
        task = UrgentTask(
            data["name"],
            data["estimated_time"],
            data["deadline"]
        )

        if data.get("is_complete"):
            task.mark_complete()

        return task

    elif task_type == "RecurringTask":
        task = RecurringTask(
            data["name"],
            data["priority"],
            data["estimated_time"],
            data["frequency"]
        )

        if data.get("is_complete"):
            task.mark_complete()

        return task

    else:
        return Task.from_dict(data)