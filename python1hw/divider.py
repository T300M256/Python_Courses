#!/usr/local/bin/python3
"""this test exception handling"""

print("Divide 10 by an int")

while True:
    try:
        inp = input("Provide an integer: ")
        if not inp:
            break
        d = int(inp)
        print(10/d)
    except ValueError:
        print("Your input must be an integer")
    except ZeroDivisionError:
        print("Your input must not be zero (i.e., 0)")

        