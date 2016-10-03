
import socket
import time
from _thread import *

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=12345

s.bind((host,port))

s.listen(10)


def clientthread(conn, addr):
    for i in range(0,5):
        reply = 'Hello! '+time.strftime("%H:%M:%S")
        conn.send(bytes(reply, 'utf-8'))
        time.sleep(3)

    conn.close()
    print('Connection from '+str(addr)+' closed.')



while True:
    try:
        conn, addr = s.accept()
    except:
        print ('Exception :\'(')
        continue

    print('Got connection from ',addr)


    # Here we start a new thread for each new connection. 
    # The thread executes clientthread() and exits when it's done.
    start_new_thread(clientthread, (conn, addr))

s.close()