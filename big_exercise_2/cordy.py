#Li Xin
#Student number: 014696390
#xin.li@helsinki.fi

import os
import math
import threading
import time

def send_cat(action, catname, search_node):
	#connect to remote ukko node by ssh and run chase_cat.py
	command = 'ssh xgli@' + search_node + \
			' python3 /cs/home/xgli/Distributed_System_Exercise_2016/big_exercise_2/chase_cat.py ' + action + catname
	os.system(command)
	

def check_listy(previouse_lines):
	with open('cmsg', 'r') as f:
		i = 0
		for line in f:
			i = i + 1
			#if new line is written, then return it
			if(i > previouse_lines):
				temp = line.split('\n')
				return temp[0]
	return ''

if __name__ == "__main__":
	#read the usable nodes from the config file
	ukkonodes = open('ukkonodes', 'r').read().split('\n')
	print(ukkonodes)
	previouse_lines = 0
	loop = True
	finding_time = 0	#indicate how many times the mouse has been found

	#choose a pivot to devide the ukko nodes into two parts for two cats
	pivot = math.floor(len(ukkonodes)/2)
	catty_nodes = ukkonodes[0:pivot]
	jazzy_nodes = ukkonodes[pivot:len(ukkonodes) - 1]

	#send catty to search each node
	for node in catty_nodes:
		chase_thread = threaing.Thread(target = send_cat, args = ('S', 'Catty', node))
		chase_thread.start()

	#send jazzy to search each node
	for node in jazzy_nodes:
		chase_thread = threaing.Thread(target = send_cat, args = ('S', 'Jazzy', node))
		chase_thread.start()

	#check cmsg file every 2 seconds
	while loop:
		msg = check_listy(previouse_lines)
		if (msg != ''):
			previouse_lines = previouse_lines + 1
			temp = msg.split()
			#if message of find the mouse
			if (temp[0] == 'F'):
				finding_time = finding_time + 1
				#if both cats have found the mouse
				if (finding_time >= 2):
					node = temp[1] + '.hpc.cs.helsinki.fi'
					chase_thread = threaing.Thread(target = send_cat, args = ('A', 'Jazzy', node))
					chase_thread.start()
				#if the first time of finding
				if (finding_time == 1):
					node = temp[1] + '.hpc.cs.helsinki.fi'
					if (temp[2] == 'Catty'):
						chase_thread = threaing.Thread(target = send_cat, args = ('A', 'Jazzy', node))
						chase_thread.start()
					else:
						chase_thread = threaing.Thread(target = send_cat, args = ('A', 'Catty', node))
						chase_thread.start()
			#if message of catching the mouse
			else:
				loop = False

		#check cmsg file every 2 seconds
		time.sleep()