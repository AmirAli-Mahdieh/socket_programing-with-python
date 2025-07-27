import people_class
import socket
my_socket= socket.socket()
client_name= input("enter your name: ")
my_socket.connect(("127.0.0.1", 80))
my_socket.send(client_name.encode())
while True:
    print(my_socket.recv(1024).decode())
    cmd= input()
    my_socket.send(cmd.encode())

