"""
this module has an iterator...
"""

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class alphabator:
    def __init__(self, lst):
        self.lst = lst
        self.itemno = 0
        self.nlst = list()
        for i in lst:
            if type(i) == int and i >= 1 and i <= 26:
                # do stuff with the ints
                self.nlst.append(alpha[i-1])
            else:
                self.nlst.append(i)
        
    def __iter__(self):
        return self
    def __next__(self):
        try:
            self.val = self.nlst[self.itemno]
        except IndexError:
            raise StopIteration
        self.itemno += 1
        return self.val