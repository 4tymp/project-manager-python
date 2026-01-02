from utils.logo import print_logo
from utils.clear import clear_terminal
from menu.projects_list import list_projects


def main():
    clear_terminal()
    print_logo()
    
    list_projects()
