# first of all import the socket library
import socket		

# next create a socket object
s = socket.socket()		
print ("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345			

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('localhost', port))		
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(1)	
print ("socket is listening")		

# a forever loop until we interrupt it or
# an error occurs
c,add = s.accept()
if c:
    name=c.recv(1024).decode()
    print(f'connected to {add} , name: {name}')
    c.send(bytes(f'Hello {name} Abhishek here','utf-8'))
print('This is the start of your chat with client')
while True:
    rc=c.recv(1024).decode()
    if(rc == 'exit'):
        print('\033[31mclient exits\033[0m')
        c.close()
        break
    print(f'\033[1;32m{rc}\033[0m')
    msg=input()
    c.send(bytes(msg,'utf-8'))
    if(msg == 'exit'):
        c.close()
        break
    
