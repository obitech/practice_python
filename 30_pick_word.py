import random

# Read file
def get_list(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file]

    except:
        print("Unable to open file.")
        return

if __name__ == "__main__":
    words = get_list("words.txt")

    len_words = len(words)

    try:
        print("Picking random value (out of " + str(len_words) + ")...")
        print("> " + random.choice(words))
    except:
        print("Unable to pick random value.")