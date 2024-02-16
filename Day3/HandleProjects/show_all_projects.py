import json

def show_all_projects():
    print("\t----- This All Projects -----")
    try:
        projects_file = open('DB/Projects/projects.json', 'r')
        data = json.load(projects_file)
        formatted_data = json.dumps(data, indent=4)

    except Exception as e:
        print('no data')
        return {}
    else:
        print(formatted_data)
