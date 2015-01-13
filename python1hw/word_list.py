#!/usr/local/bin/python3
"""this is the wordlist program"""

s = input("Enter a string: ")
lstup = []
lstlow = []

for word in s.strip().split():
    if word.islower():
        lstlow.append(word)
    else:
        lstup.append(word)

for word in lstup + lstlow:
    print(word)