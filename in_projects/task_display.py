from objects.projects_class import Project
from objects.tasks_class import Task

def display_tasks(projects_list, number):
    task_list = projects_list[number].tasks

    i = 0
    while i < len(task_list):
        print(f"{i} - {task_list[i].task} - {task_list[i].desc} - {task_list[i].progress}")
        i += 1