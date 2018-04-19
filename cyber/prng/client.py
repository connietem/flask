import socket
import random
import ast
p=23
q=7
def prng(seed):
	r1=random.randint(0,100)
	r2=random.randint(0,100)
	r3=random.randint(0,100)
	number=(seed*r1)+(r2%r3)
	return number

def calc_public(a):
	global p,q
	key=(q**a)%p
	return key

def calc_private(B):
	global p
	secret=(B**a)%p
	return secret

def decrypt(message):
	key=calc_private(int(B))
	number=[]
	message=ast.literal_eval(message)
	for m in message:
		number.append(chr(int(m)-key))
	str=""
	for d in number:
		str+=d
	print(str)

s=socket.socket()
host=socket.gethostname()
port=12355
s.connect((host,port))
seed=input("Enter the seed value")
a=prng(seed)
A=calc_public(a)
s.send(str(A))
B=s.recv(1024)
message=s.recv(1024)
print(message)
decrypt(message)
s.close()
