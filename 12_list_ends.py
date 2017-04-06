"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
"""

def first_last_list(arr):
    try: 
        return [arr[0], arr[len(arr) - 1]]
    except:
        return []


# Pytest: run with ./py.test -v 12_list_ends.py
def test1():
    assert first_last_list([5, 10, 15, 20, 25]) == [5, 25]
    assert first_last_list([23, 5, 15, 66, 20123]) == [23, 20123]
    assert first_last_list([]) == []
    assert first_last_list(['first', 'last']) == ['first', 'last']
