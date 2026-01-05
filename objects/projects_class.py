from objects.tasks_class import Task

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)