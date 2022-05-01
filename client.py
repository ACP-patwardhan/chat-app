# Import socket module
import socket
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
ip =input('\nenter ipv4 address of host\n')
port = int(input('\nenter port\n'))             
name = input('\nEnter your name to connect with abhishek\'s chat\n')
# connect to the server on local computer
s.connect((ip, port))
s.send(bytes(name,'utf-8'))
# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
while True:
    msg=input()
    s.send(bytes(msg,'utf-8'))
    if(msg=='exit'):
        s.close()
        break
    rc=s.recv(1024).decode()
    if(rc=='exit'):
        print('\033[31mserver exits\033[0m')
        s.close()
        break
    print(f'\033[1;32m{rc}\033[0m')