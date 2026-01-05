from objects.tasks_class import Task

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task_name, desc):
        task = Task(task_name,desc)
        self.tasks.append(task)