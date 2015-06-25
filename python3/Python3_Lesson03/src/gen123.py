"""
gen123.py generates sequence from a base list, repearting
each element on more than than the last
"""

def gen123(m):
    n = 0
    for item in m:
        n += 1
        for i in range(n):
            yield item