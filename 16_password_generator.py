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
def generate_password(length=5):

    if length == 0:
        return None

    pool = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?+=-_[]"

    return ''.join([random.choice(pool) for x in range(length)])

# Test
for i in range(10):
    print(generate_password(random.randint(0, 20)))