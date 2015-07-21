"""
composablle.py: defines a composable function class.
...extending to allow to be raise to postive integer powers.
"""
import types

class Composable:
    def __init__(self, f):
        "Store reference to the proxied function."
        self.func = f
    def __call__(self, *args, **kwargs):
        "Proxy the function, passing all arguments through."
        return self.func(*args, **kwargs)
    
    def __mul__(self, other):
        "Return the composition of proxied and another function"
        if type(other) is Composable:
            def anon(x):
                return self.func(other.func(x))
            return Composable(anon)
        elif type(other) is types.FunctionType:
            def anon(x):
                return self.func(other(x))
            return Composable(anon)
        raise TypeError("Illegal operands for multiplication")
    
    def __pow__(self, power):
        "Return the composition of proxied function and itself..."
        if type(power) != int:
            raise TypeError("power must be a positive integer")
        elif power <= 0:
            raise ValueError("power must be a positive integer")
        anon = self
        for e in range(power-1):
            anon = self * anon
        return anon
    
    def oldpow(self, power):
        "raise the object by a positve integer"
        if type(power) != int:
            raise TypeError("power must be a positive integer")
        elif power <= 0:
            raise ValueError("power must be a positive integer")
        def anon(x):
            return self.func(x**power)
        return(anon)
    
    def __repr__(self):
        return "<Composable function {0} at 0x{1:X}>".format(self.func.__name__, id(self))