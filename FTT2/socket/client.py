import socket
import sys


def user_input(addres, port):
    user_input = None
    while user_input != "exit":
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((addres, port))
        user_input = input("message: ")
        client.send(user_input.encode())
        response = client.recv(1024)
        print(response.decode())
        client.close()





if len(sys.argv) < 4:
        print("Usage: {} <server IP address> <port>".format(sys.argv[0]))
        sys.exit(1)
server_address = sys.argv[1]
server_port = int(sys.argv[2])
# message = sys.argv[3]

user_input(server_address, server_port)