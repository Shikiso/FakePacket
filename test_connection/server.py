import socket
import time 

HOST = '127.0.0.1'
PORT = 1234

s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)
print("Listening for connection...")
while 1:
    conn, addr = s.accept()
    print("Connection made!\n", addr)
    conn.close()

s.close()
