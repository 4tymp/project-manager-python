def start_grouping_by_progress(task_list):
    tasks_todo = []
    tasks_doing = []
    tasks_done = []
    tasks_fixing = []

    for index,task in enumerate(task_list):
        if task.progress == "todo":
            tasks_todo.append((index,task))
        elif task.progress == "doing":
            tasks_doing.append((index,task))
        elif task.progress == "done":
            tasks_done.append((index,task))
        elif task.progress == "fixing":
            tasks_fixing.append((index,task))

    return tasks_todo, tasks_doing, tasks_done, tasks_fixing