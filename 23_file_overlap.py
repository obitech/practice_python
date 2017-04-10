"""
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
(primenumbers.txt) has a list of all prime numbers under 1000, and (happynumbers.txt) has a list of happy numbers up to 1000.
"""

with open("primenumbers.txt", 'r') as prime_file:
    prime_list = [int(line.strip()) for line in prime_file]

with open("happynumbers.txt", 'r') as happy_file:
    happy_list = [int(line.strip()) for line in happy_file]

overlap = sorted(list(set(prime_list) & set(happy_list)))

print(overlap)