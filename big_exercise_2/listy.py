#Li Xin
#Student number: 014696390
#xin.li@helsinki.fi

import socket
import traceback

def listy(host, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((host, int(port)))
		s.listen(5)
		loop = True
	except Exception:
		print(traceback.print_exc()) 

	#create cmsg file or clear the previous content of it
	f = open('cmsg', 'w')
	f.close()

	while loop:
		try:
			conn, addr = s.accept()
			msg = conn.recv(1024).decode("utf8")
			f = open('cmsg', 'a')
			f.write(msg + '\n')
		except Exception:
			print(traceback.print_exc())
		finally:
			f.close()
			s.close()

		if msg[0] == 'G':
			s.close()
			loop = False