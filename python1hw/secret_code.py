#!/usr/local/bin/python3
"""tests use of built-in function"""

text = input("Message: ")
n = ""
for c in reversed(text):
    n = n + chr(ord(c)+1)
print(n)