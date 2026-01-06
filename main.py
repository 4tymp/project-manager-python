import os

from menu.projects_list import list_projects
from utils.loading import load_file

projects_list = []

if os.path.exists("files/savedprojects.csv"):
    load_file(projects_list)
    
list_projects(projects_list)
