import csv

def create_file():
    with open("files/savedprojects.csv","w") as saved_file:
        file_writer = csv.writer(saved_file)

        file_writer.writerow(['John Smith', 'Accounting', 'November'])
        file_writer.writerow(['Erica Meyers', 'IT', 'March'])