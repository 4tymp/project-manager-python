from corefunctions.new_project import add_new_project

projects_list = ["utworz nowy"]

def list_projects():
    
    project_number = None

    while True:
        print(f"Wybierz projekt:\n")

        indexes = 0
        for i in projects_list:
            print(f"{indexes} - {i}")
            indexes += 1

        project_number = input("")

        if project_number == "0":
            add_new_project(projects_list)
    