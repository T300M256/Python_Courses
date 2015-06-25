"""
stores inventory of cocunuts
"""

class Coconut(object):
    def __init__(self, ctype, weight):
        self.ctype = ctype
        self.weight = weight

class SouthAsian(Coconut):
    def __init__(self):
        self.ctype = "South Asian"
        self.weight = 3

class MiddleEastern(Coconut):
    def __init__(self):
        self.ctype = "Middle Eastern"
        self.weight = 2.5

class American(Coconut):
    def __init__(self):
        self.ctype = "American"
        self.weight = 3.5


class Inventory(object):
    """
    tracks 'different types of cocunuts from around the world' including weight attributes
    """
    
    def __init__(self):
        self.coconuts = []
    
    def add_coconut(self, c):
        """
        adds a coconut  to the inventory
        """
        # if type is not coconut through AttributeError
        if isinstance(c, Coconut):
            self.coconuts.append(c)
        else:
            raise AttributeError
        
    def total_weight(self):
        """
        provide total weight of coconuts in inventory
        """
        total = 0
        for c in self.coconuts:
            total += c.weight
        return(total)
        