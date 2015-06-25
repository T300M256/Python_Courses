"""
wiretimes.py - prints the timestamp for the packets in wireshark file
"""

import os,struct
filename = r"v:\workspace\Python3_Homework08\src\wireshark.bin"

fsize = os.stat(filename).st_size
f = open(filename, "rb")
#read through the global header bytes
s = f.read(24)
bytecount = 24
#read through packet data and print the first entry

while bytecount < fsize:    
    ts_sec, = struct.unpack("=l", f.read(4))
    ts_usec, = struct.unpack("=l", f.read(4))
    incl_len, = struct.unpack("=l", f.read(4))
    orig_len, = struct.unpack("=l", f.read(4))
    bytecount += 16
    # fast forward through packet
    f.read(orig_len)
    bytecount += orig_len
    print(str(ts_sec)+"."+str(ts_usec))

f.close()


