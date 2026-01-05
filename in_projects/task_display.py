def display_tasks(task_list):
    
    i = 0
    while i < len(task_list):
        if task_list[i].progress == "todo":
            print(f"{i} - {task_list[i].task} - {task_list[i].desc}")
        i += 1