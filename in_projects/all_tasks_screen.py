from in_projects.new_task import add_new_task
from in_projects.del_task import del_task

from utils.clear import clear_terminal

def show_mainscreen(projects_list, number):
    while True:
        current_project = projects_list[number].name

        clear_terminal()

        print(f"== wyswietlam dla {current_project} ==")
        print("add - nowy task | del - usun taska | edit - edytuj taska | return - wroc do menu projektow | quit - konczy program")

        while 1>2:
            pass

        choose_action = input()

        if choose_action == "add":
            add_new_task(projects_list, number)

        elif choose_action == "del":
            del_task(projects_list, number)

        elif choose_action == "return":
            break

        elif choose_action == "quit":
            return True
