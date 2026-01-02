from menu.new_project import add_new_project
from menu.del_project import del_project

projects_list = []

def list_projects():
    
    project_number = None

    while True:
        print(f"Wybierz projekt:")
        print("add - tworzy nowy projekt | del - usun wybrany projekt | quit - konczy program\n")
        
        indexes = 0
        for i in projects_list:
            print(f"{indexes} - {i}")
            indexes += 1

        project_number = input()

        if project_number == "add":
            add_new_project(projects_list)

        if project_number == "del":
            del_project(projects_list)
        
        if project_number == "quit":
            return False
    