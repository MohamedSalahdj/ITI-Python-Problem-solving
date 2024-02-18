from .manipulation_users_file import read_users_from_json, add_user_to_users_json


def login():
    all_emails = list(read_users_from_json().keys())
    # print(all_emails)

    email = input("Enter your email:-- ")
    
    while email not in all_emails:
        print(f"\t ---- We don't have account with this '{email}' ---- ")
        email = input("Enter your email:-- ")

    # print(read_users_from_json())
    user_data = read_users_from_json()[email]
    email_passsword =  read_users_from_json()[email]["Password"]

    # print(email_passsword)

    password = input("Enter your password:-- ")

    while password != email_passsword:
        print(f"\t ---- password for this '{email}' not correct ---- ")
        password = input("Enter correct password:-- ")
    # print(user_data)

    user_data = {
        f"{email}": user_data
    }
    
    user_data[email]["Login"] = "True"
    # print("here",user_data)
    print("\n\t---- Login Successfully ----\n")

    add_user_to_users_json(user_data)

    return user_data[email]['Email']