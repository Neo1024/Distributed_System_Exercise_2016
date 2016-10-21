#Li Xin
#Student number: 014696390
#xin.li@helsinki.fi

def mouse(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
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
        	conn.send(bytes('OUCH'))
        	conn.close()
        	loop = False
