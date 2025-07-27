import people_class
import socket
my_socket= socket.socket()
client_name= input("enter your name: ")
try:
    my_socket.connect(("127.0.0.1", 12345))
    my_socket.send(client_name.encode())
    print("name sent")
    print(my_socket.recv(1024).decode())
except:
    print("problem")
while True:
    print(my_socket.recv(1024).decode())
    cmd= input()
    my_socket.send(cmd.encode())
    print(my_socket.recv(1024).decode())
    cmd= input()
    my_socket.send(cmd.encode())
    print(my_socket.recv(1024).decode())