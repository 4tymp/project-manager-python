from utils.clear import clear_terminal

def add_new_task(projects_list, number):
    clear_terminal()

    name = input("nowy task: ")

    projects_list[number].add_task(name)

    clear_terminal()
    print(f"!! pomyślnie dodano {name} !!")
    input() #pauuje caly program zeby dal osie odczytac komunikat
