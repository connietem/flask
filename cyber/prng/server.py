import socket
import random
p=23
q=7
def prng(seed):
	r1=random.randint(0,100)
	r2=random.randint(0,100)
	r3=random.randint(0,100)
	rand_num=(seed*r1)+(r2%r3)
	return rand_num

def calc_public(b):
	global p,q
	B=(q**b)%p
	return B

def calc_private(A):
	global p
	key=(A**b)%p
	return key

def encrypt(msg):
	number=[]
	sec_key=calc_private(int(A))
	print("Secret Key is-"+str(sec_key))
	for m in msg:
		number.append(ord(m)+sec_key)
	print(number)
	return number

s=socket.socket()
host=socket.gethostname()
port=12355
s.bind((host,port))
s.listen(2)
c,addr=s.accept()
seed=input("Enter the seed value-")
b=prng(seed)
B=calc_public(b)
print("Connected to "+ str(addr))
A=c.recv(1024)
print("Received public key of A is "+str(A))
c.send(str(B))
msg=raw_input("Enter the message to be encrypted-")
message=encrypt(msg)
c.send(str(message))
c.close()
s.close()
