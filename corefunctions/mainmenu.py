from utils.logo import print_logo
from utils.clear import clear_terminal
from corefunctions.projects_list import list_projects


def main():
    clear_terminal()
    print_logo()

    print(f"Wybierz projekt:")
    
    list_projects()
