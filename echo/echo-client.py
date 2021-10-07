#!/home/saais/conda/envs/pynet/bin/python3

import socket

HOST = "localhost"
PORT = 1234

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    s.send(input().encode())
    data = s.recv(1024)
    print("Received ", data.decode())
    if data.decode() == "stop":
        break
s.close()