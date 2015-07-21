class Tree(str):
    def __init__(self, *args, **kw):
        #str.__init__(self, *args, **kw)
        str.__init__(self)
        self.sets = 0
        self.value = args[0]
    def __setitem__(self, value):
        self.sets += 1
        str.__setitem__(self, value)
        
class myString (str):
    def __init__ (self, value, data=''):
        self.value = value
        self.data = data
        
class myChar (chr):
    def __init__ (self, value, data=''):
        self.value = value
        self.data = data