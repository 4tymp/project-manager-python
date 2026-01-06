from menu.projects_list import list_projects
from utils.loading import load_file

projects_list = []

load_file(projects_list)
list_projects(projects_list)
