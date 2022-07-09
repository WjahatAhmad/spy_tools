import cv2
import socket
from traceback import print_tb 
from config import *
import pyautogui

SCREEN_SIZE = tuple(pyautogui.size())
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (SCREEN_SIZE))



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    # client.sendall(b'Hello, World!')
    while True:
        msg_length = int(client.recv(HEADER).decode(FORMAT))
        if msg_length:
            msg = client.recv(msg_length).decode(FORMAT)
            if msg == BREAK_CONNECTION:
                connected = False
            out.write(msg)