import json
import HandleProjects

def delete_your_projects(emailaccount):
    print("\t----- delete Your Projects -----")
    all_projects = HandleProjects.show_all_projects()
    all_user_projects = HandleProjects.show_all_projects()[emailaccount]
    
    project_name = input("Enter Project Name: ")
    
    while project_name not in list(all_user_projects.keys()):
        print(f"you don't have '{project_name}' Enter vaild name\t Enter exit to exit")
        project_name = input("Enter Project Name: ")
        if project_name == 'exit':
            return

    # print(all_user_projects)
    all_user_projects.pop(project_name)
    all_projects[emailaccount] = all_user_projects
    # print("+++"*15)
    project_file = open('DB/Projects/projects.json', 'w')
    json.dump(all_projects, project_file, indent=4)    