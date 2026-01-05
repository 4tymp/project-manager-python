from utils.clear import clear_terminal

def del_project(projects_list):
    try:
        chosen_one = int(input("Ktory projekt chcesz usunac? "))
    except:
        chosen_one = len(projects_list)+1

    if chosen_one > len(projects_list):
        print("\n!! niepopoprawna liczba !!\n")
        input()
        return None
    else:
        clear_terminal()
        
        print(f"\njestes pewny ze chcesz usunac projekt numer {chosen_one}?")
        try:
            check_del = int(input("jezeli tak, wpisz jeszcze raz numer projektu który chcesz usunąc. "))
        except:
            check_del = -1

        clear_terminal()

        if check_del == chosen_one:
            projects_list.pop(chosen_one)
            print(f"!! pomyslnie usunieto projekt o indexie {chosen_one} !!\n")
            input()
        else:
            print(f"!! anulowano probe usuniecia projektu o indexie {chosen_one} !!\n")
            input()