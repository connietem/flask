import json
import os

inf=open("8q.json")
board=json.loads(inf.read())
board=board["matrix"]
print(*board,sep="\n")
print("\n\n")
def issafe(row,col):
	for i in range(8):
		for j in range(8):
			if(board[i][j]==1):
				if row==i:
					return False
				if col==j:
					return False
				if abs(row-i)==abs(col-j):
					return False
	return True
def place(col):
	if col>=8:
		print(*board,sep="\n")
		print("\n") 
	for i in range(8):
		if(issafe(i,col)):
			board[i][col]=1
			if(place(col+1)==True):
				return True
			board[i][col]=0
	return False

place(1)
