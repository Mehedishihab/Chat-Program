import socket
import sys
import time


p=socket.socket()
host=socket.gethostname()
print("server will start on host :",host)
port=1971
p.bind((host,port))
print("")
print("server done binding to host and port successfully")
print("")
p.listen(1)
conn,addr=p.accept()
print(addr,"Has connected to the server and is now online...")
print("")
while 1:
        message=input(str(">>"))
        message=message.encode()
        conn.send(message)
        print("message has been sent...")
        print("")
        incoming_message=conn.recv(1024)
        incoming_message=incoming_message.decode()
        print("Client:",incoming_message)
        print("")

