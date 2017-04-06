"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
"""

import random

a = [random.randint(0, 10) for x in range(50)]
b = list(set(a))

print("Initial list: " + str(a))
print("Without duplicates: " + str(b))