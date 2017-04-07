"""
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:
* Use binary search.
"""

import random
import sys

# Create random, sorted list of len = n
def create_rand_sort_array(n):
    array = random.sample([x for x in range(n * 10)], n)
    array.sort()
    return array

# As per initial task
def simple_search(array, x):
    return x in array

# As per extra task
def bin_search(array, x):
    if array[len(array) // 2] == x:
        return True

    elif array[len(array) // 2] != x and len(array) == 1:
        return False

    else:
        if x > array[len(array) // 2]:
            return bin_search(array[len(array) // 2:], x)
        else:
            return bin_search(array[:len(array) // 2], x)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid number of arguments. Start script with ./<name> <number>")
        sys.exit(1)

    try:
        x = int(sys.argv[1])
    except:
        print("Invalid type of parameter. Start script with ./<name> <number>")
        sys.exit(1)
    
    print("Created array:")
    array = create_rand_sort_array(x)
    print(array)

    print(str(x) + " found in array!") if bin_search(array, x) else print(str(x) + " not found in array.")