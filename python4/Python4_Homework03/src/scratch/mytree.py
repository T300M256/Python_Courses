'''
Tree with non-functioning find method...extending from str
'''

class Tree(str):
    
    def __init__(self, key, data=''):
        "Create a new Tree object with empty L & R subtrees"
        str.__init__(self)
        self.key = key
        self.data = data
        self.left = self.right = None
    
    def insert(self, key, data=''):
        "Insert a new lement in the tree in the correct position"
        if key < self.key:
            #print("Here key is type",type(key))
            #print("Here self.key is type",type(self.key))
            if self.left:
                self.left.insert(key)
            else:
                #print("insert is create a new element",key)
                self.left = Tree(key,data)
        elif key > self.key:
            if self.right:
                self.right.insert(key)
            else:
                #print("insert is create a new element",key)
                self.right = Tree(key,data)
        else:
            raise ValueError("Attempt to insert duplicate value")
    def walk(self):
        "Generate the keys from the tree in sorted order"
        if self.left:
            for n in self.left.walk():
                #print("n is of type", type(n))
                yield n
        #print("self is of type", type(self),"and its data is",self.data)
        
        yield self.key
        if self.right:
            for n in self.right.walk():
                #print("n is of type", type(n))
                yield n
    def find(self, key):
        #return(key)
        for i in self.walk():
            print("comparing",i,"to",key)
            if i == key:
                print("i is type ", type(i))
                print("key is type ", type(key))
                return(i.data)

if __name__ == '__main__':
    t = Tree("D")
    for c in "BJQKFAC":
        t.insert(c)

    print(list(t.walk()))