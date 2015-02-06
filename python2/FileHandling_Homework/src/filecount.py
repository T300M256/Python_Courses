import glob
import os

def count_by_ext(path="."):
    """count the number of files for each extension in directory"""
    flst = glob.glob(path+"*.*")
    count = {}
    for fn in flst:
        if os.path.isdir(fn):
            continue
        name, e = os.path.splitext(fn)
        #if count[e]:
        if count.get(e):
            count[e] += 1
        else:
            count[e] = 1
    print(count)
    return count
        