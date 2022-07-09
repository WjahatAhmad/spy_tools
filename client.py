import socket 
from config import *

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall(b'Hello, World!')
    while True:
        data = input("Enter You Message: ")
        if data == "BREAK":
            data = data.encode(FORMAT)
            s.sendall(data)
            print("Ending The Connection!")
            break
        data = data.encode(FORMAT)
        s.sendall(data)
        data = s.recv(1024)
        data = data.decode(FORMAT)
        if data == 'BREAK':
            print('Connection Closed')
            break
        else:
            print(data)