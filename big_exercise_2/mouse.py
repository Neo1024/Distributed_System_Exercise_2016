#Li Xin
#Student number: 014696390
#xin.li@helsinki.fi

import socket
import sys
import time

if __name__ == "__main__":
	#get port from the input
	port = sys.argv[1]

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = socket.gethostname()
	s.bind((host, int(port)))
	s.listen(5)
	loop = True

	while loop:
		conn, addr = s.accept()
		msg = conn.recv(1024).decode("utf8")

		if msg == 'SEARCH':
			conn.send(bytes('WOO', 'utf-8'))
			conn.close()
		else:
			time.sleep(6)
			conn.send(bytes('OUCH', 'utf-8'))
			conn.close()
			loop = False
