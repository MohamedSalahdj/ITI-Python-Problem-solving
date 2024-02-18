import os
import json
import AuthenticationSystem as authSys
import HandleProjects 

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

sperator = '-----'

def main():
    while True:
        print(f"\t{sperator} To Regitser Enter '1' {sperator} \n\t{sperator} To Login Enter '2' {sperator} \n\t{sperator} To Exist Enter '3' {sperator} ")
        option = input("Enter Your option:..... ")
        if option == '1':
            authSys.register()
        elif option == '2':
            emailaccount = authSys.login()
            while True:
                print(f"\t{sperator} To Show All Projects Enter '1' {sperator} \n\t{sperator} To Create new Project Enter '2' {sperator} \n\t{sperator} To Edit Your Own Projects '3' {sperator} \n\t{sperator} To Delete Your Own Projects Enter '4' {sperator}\n\t{sperator} To Exist Enter '5' {sperator} ")
                project_option = input("Enter Your option:..... ")
                if project_option == '1':
                    formatted_data = json.dumps(HandleProjects.show_all_projects(), indent=4) 
                    print("\t----- This All Projects -----")
                    print(formatted_data)
                elif project_option == '2':
                    HandleProjects.craete_new_project(emailaccount)
                elif project_option == '3':
                    HandleProjects.edit_your_projects(emailaccount)
                elif project_option == '4':
                    HandleProjects.delete_your_projects(emailaccount)
                elif project_option == '5':
                    print("returned to main menu----")
                    break
                else:
                   print(f"\t{sperator} incorrect option Try again {sperator}\n")

        elif option == '3':
            print("Bay ))::::-- ")
            return
        else:
            print(f"\t{sperator} incorrect option Try again {sperator}\n")
main()