#!/usr/bin/python3

import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 445

serverSocket.bind((host, port))

serverSocket.listen(3)

while True:
    clientSocket, address = serverSocket.accept()

    print(f"Recieved connection from {address}")

    message = "Hello from server, its abin"
    clientSocket.send(message.encode('ascii'))

    clientSocket.close()