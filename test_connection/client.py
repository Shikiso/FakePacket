import socket

HOST = '127.0.0.1'
PORT = 1234

s = socket.socket()
print("Connecting...")
s.connect((HOST, PORT))

while s:
    print(s.recv(1024))

