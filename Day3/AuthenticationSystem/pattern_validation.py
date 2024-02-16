import re

def is_name_vaild(name):
    name_pattern = r'^[a-zA-Z\s]+$'

    if re.match(name_pattern, name):
        return True
    
    print("your name is not valid should name contain only character!!...... ")
    return False

def is_email_vaild(email):
    email_pattern = r'^[\w\.-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'

    if re.match(email_pattern, email):
        return True
    
    print("your email is not valid!---- try again ----  ")
    return False

def is_password_vaild(password):
    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'

    if re.match(password_pattern, password):
        return True
    
    print("\tyour password not valid!---- \nshould contain at least one lowercase letter and one one uppercase letter and one digit and minimum lenght '8' characters ----  ")
    return False

def is_mobile_number_vaild(mobilenum):
    mobile_number_pattern = r'^(010|011|012|015)\d{8}$'


    if re.match(mobile_number_pattern, mobilenum):
        return True
    
    print("\tyour mobile number is not valid!---- \n\ttry agian--- ")
    return False



