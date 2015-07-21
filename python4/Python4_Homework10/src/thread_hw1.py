"""
determine wheter os.chdir will change the current directory among threads
"""

import threading
import os
import time

main_cwd = os.getcwd()

def run(wd, name):
	"""chdir to specific working dir"""
	os.chdir(wd)
	print(name, "starts working in", os.getcwd())
	time.sleep(10)
	print(name, "  ends working in", os.getcwd())

t1 = threading.Thread(target=run, args=(main_cwd, "Thread_One"))
t1.start()
t2 = threading.Thread(target=run, args=("\\", "Thread_Two")) # only varies is main_cwd is not root dir
t2.start()
#time.sleep(1)
t3 = threading.Thread(target=run, args=("C:\\Program Files", "Thread_Three")) # only varies is main_cwd is not root dir
t3.start()