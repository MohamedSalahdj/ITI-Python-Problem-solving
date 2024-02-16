import json

def read_users_from_json(filename="../Users/users.json"):
    try:
        users_file = open(filename, 'r')
        data = json.load(users_file )
    except Exception as e:
        return {}
    else:
        return data


def add_user_to_users_json(new_user, filename="../Users/users.json"):
    all_users = read_users_from_json('../Users/users.json')
    all_users.update(new_user)
    try:
        users_file = open(filename, 'w')
    except Exception as e:
        return False
    else:
        json.dump(all_users, users_file, indent=4)