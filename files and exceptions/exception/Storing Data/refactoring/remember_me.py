"""import json
def greet_user():
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("what id your name?: ")
        with open(filename, "w") as f:
            json.dump(username,f)
            print(f"we'll remember you when you come back, {username}!")
    else:
        print(f"welcome back, {username}!")
greet_user()"""
######################################################
"""import json
def greet_user():
    filename = "ashar.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("what's your name?: ")
        with open(filename, "w") as f:
            json.dump(username, f)
            print(f"welcome to our site {username}!")
    else:
        print(f"welcome beck {username}!")
greet_user()"""
###########################################################

"""import json
def get_stored_username():
    filename = "username.json"
    try:
        with open(filename)as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("Whar is your name? ")
        filename = "username.json"
        with open(filename, "w") as f:
            json.dump(username, f)
            print(f"we'll remember you when you come back, {usename}!")
greet_user()"""
########################################################

import json
def get_stored_username():
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
def ger_new_username():
    username = input("what is your name?: ")
    filename = "username.json"
    with open(filename, "w") as f:
        json.dump(username, f)
    return username
def greet_user():
    username = get_stored_username()
    if username:
        print(f"welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"we'll remember you when you come back, {username}!")
greet_user()