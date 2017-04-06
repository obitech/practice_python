"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:
* Keep the game going until the user types “exit”
* Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random

def get_choice():
    while True:
        inp = input("> ")

        if inp == 'exit':
            return inp

        try:
            return int(inp)
        except:
            print("Invalid input")

num = random.randint(1, 9)
tries, choice = 0, 0

while choice != num:
    print("Enter your guess (or exit to abort):")
    choice = get_choice()

    if choice == 'exit':
        exit()

    if choice < num:
        print("Too low!")
        tries += 1

    elif choice > num:
        print("Too high!")
        tries += 1

    else:
        print("Correct! You finished in " + str(tries) + " attempts.")

