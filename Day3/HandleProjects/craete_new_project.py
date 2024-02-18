import json
from datetime import datetime
import HandleProjects


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


def craete_new_project(emailaccount):
    print("\t----- Create New Project -----")
    print(emailaccount)

    all_projects =  HandleProjects.show_all_projects()
    all_users_have_projects =  list(HandleProjects.show_all_projects().keys())

    project_title = input("Enter Project title:... ")
    project_details = input("Enter Project details:... ")
    project_total_target = input("Enter Project Total target (like this i.e 250000 EGP)  ")
    project_start_time = input("Enter Project Start Time:... ")
    project_end_time = input("Enter Project End Time:... ")

    while not validate_dates(project_start_time, project_end_time):
        print('\t ---- Entered tncorrect time Try again ----\n')
        project_start_time = input("Enter Project Start Time like this 2023-6-18 :... ")
        project_end_time = input("Enter Project End Time like this 2023-9-18 :... ")


    if emailaccount in all_users_have_projects:
        all_user_projects = HandleProjects.show_all_projects()[emailaccount]

     
        all_user_projects[project_title] = {
            "ProjectTitle": project_title,
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
    else:
        project_details = {
            project_title: {
                "ProjectTitle": project_title,
                "Details": project_details,
                "TotalTarget ": project_total_target,
                "startTime": project_start_time,
                "endTime": project_end_time
            }}

        new_project = {
            emailaccount : project_details
        }
        print(emailaccount)
        all_projects.update(new_project)
        project_file = open('DB/Projects/projects.json', 'w')
        json.dump(all_projects, project_file, indent=4)
        



    
    