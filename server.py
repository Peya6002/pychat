import socket
import sys
import time
from win10toast import ToastNotifier

toaster = ToastNotifier()

s = socket.socket()
host = socket.gethostname()
print("server will start on host: ",host)
port = 8080
s.bind((host,port))
print("")
print ("server done binding to host")
print("")
print("server is waiting for clients")
print("")
s.listen(1)
conn,addr = s.accept()
print(addr,"has connected to the server")
print("")
while 1: 
    message= input(str(">>>"))
    message = message.encode()
    conn.send(message)
    print("sent")
    print("")
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print(":",incoming_message)
    toaster.show_toast("chat", incoming_message, threaded=True,
                   icon_path=None, duration=3)  
    print("")




