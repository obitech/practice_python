"""
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

* Rock beats scissors
* Scissors beats paper
* Paper beats rock
"""

def get_weapon():
    valid = ['rock', 'r', 'paper', 'p', 'pap', 'scissors', 'sci', 's', 'sciss', 'scis']
    
    while True:
        inp = input("Choose between Rock/Paper/Scissors: ").lower()

        if inp in valid:
            if inp[0] == 'r':
                return 'r'
            elif inp[0] == 'p':
                return 'p'
            else:
                return 's'
        else:
            print("Invalid choice.")

def get_yn():
    while True:
        check = input("Do you want to play again (y/n)? ").lower()

        if check[0] == 'y' or check[0] == 'j':
            return True
        elif check[0] == 'n':
            return False
        else:
            print("Invalid choice.")

playing = True

while playing:
    print("-- Player 1 --")
    p1 = get_weapon()

    print("-- Player 2 --")
    p2 = get_weapon()

    print(p1 + p2)

    # p1 == 'r'
    if p1 == 'r' and p2 == 's':
        print("Player 1 wins!")
    elif p1 == 'r' and p2 == 'p':
        print("Player 2 wins!")

    # p1 == 'p'
    elif p1 == 'p' and p2 == 'r':
        print("Player 1 wins!")
    elif p1 == 'p' and p2 == 's':
        print("Player 2 wins!")

    # p1 == 's'
    elif p1 == 's' and p2 == 'r':
        print("Player 2 wins!")
    elif p1 == 's' and p2 == 'p':
        print("Player 1 wins!")

    else:
        print("Draw!")

    check = get_yn()

    if not check:
        playing = False