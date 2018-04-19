import hashlib
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12354
s.bind((host,port))
s.listen(4)
while True:
	c,addr=s.accept()
	print("Connected to"+str(addr))
	mess=c.recv(1024)
	print(mess)
	res = hashlib.sha1(mess.encode())
	c.send(mess+"#"+str(res.hexdigest()))
c.close()


