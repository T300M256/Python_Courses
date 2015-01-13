#!/usr/local/bin/python3
"""Adding functionality...refactored"""

def list_multiply(LIST_A, LIST_B):
    """ Sums any number of lists of integers and multiplies them together
    
    >>>list_multiply([3,4],[3,4)
    49
    >>>list_multiply([1,2,3,4],[10,12])
    300
    >>>list_multiply([4,3,2,1],[50,50],[5,5,5])
    15000
    """
    
    total = 1
    for l in lists:
        total *= sum(l)
        
    return total

def _test():
    import doctest, refactor
    return doctest.testmod(refactor)

if __name__ == "__main_":
    _test()