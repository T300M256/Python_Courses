class myDict(dict):
    def __init__(self, value):
        self.value = value

    def __getitem__(self, key):
        try:
            #return self[key]
            return super(myDict, self).__getitem__(key)
        except KeyError:
            return self.value

    
        