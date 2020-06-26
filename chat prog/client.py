import socket
import sys
import time

p=socket.socket()
host=input(str("Please enter the hostname of the server:"))
port=1971
p.connect((host,port))
print("Connected to the server")
while 1:
        incoming_message=p.recv(1024)
        incoming_message=incoming_message.decode()
        print("Server:",incoming_message)
        print("")
        message=input(str(">>"))
        message=message.encode()
        p.send(message)
        print("message has been sent...")
        print("")
      
