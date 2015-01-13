#!/usr/local/bin/python3
"""this tests formatting skills"""

tup1 = ((1,1),(2,2),(12,13),(4,4),(99,98))

for n1, n2 in tup1:
    p = n1 * n2
    print("{0:4} = {1:2} x {2:2}".format(p, n1, n2))