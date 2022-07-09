from audioop import add
from email import message
import socket
import threading
from config import *


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    print("Server Started\n")
    with conn:
        print(f"Connected to {addr}")
        while True:
            data = conn.recv(1024)
            data = data.decode(FORMAT)
            if data == "BREAK":
                conn.close()
                break
            print(data)
            data = input("Enter You Message: ")
            data = data.encode(FORMAT)
            conn.sendall(data)
            if data.decode(FORMAT) == 'BREAK':
                conn.close()
                print('Connection Close')
                break
            