"""
find_regex.py: returns the location of the phrase 'Regular Expressions' in a given text
"""

import re

TEXT = 'In the 1950s, mathematician Stephen Cole Kleene described automata theory and formal language theory in a set of models using a notation called "regular sets" as a method to do pattern matching. Active usage of this system, called Regular Expressions, started in the 1960s and continued under such pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry Spencer.'

s = re.search("(Regular Expressions)",TEXT)

def start():
    return s.start()

def end():
    return s.end()
    
    
