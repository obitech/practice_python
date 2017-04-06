"""
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.
"""

import sys

def reverse_string(string):
    return ' '.join(string.split(" ")[::-1])

if len(sys.argv) != 2:
    print("Invalid number of arguments. Run script with: ./<name> <string>")
    exit()

old = sys.argv[1]

print("Original string:\n" + old)
print("\nReversed string:\n" + reverse_string(old))