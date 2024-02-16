import json, os
from .pattern_validation import is_name_vaild, is_email_vaild, is_password_vaild, is_mobile_number_vaild
from .manipulation_users_file import read_users_from_json, add_user_to_users_json

os.chdir(os.path.dirname(os.path.abspath(__file__)))


users = {}

def register():
    print("\t---- Welcome from Registeration Page ---\n")

    first_name = input("Enter Your First Name: ")
    while not is_name_vaild(first_name):
        first_name = input("Enter Your First Name: ")
    
    last_name = input("Enter Your Last Name: ")
    while not is_name_vaild(last_name):
        last_name = input("Enter Your Last Name: ")

    email = input("Enter your Email: ").lower()
    all_emails = list(read_users_from_json().keys())

    while email in all_emails:
        print(f"\t ----- this '{email}' already exist -----")
        email = input("Enter your Email: ").lower()

    while not is_email_vaild(email):
        email = input("Enter your Email: ").lower()


    password = input("Enter your Password: ")
    while not is_password_vaild(password):
        password = input("Enter your Password: ")

    confirm_password = input("Confirm Password: ")
    while password !=confirm_password:
        confirm_password = input("\npassword not matched try agaain\nConfirm Password: ")
    
    mobile_number = input("Enter your Mobile Number: ")
    while not is_mobile_number_vaild(mobile_number):
        mobile_number = input("Enter your Mobile Number: ")

    users[email] = {
        "FirstName" : first_name,
        "LastName" : last_name,
        "Email" : email,
        "Password" : password,
        "MobileNumber" : mobile_number
    }
    
    add_user_to_users_json(users, '../Users/users.json')

    
