from in_projects.group_tasks_by_progress import start_grouping_by_progress

def display_tasks(task_list):

    tasks_todo, tasks_doing, tasks_done, tasks_fixing = start_grouping_by_progress(task_list)

    print("==== TODO ====")

    for index,task in tasks_todo:
        print(f"{index} - {task.task} - {task.desc}")

    print("\n==== DOING ====")    

    for index,task in tasks_doing:
        print(f"{index} - {task.task} - {task.desc}")

    print("\n==== DONE ====")    

    for index,task in tasks_done:
        print(f"{index} - {task.task} - {task.desc}")
            
    print("\n==== FIXING ====")    

    for index,task in tasks_fixing:
        print(f"{index} - {task.task} - {task.desc}")