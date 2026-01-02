from objects.projects_class import Project
from objects.tasks_class import Task

from utils.clear import clear_terminal

def show_mainscreen(projects_list, number):
    current_project = projects_list[number].name

    clear_terminal()

    print(f"== wyswietlam dla {current_project} ==")
    input()
