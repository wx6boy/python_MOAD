from collections import defaultdict


class Task:
    def __init__(self, id, name, description, status="Started"):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__status = status

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status


class Subtask(Task):
    # have comlex task id
    def __init__(self, task: Task, parent_id):
        super().__init__(task.get_id(), task.get_name(), task.get_description(), task.get_status())
        self.parent_id = parent_id

    def get_parent_id(self):
        return self.parent_id


class ComplexTask(Task):
    # contains list of subtasks
    def __init__(self, task: Task):
        super().__init__(task.get_id(), task.get_name(), task.get_description(), task.get_status())
        self.subtasks = []


class TaskManager:
    id_series = 0

    def __init__(self):
        self.complex_tasks = defaultdict(ComplexTask)
        self.tasks = defaultdict(Task)
        self.subtasks = defaultdict(Subtask)

    def __get_and_increment_id(self):
        next_id_value = TaskManager.id_series
        TaskManager.id_series += 1
        return next_id_value

    def create_task(self, name, description):
        current_id = self.__get_and_increment_id()
        new_task = Task(current_id, name, description)
        self.tasks[current_id] = new_task
        return new_task

    def create_subtask(self, subtask: Task, parent_id):
        if parent_id not in self.complex_tasks:
            self.create_complex_task(self.tasks[parent_id])
        self.tasks.pop(subtask.get_id(), None)
        self.subtasks[subtask.get_id] = Subtask(subtask, parent_id)
        self.complex_tasks[parent_id].subtasks.append(subtask.get_id())

    def create_complex_task(self, complex_task):
        if complex_task.get_id() not in self.complex_tasks:
            self.complex_tasks[complex_task.get_id()] = ComplexTask(complex_task)
            self.tasks.pop(complex_task.get_id(), None)
        return self.complex_tasks[complex_task.get_id()]

    def get_tasks(self):
        return list(self.tasks.values())

    def get_subtasks(self):
        return list(self.subtasks.values())

    def get_complex_tasks(self):
        return list(self.complex_tasks.values())

    def get_tasks_by_id(self, id):
        return self.tasks[id]

    def get_subtasks_by_id(self, id):
        return self.subtasks[id]

    def get_complex_tasks_by_id(self, id):
        return self.tasks[id]

    def remove_tasks(self):
        self.tasks = defaultdict(Task)

    def remove_subtasks(self):
        self.subtasks = defaultdict(Subtask)
        for key in self.complex_tasks:
            self.tasks[self.complex_tasks[key].get_id()] = Task(self.complex_tasks[key].get_id(),
                                                                self.complex_tasks[key].get_name(),
                                                                self.complex_tasks[key].get_description(),
                                                                self.complex_tasks[key].get_status())
        self.complex_tasks = defaultdict(ComplexTask)

    def remove_complex_tasks(self):
        self.complex_tasks = defaultdict(ComplexTask)
        self.subtasks = defaultdict(Subtask)

    def remove_task_by_id(self, id):
        self.tasks.pop(id, None)

    def remove_subtask_by_id(self, id):
        self.complex_tasks[self.subtasks[id].get_parent_id()].subtasks.remove(id)
        if not self.complex_tasks[self.subtasks[id].get_parent_id()].subtasks:
            self.tasks[self.complex_tasks[self.subtasks[id].get_parent_id()].get_id()] = \
                Task(self.complex_tasks[self.subtasks[id].get_parent_id()].get_id(),
                     self.complex_tasks[self.subtasks[id].get_parent_id()].get_name(),
                     self.complex_tasks[self.subtasks[id].get_parent_id()].get_description(),
                     self.complex_tasks[self.subtasks[id].get_parent_id()].get_status())
            self.complex_tasks.pop(self.subtasks[id].get_parent_id(), None)
        self.subtasks.pop(id, None)

    def remove_complex_task_by_id(self, id):
        for key in self.subtasks:
            if self.subtasks[key].get_parent_id() == id:
                self.subtasks.pop(key, None)

        self.complex_tasks.pop(id, None)

    def update_status(self, task, status):
        if task.get_id() in self.complex_tasks:
            self.complex_tasks[task.get_id()].set_status(status)
        elif task.get_id() in self.subtasks:
            self.subtasks[task.get_id()].set_status(status)
        elif task.get_id() in self.tasks:
            self.tasks[task.get_id()].set_status(status)


if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.create_task("Работа", "Выполнить работу по клиенту 1")
    task_manager.create_task("Учеба", "Линейная алгебра")
    task_manager.create_task("Работа", "Выполнить работу по клиенту 2")
    task_manager.create_task("Учеба", "Философия")
    task_manager.create_task("Работа", "Выполнить работу по клиенту 3")
    task_manager.create_task("Учеба", "Программирование")
    new_task = task_manager.create_task("Учеба", "Теория вероятностей")
    general_task = task_manager.create_task("Учеба", "Неделя 1")
    task_manager.update_status(new_task, "Finished")
    task_manager.update_status(general_task, "dd")
    task_manager.create_subtask(new_task, general_task.get_id())
    task_manager.remove_subtasks()
    tasks = task_manager.get_tasks()
    for i in tasks:
        print(i.get_status())