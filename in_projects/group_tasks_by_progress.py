def start_grouping_by_progress(task_list,tasks_todo,tasks_doing,tasks_done,tasks_fixing):
    i = 0
    while i < len(task_list):
        if task_list[i].progress == "todo":
            tasks_todo.append(task_list[i])
        elif task_list[i].progress == "doing":
            tasks_doing.append(task_list[i])
        elif task_list[i].progress == "done":
            tasks_done.append(task_list[i])
        elif task_list[i].progress == "fixing":
            tasks_fixing.append(task_list[i])
        i += 1