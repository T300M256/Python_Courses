"""
a classes that will do magic stuff...here we try to protect via __new__
"""

class Centipede(object):
    def __new__(cls):
        cls.legs = []
        cls.stomach = []
        return object.__new__(cls)
        
    def __init__(self):
        pass
    
    def __call__(self, *args, **kwargs):
        for i in args:
            self.stomach.append(i)
        # not sure if this is best for setting leg valuse
        #for k,v in kwargs:
        #    self.legs[k] = v
            
    def __str__(self):
        return ",".join(self.stomach)
        
    def __repr__(self):
        return ",".join(self.legs)
    
    def __setattr__(self, key, value):
        #print("ATTR: setting attribute {0!r} to {1!r}".format(key, value))
        if key != 'legs' and key != 'stomach':
            self.legs.append(key)
        if key == 'legs' or key == 'stomach':
            raise AttributeError
        self.__dict__[key] = value
