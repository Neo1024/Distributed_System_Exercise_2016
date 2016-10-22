#Li Xin
#Student number: 014696390
#xin.li@helsinki.fi

import sys
import socket
import random
import threading
import os

import mouse

def send_mouse():
	command = 'ssh xgli@' + mouse_node + \
		' python3 /cs/home/xgli/Distributed_System_Exercise_2016/big_exercise_2/mouse.py ' + mouse_port
	os.system(command)

if __name__ == "__main__":
	#read the usable nodes from the config file
	ukkonodes = open('ukkonodes', 'r').read().split('\n')
	print(ukkonodes)

	#read the port of listy and mouse
	f = open('port_number', 'r')
	lines = f.read().split('\n')
	temp = lines[0].split()
	listy_port = temp[1]
	temp = lines[1].split()
	mouse_port = temp[1]
	f.close()

	#randomly choose a node to run mouse.py on a new thread
	mouse_node = random.choice(ukkonodes)
	#mouse.mouse(mouse_node, mouse_port)
	mouse_thread = threading.Thread(target = mouse.mouse, args = (mouse_node, mouse_port))


	print('program ends!')
