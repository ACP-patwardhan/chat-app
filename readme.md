Simple python based chat app. allows 2 remote machines to text.\
start server.py on the host machine:
```python
python3 server.py
```
the server will wait for getting connection request from 1 client.\
on client machine run:\n
```python
python3 client.py
```
enter host ip address, if you're running server on same machine you can enter localhost\
enter port number for the host. it is 12345 for the server.\
enter your name.

Client chats first. then the server follows.\
if anyone types exit on thier turn, the connection closes and both apps stop