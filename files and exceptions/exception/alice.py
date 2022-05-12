#file not found error page 197
"""filename = "alice.txt"
with open(filename) as f:
    contents = f.read()""" #that find error

#soved
"""filename = "alice.txt"
try:
    with open(filename) as f:
        content = f.read()
except FileNotFoundError:
    print(f"Sorry, the '{filename}' does not exist.")"""

#practice file
"""filename = "alice.txt"
try:
    with open(filename) as f:
        content = f.read()
except FileNotFoundError:
    print(f"'{filename}' does't exist.")
else:
    print(content)"""
#If there not exist file .txt then FileNotFoundeError showing-
#if we want to write but file is not here then programm automaticaly-
#make the programm

#practice file
"""filename = "a.txt"
x = input("write something for store to the file: ")
try:
    with open(filename, "w") as f:
        f.write(x)
except FileNotFoundError:
    print(f"here '{filename}' dose't exist.")
else:
    with open(filename) as f:
        content = f.read()
        print(content)
"""
# trying that without try then what happend

"""filename = "ax.txt"
x = input("write ")
with open(filename, "w") as f:
    f.write(x)
"""

########### Analyzing Test ############
##page -198

"""title = "Alice in wonderland"
title.split()
["Alice", "in", "wonderland"]
filename = "alice.txt"
try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exits.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")"""

takenfile = input("store file name please without extention: ")
filename = takenfile + ".txt"
try:
    with open(filename) as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print(f"sorry this {filename} is not exist.")
else:
    x = content.split()
    print(len(x))



