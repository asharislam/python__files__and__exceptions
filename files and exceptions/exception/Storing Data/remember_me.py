########################## page --205
"""import json

filename = "username.json"
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("whats your name: ")
    with open(filename, "w") as f:
        print(f"we'll remember you when you come beck, {username}!")
else:
    print(f"welcome back, {username}!")"""

###############################################
"""
import json

filename = "username.json"
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("what is your name?")
    with open(filename, "w") as f:
        json.dump(username, f)
        print(f"we'll remember you when you come back, {username}!")
else:
    print(f"welcome back, {username} !")"""

##########################
"""import json

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")"""


#######################################

"""import json
filename = "username.json"
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What's your name?: ")
    with open(filename, "w") as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username} !.")
else:
    print(f"Welcome back {username}! .")"""

######################################################
import json
filename = "username.json"
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name?: ")
    with open(filename, "w") as f:
        json.dump(username, f)
        print(f"Hell {username}.")
else:
    print(f"Welcome beck {username}.")