from menu.new_project import add_new_project
from menu.del_project import del_project

from in_projects.all_tasks_screen import show_mainscreen
from utils.clear import clear_terminal

projects_list = []

def list_projects():
    
    choose_action = None

    while True:
        print("== Wybierz projekt: ==")
        print("add - tworzy nowy projekt | del - usun wybrany projekt | quit - konczy program\n")
        
        indexes = 0
        while indexes < len(projects_list):
            print(f"{indexes} - {projects_list[indexes].name}")
            indexes += 1

        choose_action = input()

        if choose_action == "add":
            add_new_project(projects_list)

        elif choose_action == "del":
            del_project(projects_list)

        elif choose_action == "quit":
            return False
        
        else:
            project_number = int(choose_action)

            if project_number >= len(projects_list):
                clear_terminal()
                print(f"\nNie ma projektu z takim numerem.\n")
            else:
                show_mainscreen(projects_list, project_number)
        
        
    