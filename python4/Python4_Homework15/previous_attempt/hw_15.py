"""
hw_15.py: 'creates a ten-megabyte data file in two different ways, and time each 
method. The first technique should create a memory-mapped file and write the data
by setting one chunk at a time using successively higher indexes. The second
technique should create an empty binary file and repeatedly use the write() method
to write a chunk of data.'
"""

import os
from datetime import datetime
import mmap

FILE1 = "mmap.txt"
FILE2 = "binary.txt"

BIN_CHUNK = b'\0'*1024 # 1 kilobyte

def make_file_1(fn):
    # initiate a file so Windows doesn't have a fit making a map
    f = open(fn, "wb")
    f.write(b'\0') # dump a byte initialize a file
    f.close()
    # now set up the map on the same file
    f = open(fn, "r+b")
    mapf = mmap.mmap(f.fileno(), 1024*1024*10)
    for i in range(10*1024):
        mapf[i:i+1024] = BIN_CHUNK
    mapf.close()
    f.close()

def make_file_2(fn):
    f = open(fn, "wb")
    for i in range(10*1024):
        f.write(BIN_CHUNK)
    f.close()


if __name__ == "__main__":
    
    start1 = datetime.now()
    make_file_1(FILE1)
    end1 = datetime.now()
    delta1 = end1 - start1
    print(FILE1,"is of size", os.path.getsize(FILE1), "generated in", str(delta1.microseconds), 'ms')
 
    start2 = datetime.now()
    make_file_2(FILE2)
    end2 = datetime.now()
    delta2 = end2 - start2
    print(FILE2,"is of size", os.path.getsize(FILE2), "generated in", str(delta2.microseconds), 'ms')

    
    # clean up
    os.unlink(FILE1)
    os.unlink(FILE2)
