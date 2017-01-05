#Li Xin
#Student number: 014696390
#xin.li@helsinki.fi

import sys
import socket
import time
import random
import select
from _thread import *

#parse arguments from the input
config_file = sys.argv[1]
line = sys.argv[2]

#read the id and port from the config file
def read_params(config_file):
	ids = []
	ports = []

	with open(config_file, "r") as f:
		for line in f:
			ids.append(line[0: 3])
			ports.append(line[4: 9])
	return(ids, ports)

#send message to a random client
def send_message(sender_id, receiver_port, lamport_clock):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = socket.gethostname()
	try:
		msg = str(sender_id) + " " + str(lamport_clock) + " " + time.strftime("%H:%M:%S")
		s.connect((host, receiver_port))
		s.send(bytes(msg, "utf8"))
	except:
		print('Exception happens when send message to tread ' + str(sender_id))
		return
	finally:
		s.close()

#start a new thread to open an socket for listening and send messages
def client_thread(own_index, ids, ports):
	#own_index indicates the index of current thread in the array ids[] and ports[]
	lamport_clock = 0
	event_count = 0

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = socket.gethostname()
	own_port = ports[own_index]
	own_identifier = ids[own_index]
	s.bind((host, int(own_port)))
	s.listen(5)

	#get a poll object for polling the input requests
	poll = select.poll()
	poll.register(s.fileno(), select.POLLIN)

	f = open("output_" + own_identifier, "w")

	while(event_count < 100):
		#randomly decide whether to send a message or have a local event
		#send a message
		if random.random() > 0.5:
			receiver_id = random.choice(ids)
			#make sure the randomly chosen receiver is not the client itself
			while receiver_id == own_identifier:
				receiver_id = random.choice(ids)
			receiver_port = ports[ids.index(receiver_id)]
			send_message(own_identifier, int(receiver_port), lamport_clock)
			f.write("s " + receiver_id + " " + str(lamport_clock) + "\n")
			lamport_clock = lamport_clock + 1
		#local event
		else:
			#local event
			lamport_clock = lamport_clock + 1
			f.write("l 1\n")
		event_count = event_count + 1

		#listening the port
		for fd, event in poll.poll(1):
			if fd == s.fileno():
				try:
					conn, addr = s.accept()
					msg = str.split(conn.recv(1024).decode("utf8") )
					sender_id = msg[0]
					sender_clock = msg[1]
					timestamp = msg[2]

					if int(sender_clock) > lamport_clock:
						lamport_clock = int(sender_clock) + 1
					else:
						lamport_clock = lamport_clock + 1
					event_count = event_count + 1
					f.write("r " + sender_id + " " + sender_clock + " " + str(lamport_clock) + "\n")
				except:
					print("Exception happened while receiving message")
					continue

	#close the socket, file, and poll object
	poll.unregister(s.fileno())
	f.close()
	s.close()

if __name__ == "__main__":
	ids, ports = read_params(config_file)

	#loop for all the ids and create the socket listening
	for i in range(0, len(ids)):
		print("concrrently start the client thread: " + str(i))
		start_new_thread(client_thread, (i, ids, ports))
	#let the main thread sleep to wait the child client threads so that 
	#the main thread won't exit while any of the client thread is still running
	time.sleep(10)