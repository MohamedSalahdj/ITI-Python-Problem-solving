import AuthenticationSystem

sperator = '-----'

def main():
    while True:
        print(f"\t{sperator} To Regitser Enter '1' {sperator} \n\t{sperator} To Login Enter '2' {sperator} \n\t{sperator} To Exist Enter '3' {sperator} ")
        option = input("Enter Your option:..... ")
        if option == '1':
            AuthenticationSystem.register()
        elif option == '2':
            AuthenticationSystem.login()
            while True:
                print(f"\t{sperator} To Show All Projects Enter '1' {sperator} \n\t{sperator} To Edit Your Own Projects '2' {sperator} \n\t{sperator} To Delete Your Own Projects Enter '3' {sperator}\n\t{sperator} To Exist Enter '4' {sperator} ")
                project_option = input("Enter Your option:..... ")
                if project_option == '1':
                    print("Show all projects ----")
                elif project_option == '2':
                    print("Edit your projects ----")
                elif project_option == '3':
                    print("Delete your projects ----")
                elif project_option == '4':
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