import json
import HandleProjects
from datetime import datetime

def validate_dates(start_time, end_time):
    try:
        start_date = datetime.strptime(start_time, '%Y-%m-%d')
        end_date = datetime.strptime(end_time, '%Y-%m-%d')
        print("start date after strip--->  " , start_date)
        print("end date after strip--->  ", end_date)
        if start_date >= end_date:
            return False
        return True
    except ValueError:
        return False

def edit_your_projects(emailaccount):
    print("\t----- Edit Your Projects -----")
    all_projects = HandleProjects.show_all_projects()
    all_user_projects = HandleProjects.show_all_projects()[emailaccount]

    project_name = input("Enter Project Name: ")

    while project_name not in list(all_user_projects.keys()):
        print(f"you don't have '{project_name}' Enter vaild name\t OR exit to exit")
        project_name = input("Enter Project Name: ")
        if project_name == 'exit':
            return
    
    user_project_info = HandleProjects.show_all_projects()[emailaccount][project_name]
    print("\t ---- you can't edit project name ----")
    
    # upgrade new feature 
    # print("\tTo edit 'project details' Enter '1'\n To edit 'Total taeget' Enter '2'\nTo edit 'start time' Enter '3'\nTo edit 'end time' Enter '4'")
    # i = 0
    # while i < 4:


    project_details = input("Enter New Project details:... ")
    project_total_target = input("Enter New Project Total target (like this i.e 250000 EGP)  ")
    project_start_time = input("Enter New Project Start Time:... ")
    project_end_time = input("Enter New Project End Time:... ")


    while not validate_dates(project_start_time, project_end_time):
        print('\t ---- Entered tncorrect time Try again ----\n')
        project_start_time = input("Enter Project Start Time like this 2023-6-18 :... ")
        project_end_time = input("Enter Project End Time like this 2023-9-18 :... ")

    all_user_projects[user_project_info['ProjectTitle']] = {
            "ProjectTitle": user_project_info['ProjectTitle'],
            "Details": project_details,
            "TotalTarget ": project_total_target,
            "startTime": project_start_time,
            "endTime": project_end_time
        }
    all_projects.update({emailaccount:all_user_projects})
    print("\n\nhere",all_projects)
    project_file = open('DB/Projects/projects.json', 'w')

    json.dump(all_projects, project_file, indent=4)
    project_file.close()

    print(user_project_info)