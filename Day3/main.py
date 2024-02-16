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
        elif option == '3':
            print("Bay ))::::-- ")
            return
        else:
            print(f"\t{sperator} incorrect option Try again {sperator}\n")
main()