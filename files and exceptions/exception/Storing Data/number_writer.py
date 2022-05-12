#########page-203#########
######### --- json dump ---######
"""import json
nunbers = [2, 3, 5, 7, 11, 13]
filename = "numbers.json"
with open(filename, "w") as f:
    json.dump(nunbers, f)"""

"""import json
numbers = [2, 3, 4, 5, 7]
filename = "numbers.json"
with open(filename, "w") as f:
    json.dump(numbers, f)"""

"""import json
filename = "number.json"
number = [2, 4, 5, 6]
with open(filename, "w") as f:
    json.dump(number, f)"""

"""import json
filename = "number.json"
number = "Hello world python"
with open(filename, "w") as f:
    json.dump(number, f)"""

########### readding data to json####
######using json.load############






















########## practice time #########
import json
filename = "ashardatabase.json"
databasestore = input("please write somethig for store: ")
with open(filename, "w") as f:
    json.dump(databasestore, f)




