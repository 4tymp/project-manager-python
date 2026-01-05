from in_projects.new_task import add_new_task
from in_projects.del_task import del_task
from in_projects.task_display import display_tasks

from utils.clear import clear_terminal

def show_mainscreen(projects_list, number):
    while True:
        current_project = projects_list[number].name

        clear_terminal()

        print(f"== wyswietlam dla {current_project} ==")
        print(f"add - nowy task | del - usun taska | edit - edytuj taska | return - wroc do menu projektow | quit - konczy program")

        # tutaj wyswietlanie taskow!
        print("------------------------------------------------------------------------------------------------------------------")
        print("id - task - opis - progress")

        display_tasks(projects_list, number)

        choose_action = input()

        if choose_action == "add":
            add_new_task(projects_list, number)

        elif choose_action == "del":
            del_task(projects_list, number)

        elif choose_action == "return":
            break

        elif choose_action == "quit":
            return True
