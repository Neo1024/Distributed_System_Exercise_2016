#Li Xin
#Student number: 014696390
#xin.li@helsinki.fi

def listy(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(5)
	loop = True
	#create cmsg file or clear the previous content of it
	f = open('cmsg', 'w')
	f.close()

	while loop:
        conn, addr = s.accept()
        msg = conn.recv(1024).decode("utf8")
        f = open('cmsg', 'a')
        f.write(msg + '\n')
        f.close()

        temp = str.split(msg)
        if temp[0] == G:
        	loop = False

	    #try:
	    #except:
	    #    print('Exception :\'(')
	    #    continue

