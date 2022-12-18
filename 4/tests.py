import unittest
import task_manager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = task_manager.TaskManager()

    def test_create_task(self):
        task = task_manager.Task(1, "Работа", "Надо работать", "В работе")
        self.manager.create_task(task)
        self.assertEqual(self.manager.get_tasks(), [task])

    def test_update_status(self):
        task = task_manager.Task(1, "Работа", "Надо работать", "В работе")
        self.manager.create_task(task)
        task = task_manager.Task(1, "Работа", "Надо работать", "Готово")
        self.manager.update_status(task)
        self.assertEqual(self.manager.get_tasks()[0].get_status(), task.get_status())

    def test_remove_tasks(self):
        task = task_manager.Task(1, "Работа", "Надо работать", "В работе")
        self.manager.create_task(task)
        self.manager.remove_tasks()
        self.assertEqual(self.manager.get_tasks(), [])

    def test_remove_task_by_id(self):
        task = task_manager.Task(1, "Работа", "Надо работать", "В работе")
        self.manager.create_task(task)
        task = task_manager.Task(2, "Учеба", "Нада учиться", "Отложено")
        self.manager.create_task(task)
        self.manager.remove_task_by_id(1)
        self.assertEqual(self.manager.get_tasks(), [task])


if __name__ == "__main__":
    unittest.main()