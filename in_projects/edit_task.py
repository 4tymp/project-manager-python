def edit_task(task_list):
    print() #dodane dla estetyki panowie
    try:
        chosen_one = int(input("ktorego taska chcesz edytowac? "))
    except:
        chosen_one = len(task_list)+1

    if chosen_one > len(task_list):
        print("\n!! Nie ma takiego taska !!\n")
        input()
    else:
        print("")
        edited_element = input("co chcesz edytować? (1 - progress, 2 - task, 3 - opis) ")

        if edited_element == "1" or edited_element == "progress":
            print("\npodaj nowy progress:")
            new_value = input("0 - todo | 1 - doing | 2 - done | 3 - fixing ")

            if new_value == "0" or new_value == "todo":
                task_list[chosen_one].progress = "todo"
            elif new_value == "1" or new_value == "doing":
                task_list[chosen_one].progress = "doing"
            elif new_value == "2" or new_value == "done":
                task_list[chosen_one].progress = "done"
            elif new_value == "3" or new_value == "fixing":
                task_list[chosen_one].progress = "fixing"
            
            print(f"\n!! pomyslnie zmieniono progress taska o id {chosen_one} na {task_list[chosen_one].progress} !!\n")
            input()

        elif edited_element == "2" or edited_element == "task":
            print(f"\npodaj nowego taska:")
            new_value = input()
            task_list[chosen_one].task = new_value

            print(f"\n!! poprawnie zmieniono taska o id {chosen_one} na {new_value} !!\n")
            input()

        elif edited_element == "3" or edited_element == "opis":
            print(f"\npodaj nowy opis:")
            new_value = input()
            task_list[chosen_one].desc = new_value

            print(f"\n!! poprawnie zmieniono opis taska o id {chosen_one} na {new_value} !!\n")
            input()
        else:
            print(f"\n!! nie ma takiego elementu !!\n")
            input()
