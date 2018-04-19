import hashlib
import socket
from tkinter import *
mess=""
message=""

def server():
    mess=E1.get()
    s.send(mess)

def fromserver():
	mess=E1.get()
    message=s.recv(4096)
    print(message)
    mparts=message.split("#")
    print(mparts[0]+mparts[1])
    newsha=hashlib.sha1(mess.encode())
    if newsha.hexdigest()!=mparts[1]:
        L2=Label(top, text="Message has been tampered")
        L2.pack(side=LEFT)
    else:
        L2=Label(top, text="Message has not been tampered")
        L2.pack()

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12354
s.connect((host,port))
top=Tk()
L1=Label(top, text="Enter the request")
L1.pack(side=LEFT)
E1=Entry(top,bd=5)
B1=Button(top, text="Send to server", command=server)
B1.pack()
E1.pack()
B2=Button(top,text="Receive from server",command=fromserver)
B2.pack()

top.mainloop()
s.close()
