import sys
import socket
import time
import random
import select
from _thread import *

def thread_fun(index):
	time.sleep(1)
	print("new thread: " + str(index))

if __name__ == "__main__":
    for i in range(0, 10):
    	start_new_thread(thread_fun, (i,))
    	print("main thread: " + str(i))
    time.sleep(5)