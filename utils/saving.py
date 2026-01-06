import csv

def save_file(projects_list):
    with open("files/savedprojects.csv","w", newline="") as saved_file:
        file_writer = csv.writer(saved_file)

        file_writer.writerow(["PROJEKT","TASK","OPIS","PROGRESS"])
        
        for project in projects_list:
            for task in project.tasks:
                file_writer.writerow([project.name,task.task,task.desc,task.progress])