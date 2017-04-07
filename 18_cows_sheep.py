import random
import sys

def get_yn():
    while True:
        check = input("Do you want to play again (y/n)? ").lower()

        if check[0] == 'y' or check[0] == 'j':
            return True
        elif check[0] == 'n':
            return False
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    print("Welcome to the game! A random number has been generated, which you have to guess.")
    print("For every digit which is _correct but not in the right place_ you will get one _sheep_.")
    print("For every digit which is _correct and in the right place_ you will get a _cow_")
    print("Good luck!\n")

    playing = 1
    num = str(random.randint(1000, 9999))
    guess = 0
    cows = 0

    # Debug
    print(num)

    while playing:
        while cows != 4:
            inp = input("Please enter your guess or 'exit' to quit: ")
            
            if inp == 'exit':
                sys.exit(0)

            cows, sheep = 0, 0
            
            for i in range(len(inp)):
                if inp[i] in num:
                    if inp[i] == num[i]:
                        cows += 1
                    else:
                        sheep += 1
            print(str(cows) + " cows, " + str(sheep) + " sheep.")
            guess += 1

        print("Congratulations, you guessed correctly after " + str(guess) + " tries!")
        check = get_yn()
        if not check:
            playing = 0
