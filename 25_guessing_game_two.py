"""
In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. 
The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
At the end of this exchange, your program should print out how many guesses it took to get your number.
As the writer of this program, you will have to choose how your program will strategically guess. 
A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. 
But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. 
After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)
"""

def get_inp(num):
    while True:
        text = "My guess is: " + str(num) + ". Is my guess correct (c), too high (h) or too low (l)?"
        inp = input(text).lower()

        if inp[0] == 'c' or inp[0] == 'h' or inp[0] == 'l':
            return inp

        print("Invalid entry.")


if __name__ == "__main__":
    guess = 1
    arr = list(range(101))
    num = arr[len(arr) // 2]
    print("Please think of a number between 0 and 100 (inclusive) and I will try to guess it.")

    inp = get_inp(num)

    while inp != 'c':
        leng = len(arr)

        if inp == 'h':
            arr = arr[:leng // 2]
            
        elif inp == 'l':
            arr = arr[leng // 2:]

        else:
            break
        
        num = arr[len(arr) // 2]
        guess += 1
        inp = get_inp(num)

    print("I guessed your number after " + str(guess) + " tries.")