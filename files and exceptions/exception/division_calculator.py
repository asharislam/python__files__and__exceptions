###########194

"""try:
    x = int(input("please give me a number: "))
    y = int(input("by divide number: "))
    print(x/y)
except ZeroDivisionError:
    print(f"for {x} you can't divide by zero!")
else:
    print(f"your answer is {x/y}")"""

#main formula
"""try:
    print(5/0)
except ZeroDivisionError:
    print("You Can't Divided By Zero!")"""

## using exceptions to prevent
"""print("Give me two number or Enter 'q' to exit: ")
while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("\nSecond number: ")
    if second_number == "q":
        break
    answer = int(first_number)/ int(second_number)
    
    print(f"your answer is: {float_answer}")"""

#practice season
"""print(" Enter'q' for Exit OR Please Give me two number for Divide: ")
while True:
    x = input("please Give me a number: ")
    if x == "q":
        break
    y = input("Please Give me second number: ")
    if y == "q":
        break
    z = int(x)/int(y)
    print(f"Your answer is: {z}")"""

#practice while and try both
print(" Enter'q' for Exit OR Please Give me two number for Divide: ")

while True:
    x = input("please Give me a number: ")
    if x == "q":
        break
    y = input("Please Give me second number: ")
    if y == "q":
        break
    try:
        z = int(x)/int(y)
    except ZeroDivisionError:
        print("you can't devided by zero.")
    else:
        z = int(x)/int(y)
        print(f"Your answer is: {z}")