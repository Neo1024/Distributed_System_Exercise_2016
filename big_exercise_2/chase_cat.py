#Li Xin
#Student number: 014696390
#xin.li@helsinki.fi

import sys
import socket

if __name__ == "__main__":
	#parse arguments from the input
	action = sys.argv[1]
	catname = sys.argv[2]

	f = open('listy_location', 'r')
	listynode = f.readline()
	f.close()
	f = open('port_number', 'r')
	listyport = f.readline()
	mouseport = f.readline()
	f.close()

	if (action == 'S'):
		msg = 'SEARCH'
	else:
		msg = 'MEOW'

	listy = socket.socket()
	listy.connect((listynode, listyport))

	s = socket.socket()
	s.setblocking(False)
	host = s.gethost()
	s.connect((host, mouseport))
	s.send(bytes(msg, "utf8"))

	if (action == 'S'):
		time.sleep(12)
	else:
		time.sleep(8)

	response = s.recv(1024).decode("utf8")
	#get the short name of ukko node
	temp = str.split(searchnode, '.')
	ukko = temp[0]
	#send message to listy
	if (response == 'OUCH'):
		listy.send(bytes('G' + ukko + catname , 'utf8'))
	else:
		listy.send(bytes('F' + ukko + catname , 'utf8'))

	s.close()
	listy.close()

		