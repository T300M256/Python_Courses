#!/usr/local/bin/python3
"""this is the final program that does stuff with a file of text"""

import sys


# get the arg
try:
    filename = str(sys.argv[1])
except IndexError:
    print("USAGE: final2.py file")
    sys.exit()

# open the file
try:
    f = open(filename, 'r')
except FileNotFoundError:
    print("Could not open the file",filename,"for reading")
    sys.exit()

# read the file
text = f.read()

f.close()

# process the words
words = text.split()
#print('1: ',words[0])
len_count = {}
for w in words:
    l = 0
    if w.isalpha():
        l = len(w)
    else:
        for c in w:
            if c.isalpha():
                l += 1

    if l <= 0:
        continue
    elif l in len_count:
        len_count[l] += 1
    else:
        len_count[l] = 1

# print output
print("Length Count")
for l,c in len_count.items():
    print(l,c)