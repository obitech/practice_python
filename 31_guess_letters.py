# from 30_pick_word import get_list

def pick_word():
    # TODO: Implement auto stuff
    return "EVAPORATE"

def get_char():
    while True:
        char = input("Guess your letter: ")

        if not char.isalpha or len(char) != 1:
            print("Invalid entry, please enter an alphabetic character.")
        else:
            return char.upper()

if __name__ == "__main__":
    word = pick_word();
    len_word = len(word)
    curr_selection = ["_" for x in range(len_word)]
    solved, tries, faults = False, 0, 0
    already_guessed = []

    print("Welcome to Hangman!")
    while not solved:
        tries += 1
        for c in curr_selection:
            print(c + ' ', end=" ")
        print()

        guess = get_char()

        if guess in word:
            for c in range(len_word):
                if guess == word[c]:
                    curr_selection[c] = guess

        else:
            if guess in already_guessed:
                print("Incorrect! You already tried that dummy...")
            else:
                print("Incorrect!")
                already_guessed.append(guess)
                
            faults += 1
            continue

        if ''.join(curr_selection) == word:
            print("Congratulations! You solved " + word + " in " + str(faults) + " tries!")
            solved = True