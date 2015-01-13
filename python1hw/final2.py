#!/usr/local/bin/python3
"""this is the final program that does stuff with a file of text and makes a histogram"""

import sys
import math

DEFAULT_SCALE = 20 # this is the default scale for each row of the chart

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
    
# get some characteristics of the data
longest = max(len_count.keys())
most_freq = max(len_count.values())

# convert into graph characteristics
height = math.ceil(most_freq/100)*100
width = math.ceil(longest/10)*10

# determine how many row to print in the chart
scale = DEFAULT_SCALE
num_rows = round(height/scale)

# print chart
for r in range(num_rows,0,-1):
    row_val = r * scale
    # prepare the y-axis and labels
    if row_val % 100 != 0:
        row = "{0:6}   |".format('')
    else:
        row = "{0:6} - |".format(row_val)
    # prepare the histogram content for each row
    histo = ""
    for k,v in sorted(len_count.items()):
        if v > row_val-(scale/2):
            histo = histo + "***"
        else:
            histo = histo + "   "
    row = row + histo
    print(row)

# create x-axis and labels
print("     0 - +"+"-+-"*(width-1))
xlabel = ""
for n in range(1,width+1):
    xlabel = xlabel + "%3s" % (n)
print(" "*9+xlabel)

