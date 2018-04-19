import sys
from xml.dom import minidom

board=[]

def danger(row,col):
	for (i,j) in board:
		if row==i:
			return True
		if col==j:
			return True
		if abs(row-i)==abs(col-j):
			return True
	return False
	
def placequeen(row, size):
        if row>size:
                print(board)
                sys.exit(0)
        else:
                for col in range(1, size+1):
                        if not danger(row, col):
                                board.append((row,col))
                                placequeen(row+1,size)
                                board.remove((row,col))

xmldoc=minidom.parse('nqu.xml')
name=xmldoc.getElementsByTagName("Q1")[0]
pos=int(name.childNodes[0].nodeValue)

placequeen(pos,8)
