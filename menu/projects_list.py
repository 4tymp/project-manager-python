from menu.new_project import add_new_project
from menu.del_project import del_project

from in_projects.all_tasks_screen import show_mainscreen
from utils.clear import clear_terminal
from utils.logo import print_logo

projects_list = []

def list_projects():
    
    choose_action = None

    while True:
        clear_terminal()
        print_logo()

        print("== Wybierz projekt: ==")
        print("add - tworzy nowy projekt | del - usun wybrany projekt | quit - konczy program")
        
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
            break
        
        else:
            try:
                project_number = int(choose_action)
            except:
                project_number = len(projects_list)+1

            if project_number >= len(projects_list):
                clear_terminal()
                print(f"\nNie ma projektu z takim numerem ani takiej komendy.\n")
            else:

                check_quit = show_mainscreen(projects_list, project_number)
                if check_quit == True: ##jezeli w ekranie projektu wpiszesz quit zamiast return program sie konczy
                    break