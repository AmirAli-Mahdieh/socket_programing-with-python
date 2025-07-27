import people_class
import socket
import threading
from _thread import start_new_thread
lock=threading.Lock()
def client_communication(the_client, the_name):
    print(the_name, " connected")
    the_client.send("server: welcome".encode())
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
            lock.acquire()
            people_list.append(t_person)
            lock.release()
            the_client.send("done!".encode())
            print(the_name,": adde new member:",name)
        elif int(cmd)==2:
            the_client.send("Enter number of person and its new place:".encode())
            j , new_place=the_client.recv(1024).decode().split(" ")
            if int(j)-1<len(people_list):
                lock.acquire()
                people_list[int(j)-1].set_city(new_place)
                lock.release()
                the_client.send("done!".encode())
                print(the_name,": changed info of ", people_list[int(j)-1].get_user_name())
            else:
                the_client.send("invalid input")
        elif int(cmd)==3:
            the_client.send("Enter number of person to get its info".encode())
            j= the_client.recv(1024).decode()
            if int(j)-1<len(people_list):
                lock.acquire()
                name, age, city= people_list[int(j)-1].get_all()
                lock.release()
                the_client.send(f"{name}:{age}, {city}".encode())
                print(the_name,f": got {name} infos")
        elif int(cmd)==4:
            the_client.send("Enter number of person to delete:".encode())
            j= the_client.recv(1024).decode()
            lock.acquire()
            if int(j)-1<len(people_list) and int(j)>=0:
                print(the_name,f": deleted {people_list[int(j)-1].get_user_name()}")
                people_list.pop(int(j)-1)
                lock.release()
                the_client.send("done!".encode())
                
            else:
                the_client.send("invalid input")
        else:
            break
    the_client.close()

def sign_in(name):
    text_addres ="C:/c++projects/ejigma/techstack_backend/vaild_clients.txt"
    with open(text_addres, 'r', encoding="utf-8") as file:
        for i in file:
            if i.strip()==name:
                return True
        return False

people_list=[people_class.people("david", 10, "isfahan"), people_class.people("john", 25, "tehran")]
clients_list=["ali", "amir", "ahmad"]
my_socket= socket.socket()
my_socket.bind(('', 12345))
my_socket.listen(5)
print ("server is listening")
while True:
    the_client, addr= my_socket.accept()
    the_name= the_client.recv(1024).decode()
    if sign_in(the_name):
        start_new_thread(client_communication, (the_client, the_name))
    else:
        the_client.send("not valid".encode())
        the_client.close()
        


