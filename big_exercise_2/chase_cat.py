#Li Xin
#Student number: 014696390
#xin.li@helsinki.fi

import sys
import socket
import time

if __name__ == "__main__":
	#parse arguments from the input
	action = sys.argv[1]
	catname = sys.argv[2]

	f = open('/cs/home/xgli/Distributed_System_Exercise_2016/big_exercise_2/listy_location', 'r')
	listynode = f.readline()
	f.close()
	f = open('/cs/home/xgli/Distributed_System_Exercise_2016/big_exercise_2/port_number', 'r') 
	temp = f.readline().split()
	listyport = temp[0]
	temp = f.readline().split()
	mouseport = temp[0]
	f.close()

	if (action == 'S'):
		msg = 'SEARCH'
	else:
		msg = 'MEOW'

	s = socket.socket()
	host = socket.gethostname()
	print(host)
	status = s.connect_ex((host, int(mouseport)))

	if (status == 0):
		s.send(bytes(msg, "utf8"))
		response = s.recv(1024).decode("utf8")
		#get the short name of ukko node
		ukko = socket.gethostname()

		#send message to listy
		listy = socket.socket()
		listy.connect((listynode, int(listyport)))
		if (response == 'OUCH'):
			listy.send(bytes('G' + ukko + catname , 'utf8'))
		else:
			listy.send(bytes('F' + ukko + catname , 'utf8'))

		s.close()
		listy.close()

	if (action == 'S'):
		time.sleep(12)
	else:
		time.sleep(8)
	print(status)
