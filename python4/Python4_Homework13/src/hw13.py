"""
hw13.py: homework thriteen

Write a subclass sstr of the standard str type that implements the "<<" and ">>" methods as a cyclic shifting of the characters in the string.

"""

class sstr(str):
    """
    a subclass of str that has specific shift operator behavior
    """
    
    def __lshift__(self, other):
        if other == 0:
            return self
        return(sstr(self[other:]+self[0:other])) 
    
    def __rshift__(self, other):
        if other == 0:
            return self
        return(sstr(self[(0-other):]+self[0:len(self)-other]))

    
        