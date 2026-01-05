from utils.clear import clear_terminal
from objects.projects_class import Project
from objects.tasks_class import Task

def del_task(task_list):
    chosen_one = int(input("Ktory task chcesz usunac? "))

    clear_terminal()
    
    print(f"\njestes pewny ze chcesz usunac task numer {chosen_one}?")
    try:
        check_del = int(input("jezeli tak, wpisz jeszcze raz numer taska który chcesz usunąc. "))
    except:
        check_del = -1
    
    clear_terminal()

    if check_del == chosen_one:
        task_list.pop(chosen_one)
        print(f"pomyslnie usunieto task o id {chosen_one}.\n")
    else:
        print(f"anulowano probe usuniecia taska o id {chosen_one}")

    input()