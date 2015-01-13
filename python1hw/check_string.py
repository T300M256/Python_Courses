#!/usr/local/bin/python3
"""check the input meets the requirements"""

s = ""
while not s.isupper() or not s.endswith("."):
    s = input("Please enter an upper-case string ending with a period: ")
    if not s.isupper():
       print("Input is not all upper case.")
    elif not s.endswith("."):
        print("Input does not end with a period.")
    else:
        print("Input meets both requirements.")