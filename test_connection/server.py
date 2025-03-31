import socket
import time 

HOST = '127.0.0.1'
PORT = 1234

s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
while conn:
    conn.send(b"Hello")
    time.sleep(5)

s.close()
