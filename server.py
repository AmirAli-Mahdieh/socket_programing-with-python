import people_class
import socket
def client_communication(the_client):
    while True:
        for i in range(people_list.count()):
            my_socket.send(f"{i+1}- {people_list[i]}")
        my_socket.send("Enter 1: add a person, 2: edit a person place, 3: recive a person, 4: delete a person\n".encode())
        cmd= the_client.recv(1024).encode()
        if cmd==1:
            my_socket.send("Enter :name age place")
            name , age, place= my_socket.recv(1024).decode().splite(" ")
            t_person= people_class.people(name, age, place)
            people_list.append(t_person)
        elif cmd==2:
            my_socket.send("Enter number of person and its new place:")
            j , new_place=my_socket.recv(1024).decode().splite(" ")
            if j-1<people_list.count():
                people_list[j-1].set_city(new_place)
        elif cmd==3:
            my_socket.send("Enter number of person to get its info")
            j= my_socket.recv(1024).decode()
            if j-1<people_list.count():
                name, age, city= people_list[j-1].get_all()
                my_socket.send("{name}:{age}, {city}".encode())
        elif cmd==4:
            my_socket.send("Enter number of person to delete:")
            j= my_socket.recv(1024).decode()
            if j-1<people_list.count() and j>=0:
                people_list.pop(j-1)
        else:
            break
    the_client.close()
            
people_list=[]
clients_list=["ali", "amir", "ahmad"]
my_socket= socket.socket()
my_socket.bind(('', 80))
my_socket.listen(5)
print ("server is listening")
while True:
    the_client, addr= my_socket.accept()
    message= the_client.recv(1024).decode()
    if message=="ali":
        the_client.send("welcome".encode())
    else:
        the_client.send("not valid".encode())
        the_client.close()
        


