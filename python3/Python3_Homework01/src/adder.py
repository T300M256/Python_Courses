"""
Adds to int objects together
"""

def add(a,b):
    if type(a) != int:
        raise TypeError
        #return
    if type(b) != int:
        raise TypeError
        #return
    return(a+b)