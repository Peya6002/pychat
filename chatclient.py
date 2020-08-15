import socket
import sys
import time
from win10toast import ToastNotifier


toaster = ToastNotifier()


s = socket.socket()
host = input(str("please enter the hostname of the server"))
port = 8080
s.connect((host,port))
print("COnnected to the chat")
while 1:
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print(":",incoming_message)
    toaster.show_toast("chat", incoming_message, threaded=True,
                   icon_path=None, duration=3)  
    print("")
    message= input(str(">>>"))
    message = message.encode()
    s.send(message)
    print("sent")
    print("")
