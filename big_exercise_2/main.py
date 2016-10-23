#Li Xin
#Student number: 014696390
#xin.li@helsinki.fi

import sys
import socket
import random
import threading
import os

import listy

def send_mouse(mouse_port):
	command = 'ssh xgli@' + mouse_node + \
		' python3 /cs/home/xgli/Distributed_System_Exercise_2016/big_exercise_2/mouse.py ' + mouse_port
	os.system(command)

def start_cordy():
	command = 'python3 /cs/home/xgli/Distributed_System_Exercise_2016/big_exercise_2/cordy.py'
	os.system(command)

if __name__ == "__main__":
	#read the usable nodes from the config file
	ukkonodes = open('ukkonodes', 'r').read().split('\n')

	#read the port of listy and mouse
	f = open('port_number', 'r')
	lines = f.read().split('\n')
	temp = lines[0].split()
	listy_port = temp[0]
	temp = lines[1].split()
	mouse_port = temp[0]
	f.close()

	#randomly choose a node to run mouse.py on a new thread
	mouse_node = random.choice(ukkonodes)
	mouse_thread = threading.Thread(target = send_mouse, args = (mouse_port, ))
	mouse_thread.start()

	#start a new thread and run listy.py on the same ukko node as main.py and cordy.py
	host = socket.gethostname()
	listy_thread = threading.Thread(target = listy.listy, args = (host, listy_port))
	listy_thread.start()

	#start a new thread and run cordy.py on the same ukko node as main.py and listy.py
	cordy_thread = threading.Thread(target = start_cordy)
	cordy_thread.start()

	print('program ends!')
