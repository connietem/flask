from pymongo import MongoClient
import threading
from threading import Thread
import time

class phil(Thread):
	connection=MongoClient("localhost",27017)
	def read_m(self,indexx):
		db=phil.connection.test.diniraw7
		cursor=db.find({"ph_no":indexx})
		print cursor[0]

	def __init__(self,indexx,name,leftf,rightf):
		Thread.__init__(self)
		self.name=name
		self.indexx=indexx
		self.leftf=leftf
		self.rightf=rightf

	def run(self):
		while(self.running==True):
			time.sleep(6)
			print 'Philosopher %d is hungry'%self.indexx
			self.get_fork()

	def get_fork(self):
		fork1=self.leftf
		fork2=self.rightf

		while(self.running==True):
			fork1.acquire(True)
			val=fork2.acquire(False)
			if val:
				break

			fork1.release()
			fork1,fork2=fork2,fork1
		else:
			return
		self.dine()
		fork1.release()
		fork2.release()

	def dine(self):
		print "Philosopher %d is finally eating"%self.indexx
		self.read_m(self.indexx)
		time.sleep(5)
		print "Philosopher %d has finally finished eating"%self.indexx
def dining():
	fork=[]
	for i in range(5):
		fork.append(threading.Lock())
	names=("a","b","c","d","e")
	phils=[]
	for i in range(5):
		phils.append(phil(i,names[i],fork[i%5],fork[(i+1)%5]))
	phil.running=True
	for p in phils:
		p.start()
	time.sleep(30)
	print "Finishing!"
	phil.running=False

dining()		
