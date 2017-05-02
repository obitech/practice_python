def get_list(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file]

    except:
        print("Unable to open file.")
        return

def pick_word(file):
    import random

    arr = get_list(file)

    return random.choice(arr).upper()

def get_char():
    while True:
        char = input("Guess your letter: ")

        if not char.isalpha or len(char) != 1:
            print("Invalid entry, please enter an alphabetic character.")
        else:
            return char.upper()

def create_hangman(wrongs, pic=None):
    w, h = 5, 7

    if pic == None:
        # pic[7][5]
        pic = [[" " for x in range(w + 1)] for y in range(h + 1)]

    # Top beam
    pic[0][w-1] = "+"
    pic[0][0] = "+"
    for i in range(1, w-1):
        pic[0][i] = "-"

    pic[1][1] = "/"
    pic[1][w-1] = "|"

    # Main beam
    for i in range(1, h):
        pic[i][0] = "|"

    # Bottom
    for i in range(w+1):
       pic[h][i] = "="

    # Make guy
    if wrongs == 1:
        pic[2][4] = "O"
    elif wrongs == 2:
        pic[3][4] = "|"
    elif wrongs == 3:
        pic[3][3] = "/"
    elif wrongs == 4:
        pic[3][5] = "\\"
    elif wrongs == 5:
        pic[4][3] = "/"
    elif wrongs == 6:
        pic[4][5] = "\\"
    else:
        pass

    return pic

def print_hangman(hangman):
    for y in range(8):
        for x in range(6):
            print(hangman[y][x], end=" ")
        print()

if __name__ == "__main__":
    word = pick_word("words.txt");
    len_word = len(word)
    curr_selection = ["_" for x in range(len_word)]
    solved, faults = False, 0
    already_guessed = []
    hangman = create_hangman(faults)

    print("Welcome to Hangman!")
    while not solved:
        print("Current tries: " + str(faults))
        hangman = create_hangman(faults, hangman)
        print_hangman(hangman)

        for c in curr_selection:
            print(c + " ", end=" ")
        print()

        if faults < 6:
            guess = get_char()

            if guess in word:
                for c in range(len_word):
                    if guess == word[c]:
                        curr_selection[c] = guess

            else:
                if faults < 6:
                    if guess in already_guessed:
                        print("Incorrect! You already tried that dummy...")
                    else:
                        print("Incorrect!")
                        already_guessed.append(guess)

                    faults += 1
                    continue
                else:
                    break
        else:
            print("You guessed too many times. The word was " + word)
            break

        if ''.join(curr_selection) == word:
            print("Congratulations! You solved " + word + " in " + str(faults) + " tries!")
            solved = True