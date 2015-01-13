#!/usr/local/bin/python3
""" Named and generic exceptino handling"""

def add(a,b):
   """Print the result of adding a set and a value"""
   try:
       a.add(b)
       print(a)
   except AttributeError:
       print("({0}) is not a set object".format(a))
   except TypeError:
       print("({0}) is not a hashable object".format(a))
   except:
       print("This is a generic exception")
       raise

class Test(object):
    """ Just a simple test class """
    
    def add(self, a):
        """ Demonsrates how you need to be able to handle unpredicatble results. """
        d = {'python':'fun'}
        return d[a]

if __name__ == "__main__":
    s = set((1,2,3))
    add(s, 4)
    add(1, 4)
    add(s, [4,5,6])
    t = Test()
    add(t, 1)
       