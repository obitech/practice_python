"""
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). 
"""

import math

def get_int(text="Please enter integer: "):
    while True:
        try:
            num = int(input(text))
            break
        except:
            pass

    return num

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

num = get_int()

if is_prime(num):
    print(str(num) + " is prime.")
else:
    print(str(num) + " is composite.")