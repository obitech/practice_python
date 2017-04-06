"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

"""
def get_int(text="Please enter integer: "):
    while True:
        try:
            num = int(input(text))
            break
        except:
            print("Invalid input.")

    return num


while True:
    n = get_int("How many Fibonacci numbers should be displayed? ")

    if n >= 0:
        break

    print("Input must be positive!")
"""

def fib(n):
    a, b, temp = 1, 0, 0
    arr = [0]

    for i in range(1, n + 1):
        arr.append(a)
        temp = a
        a = a + b
        b = temp

    return arr


# Test cases
def test_basic():
    assert fib(0) == [0]
    assert fib(1) == [0, 1]
    assert fib(2) == [0, 1, 1]
    assert fib(5) == [0, 1, 1, 2, 3, 5]
    assert fib(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert fib(14) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]