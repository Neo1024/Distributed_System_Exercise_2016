
import socket
import time

s = socket.socket()

host = socket.gethostname()
port = 12345

s.connect((host,port))

while True:
    buf = s.recv(1024)
    
    # Break out if we received nothing. 
    # This happens e.g. when the server closes the remote socket.
    if not buf:
        break

    print(buf)

s.close()