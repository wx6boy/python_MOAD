import unittest
import task_manager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = task_manager.TaskManager()

    def test_create_task(self):
        task = self.manager.create_task("Work", "Exercise №1")
        self.assertEqual(self.manager.get_tasks(), [task])

    def test_update_status(self):
        task = self.manager.create_task("Work", "Exercise №1")
        self.manager.update_status(task, "Finished")
        self.assertEqual(self.manager.get_tasks()[0].get_status(), task.get_status())

    def test_remove_tasks(self):
        self.manager.create_task("Work", "Exercise №1")
        self.manager.remove_tasks()
        self.assertEqual(self.manager.get_tasks(), [])

    def test_remove_task_by_id(self):
        first_task = self.manager.create_task("Work", "Exercise №1")
        remove_id = first_task.get_id()
        second_task = self.manager.create_task("Work", "Exercise №2")
        self.manager.remove_task_by_id(remove_id)
        self.assertEqual(self.manager.get_tasks(), [second_task])

    def test_create_complex_task(self):
        first_task = self.manager.create_task("Work", "Exercise №1")
        second_task = self.manager.create_task("Work", "Exercise №2")
        third_task = self.manager.create_task("Work", "January")
        self.manager.create_subtask(first_task, third_task.get_id())
        self.manager.create_subtask(second_task, third_task.get_id())
        self.assertEqual(self.manager.get_complex_tasks()[0].get_id(), third_task.get_id())
        self.assertEqual(len(self.manager.get_subtasks()), 2)

    def test_remove_subtasks(self):
        first_task = self.manager.create_task("Work", "Exercise №1")
        second_task = self.manager.create_task("Work", "Exercise №2")
        third_task = self.manager.create_task("Work", "January")
        self.manager.create_subtask(first_task, third_task.get_id())
        self.manager.create_subtask(second_task, third_task.get_id())
        self.manager.remove_subtasks()
        self.assertEqual(len(self.manager.get_complex_tasks()), 0)
        self.assertEqual(len(self.manager.get_tasks()), 1)


if __name__ == "__main__":
    unittest.main()