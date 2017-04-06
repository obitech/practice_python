"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:
* If the number is a multiple of 4, print out a different message.
* Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
  If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

def get_num():
    while True:
        try:
            num = int(input("Please enter integer: "))
            break
        except:
            pass

    return num

num = get_num()

# Normal:
# print(str(num) + " is odd.") if num % 2 != 0 else print(str(num) + " is even.")

# Extra 1:
if num == 4:
    print("Nice number!")

elif num % 2 == 0:
    print(str(num) + " is even.")

else:
    print(str(num) + " is odd.")

# Extra 2:
num = get_num()
check = get_num()

try:
    div = num % check
except:
    print("Division by 0 not possible.")
    exit()

print(str(num) + " divided by " + str(check) + " divides evenly.") if div == 0 else print(str(num) + " divided by " + str(check) + " divides oddly.") 