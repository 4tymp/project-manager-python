from objects.tasks_class import Task

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task_name, task_desc="", task_progress="todo"):
        task = Task(task_name, task_desc, task_progress)
        self.tasks.append(task)