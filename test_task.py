# Test Task script - The Unit Test Cases for testing the task class and task manager
# Thomas Hobbs

import unittest
from task import Task, UrgentTask, RecurringTask


class TestTask(unittest.TestCase):
    """
    Tests for the task class.
    """
    
    def setUp(self):
        """
        Create a fresh task before each test.
        """
        self.task = Task("Buy groceries", "high", 30)
        
    def test_task_creation(self):
        """
        Test task attributes are set correctly.
        """
        self.assertEqual(self.task.name, "Buy groceries")
        self.assertEqual(self.task.get_priority(), "high")
        self.assertEqual(self.task.estimated_time, 30)
        self.assertEqual(self.task.get_is_complete(), False)
    
    def test_mark_complete(self):
        """
        Test marking a task complete.
        """
        self.task.mark_complete()
        self.assertTrue(self.task.get_is_complete())
            
    def test_set_priority_valid(self):
        """
        Test changing to a valid priority.
        """
        self.task.set_priority("low")
        self.assertEqual(self.task.get_priority(), "low")
        
    def test_set_priority_invalid(self):
        """
        Test invalid priority does not change.
        """
        self.task.set_priority("urgent")
        self.assertEqual(self.task.get_priority(), "high")
        
    def test_to_dict(self):
        """
        Test conversion to dictionary
        """
        task_dict = self.task.to_dict()
        
        self.assertEqual(task_dict["name"], "Buy groceries")
        self.assertEqual(task_dict["priority"], "high")
        self.assertEqual(task_dict["estimated_time"], 30)
        self.assertFalse(task_dict["is_complete"])
        
    def test_from_dict(self):
        """
        Test creating task from dictionary.
        """
        data = {
            "type": "Task",
            "name": "Buy groceries",
            "priority": "high",
            "estimated_time": 30,
            "is_complete": False
        }
        
        task = Task.from_dict(data)
        
        self.assertEqual(task.name, "Buy groceries")
        self.assertEqual(task.get_priority(), "high")
        
        
    def test_str_output(self):
        """
        Test string representation.
        """
        self.assertIn("Buy groceries", str(self.task))
        self.assertIn("Pending", str(self.task))
        
    def test_from_dict_completed(self):
        """
        Test completed task is restored correctly.
        """
        data = {
            "type": "Task",
            "name": "Buy groceries",
            "priority": "high",
            "estimated_time": 30,
            "is_complete": True
        }

        task = Task.from_dict(data)

        self.assertTrue(task.get_is_complete())
    
class TestUrgentTask(unittest.TestCase):
    """
    Test for UrgentTask.
    """
    
    def setUp(self):
        """
        Create urgent task.
        """
        self.task = UrgentTask("Fix server outage", 5, "2024-12-01")    
    
    def test_urgent_priority_is_always_high(self):
        """
        Test priority is always high.
        """
        self.assertEqual(self.task.get_priority(), "high")
    
    def test_urgent_str_contains_label(self):
        """
        Test urgent label exists.
        """
        self.assertIn("[URGENT]", str(self.task))
        
    def test_urgent_str_contains_deadline(self):
        """
        Test deadline appears.
        """
        self.assertIn("2024-12-01", str(self.task))    
        
    def test_urgent_to_dict_includes_type(self):
        """
        Test dictionary contains type.
        """
        task_dict = self.task.to_dict()
        
        self.assertEqual(task_dict["type"], "UrgentTask")
        self.assertIn("deadline", task_dict)
        
class TestRecurringTask(unittest.TestCase):
    """
    Tests for RecurringTask.
    """
    
    def setUp(self):
        """
        Create recurring task.
        """
        self.task = RecurringTask("Team standup", "medium", 15, "daily")    
    
    def test_recurring_str_contains_label(self):
        """
        Test recurring label exists.
        """
        self.assertIn("[RECURRING", str(self.task)) 

    def test_recurring_to_dict_includes_type(self):
        """
        Test dictionary contains type.
        """
        task_dict = self.task.to_dict()
        
        self.assertEqual(task_dict["type"], "RecurringTask")
        self.assertIn("frequency", task_dict)        
        
    def test_reset(self):
        """
        Test reset marks task incomplete.
        """
        self.task.mark_complete()
        self.task.reset()
        
        self.assertFalse(self.task.get_is_complete())

        
if __name__ == "__main__":
    unittest.main()