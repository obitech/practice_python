"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

def is_palin(string):
    if string[::-1].lower() == string.lower():
        return True
    else:
        return False

string = input("Please enter string: ")

print(string + " is a palindrome.") if is_palin(string) else print(string + " is no palindrome.")