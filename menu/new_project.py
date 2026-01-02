import menu.mainmenu as mainmenu
from utils.clear import clear_terminal

def add_new_project(projects_list):
    clear_terminal()

    new_project_name = input(f"jak ma sie nazywac?\n")
    projects_list.append(new_project_name)

    clear_terminal()
    print(f"dodano {new_project_name}.\n")
