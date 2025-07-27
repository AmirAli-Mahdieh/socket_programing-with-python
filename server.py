import people_class
import socket
def client_communication(the_client):
    while True:
        main_message=""
        for i in range(len(people_list)):
            main_message+=f"{i+1}- {people_list[i].get_user_name()}"
        main_message+="\nEnter 1: add a person, 2: edit a person place, 3: recive a person, 4: delete a person\n"
        the_client.send(main_message.encode())
        cmd= the_client.recv(1024).decode()
        if int(cmd)==1:
            the_client.send("Enter :name age place".encode())
            name , age, place= the_client.recv(1024).decode().split(" ")
            t_person= people_class.people(name, age, place)
            people_list.append(t_person)
            the_client.send("done!".encode())
        elif int(cmd)==2:
            the_client.send("Enter number of person and its new place:".encode())
            j , new_place=the_client.recv(1024).decode().split(" ")
            if int(j)-1<len(people_list):
                people_list[int(j)-1].set_city(new_place)
                the_client.send("done!".encode())
            else:
                the_client.send("invalid input")
        elif int(cmd)==3:
            the_client.send("Enter number of person to get its info".encode())
            j= the_client.recv(1024).decode()
            if int(j)-1<len(people_list):
                name, age, city= people_list[int(j)-1].get_all()
                the_client.send(f"{name}:{age}, {city}".encode())
        elif int(cmd)==4:
            the_client.send("Enter number of person to delete:".encode())
            j= the_client.recv(1024).decode()
            if int(j)-1<len(people_list) and int(j)>=0:
                people_list.pop(int(j)-1)
                the_client.send("done!".encode())
            else:
                the_client.send("invalid input")
        else:
            break
    the_client.close()
            
people_list=[people_class.people("david", 10, "isfahan"), people_class.people("john", 25, "tehran")]
clients_list=["ali", "amir", "ahmad"]
my_socket= socket.socket()
my_socket.bind(('', 12345))
my_socket.listen(5)
print ("server is listening")
while True:
    the_client, addr= my_socket.accept()
    message= the_client.recv(1024).decode()
    if message=="ali":
        print("connected")
        the_client.send("server: welcome".encode())
        client_communication(the_client)
    else:
        the_client.send("not valid".encode())
        the_client.close()
        


