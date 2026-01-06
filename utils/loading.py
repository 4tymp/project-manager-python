from objects.projects_class import Project

import csv

def load_file(projects_list):
    with open('files/savedprojects.csv') as saved_file:
        file_reader = csv.reader(saved_file)

        old_project = None
        project_index = -1

        next(file_reader)

        for row in file_reader:
            
            project_name = row[0]

            if project_name != old_project:
                new_project = Project(project_name)
                projects_list.append(new_project)
                project_index += 1
                old_project = project_name

            projects_list[project_index].add_task(row[1], row[2], row[3])
