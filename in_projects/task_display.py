from in_projects.group_tasks_by_progress import start_grouping_by_progress

def display_tasks(task_list):

    tasks_todo = []
    tasks_doing = []
    tasks_done = []
    tasks_fixing = []

    start_grouping_by_progress(task_list,tasks_todo,tasks_doing,tasks_done,tasks_fixing)


    print("==== TODO ====")

    for i in tasks_todo:
        print(f"{task_list.index(i)} - {i.task} - {i.desc}")

    print("==== DOING ====")    

    for i in tasks_doing:
        print(f"{task_list.index(i)} - {i.task} - {i.desc}")

    print("==== DONE ====")    

    for i in tasks_done:
        print(f"{task_list.index(i)} - {i.task} - {i.desc}")
            
    print("==== FIXING ====")    

    for i in tasks_fixing:
        print(f"{task_list.index(i)} - {i.task} - {i.desc}")