class Furnishings(object):
    def __init__(self, room):
        self.room = room

class Sofa(Furnishings):
    pass

class Bookshelf(Furnishings):
    pass

class Bed(Furnishings):
    pass

class Table(Furnishings):
    pass

def map_the_home(home):
    mp = {}
    for i in home:
        if i.room in mp.keys():
            mp[i.room].append(i)
        else:
            mp[i.room] = [i]
        #mp[i.room] = i
    return(mp)

def counter(home):
    result = ""
    fcount = {"Beds":0, "Bookshelves":0, "Sofas":0, "Tables":0}
    for i in home:
        if type(i) == Bed:
            fcount["Beds"] += 1
        elif type(i) == Bookshelf:
            fcount["Bookshelves"] += 1
        elif type(i) == Sofa:
            fcount["Sofas"] += 1
        elif type(i) == Table:
            fcount["Tables"] += 1
        
    for k in sorted(fcount.keys()):
        result += k+": "+str(fcount[k])+"\n"
    return result