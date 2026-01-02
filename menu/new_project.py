from objects.projects_class import Project
from utils.clear import clear_terminal

def add_new_project(projects_list):
    clear_terminal()

    name = input(f"jak ma sie nazywac?\n")

    new_project = Project(name)
    projects_list.append(new_project)


    clear_terminal()
    print(f"!! pomyslnie dodano {name}. !!")
    input() # pauzuje calosc zeby bylo widac ze dodano
