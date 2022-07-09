import socket
import threading
from config import *
from screen_record import capture_now

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((HOST, PORT))

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:

        msg = capture_now()
        msg_length = str(len(msg)).encode(FORMAT)
        msg_length += b' ' * (HEADER - len(msg_length))
        conn.sendall(msg_length)
        conn.sendall(msg.encode(FORMAT))
    
    print("CONNECTION CLOSED")
    conn.close()


def start():
    SERVER.listen()
    print(f"[STARTED] server started listening on {HOST}")
    while True:
        conn, addr = SERVER.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

start()