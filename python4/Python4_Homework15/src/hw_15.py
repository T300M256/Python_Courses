"""
hw_15.py: 'creates a ten-megabyte data file in two different ways, and time each 
method. The first technique should create a memory-mapped file and write the data
by setting one chunk at a time using successively higher indexes. The second
technique should create an empty binary file and repeatedly use the write() method
to write a chunk of data.'
"""

import os
import timeit
import mmap
import math

FILE1 = "mmap.txt"
FILE2 = "binary.txt"

BIN_CHUNK = b'\0'*1024 # 1 kilobyte

def make_file_map(fn, chunk_size):
    # initiate a file so Windows doesn't have a fit making a map
    f = open(fn, "wb")
    f.write(b'\0') # dump a byte initialize a file
    f.close()
    # now set up the map on the same file
    f = open(fn, "r+b")
    chunks = math.ceil(1024*1024*10 / chunk_size)
    mapf = mmap.mmap(f.fileno(), chunks*chunk_size)
    i = 0 # index for last byte written
    while i < 1024*1024*10:
        mapf[i:i+chunk_size] = b"\0"*chunk_size
        i += chunk_size
    mapf.close()
    f.close()

def make_file(fn, chunk_size):
    f = open(fn, "wb")
    #for i in range(10*1024):
    while os.path.getsize(fn)< 1024*1024*10:
        f.write(b'\0'*chunk_size)
    f.close()


if __name__ == "__main__":
    
    for chunk_size in 1000, 10000, 100000, 1000000:
        #print(timeit.timeit("make_file(\"{0}\", {1})".format(FILE2, chunk_size), "from __main__ import make_file", number=1))
        delta1 = timeit.timeit("make_file_map(\"{0}\", {1})".format(FILE1, chunk_size), "from __main__ import make_file_map", number=1)
        delta2 = timeit.timeit("make_file(\"{0}\", {1})".format(FILE2, chunk_size), "from __main__ import make_file", number=1)
        print(FILE1,"is of size", os.path.getsize(FILE1), "generated in", delta1, "using chunk size of", chunk_size)
        print(FILE2,"is of size", os.path.getsize(FILE2), "generated in", delta2, "using chunk size of", chunk_size)
       
    # clean up
    os.unlink(FILE1)
    os.unlink(FILE2)
