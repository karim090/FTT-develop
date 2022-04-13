import os
import socket

PORT = 8081

def server():
    server = socket.socket()
    server.bind(("", PORT))
    server.listen(0)
    print("Server listening on port: {}".format(PORT))

    counter = 0
    while True:
        client, addr = server.accept()
        print("Accepted connection from: {}".format(addr))
        data = client.recv(1024).decode()
        counter += 1
        print("data: {}".format(data))
        client.send("Recived {}.".format(counter).encode())
        client.close()


server()