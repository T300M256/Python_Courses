"""
a classes that will do magic stuff...here we try to protect via __new__
"""

class Centipede(object):
    def __new__(cls):
        cls.legs = []
        cls.stomach = []
        return object.__new__(cls)
        
    def __init__(self):
        self.__dict__['legs'] = []
        self.__dict__['stomach'] = []
        
    
    def __call__(self, *args ):
        for i in args:
            self.stomach.append(i)
            
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
