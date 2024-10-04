#!/usr/bin/python3
"""
Purpose: Demonstration of Palindrome check

    palindrome strings
        dad
        mom

Algorithms:
-----------
Step 1: Take the string in run-time and store in a variable


"""


# enter string to check

enter_string = input(" Enter string to check palidrome: ")

print(enter_string[::-1])

if enter_string == enter_string[::-1]:
    print(f"'{enter_string}' is a palindrome")
else:
    print(f"'{enter_string}' is not a palindrome")


