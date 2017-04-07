"""
Write a password generator in Python. Be creative with how you generate passwords,
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.

Extra:
* Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""

import random

# Pick a strength: 1 = weak, 2 = mid, 3 = strong
def generate_password(strength=2):

    if (strength < 1) or (strength > 3):
        print("Please enter a strength between 1 and 3 (inclusively)")
        return None

    pool = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    1,2,3,4,5,6,7,8,9,0,
    '!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '=', '-', '+']

    password = []

    # Determining length of password
    if strength == 1:
        length = random.randint(5, 10)
    elif strength == 2:
        length = random.randint(11, 20)
    else:
        length = random.randint(21, 50)

    # Randomly pick from pool
    for i in range(length):
        char = random.choice(pool)

        # Randomize upper/lower
        if type(char) == str and char.isalpha():
            if random.randint(0, 1) == 1:
                char = char.upper()

        password.append(char)

    # Randomize for good measure
    for i in range(10):
        random.shuffle(password)

    # print("Returning: " + str(password))
    return ''.join(str(x) for x in password if x != type(str))

def test_weak(n=5):
    print("Weak passwords:")

    for i in range(n):
        print(str(generate_password(1)))
    print()

def test_mid(n=5):
    print("Mid passwords:")

    for i in range(n):
        print(str(generate_password(2)))
    print()

def test_strong(n=5):
    print("Strong passwords:")

    for i in range(n):
        print(str(generate_password(3)))
    print()

test_weak(10)
test_mid(10)
test_strong(10)