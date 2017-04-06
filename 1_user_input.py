"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
* Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
* Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

"""

import datetime

name = input("Please enter name: ")

# Get age
while True:
    try:
        age = int(input("Please enter age: "))
        break
    except:
        print("Please enter integer.")

# Get repeats
while True:
    try:
        repeats = int(input("How often you want to repeat this message? "))
        break
    except:
        print("Please enter integer.")

now = datetime.datetime.now()

print(("Hello " + str(name) + ", you are " + str(age) + " years old. In year " + str((now.year + (100 - age))) + " you will be 100 years old!\n") * repeats)