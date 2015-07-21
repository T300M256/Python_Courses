"""
control.py Creates queues, starts output and worker threads,
           and pushes input into th einput queue
"""

from queue import Queue
from output import OutThread
from worker import WorkerThread
import random
from datetime import datetime

start = datetime.now()

WORKERS = 10
albet = "abcdefghijklmnopqrstuvwxyz"



inq = Queue(maxsize=int(WORKERS*1.5))
outq = Queue(maxsize=int(WORKERS*1.5))

ot = OutThread(WORKERS, outq)
ot.start()

for i in range(WORKERS):
    w = WorkerThread(inq, outq)
    w.start()
# random string of 1000 characters
randseq = [random.randint(0,25) for i in range(1000)]
genstring = ""
for x in randseq:
    genstring += albet[x]
for work in enumerate(genstring):
    inq.put(work)
for i in range(WORKERS):
    inq.put(None)
inq.join()
print("Control thread terminating")
print("runtime (in seconds):",(datetime.now()-start).total_seconds())