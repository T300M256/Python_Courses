"""
control.py Creates queues, starts output and worker processes,
           and pushes input into th einput queue
"""

from multiprocessing import Queue, JoinableQueue
from output import OutThread
from worker import WorkerThread
import random

if __name__ == '__main__':
    WORKERS = 10
    albet = "abcdefghijklmnopqrstuvwxyz"
    
    inq = JoinableQueue(maxsize=int(WORKERS*1.5))
    outq = Queue(maxsize=int(WORKERS*1.5))
    
    ot = OutThread(WORKERS, outq)
    ot.start()
    
    for i in range(WORKERS):
        w = WorkerThread(inq, outq)
        w.start()
    #instring = input("Words of wisdom: ")
    # random string of 1000 characters
    randseq = [random.randint(0,25) for i in range(1000)]
    genstring = ""
    for x in randseq:
        genstring += albet[x]
    # feed the process pool with wok units
    for work in enumerate(genstring):
        inq.put(work)
    # terminate the process pools
    for i in range(WORKERS):
        inq.put(None)
    inq.join()
    print("Control process terminating")