import sys
import fs
list_of_lists = []
maxN = 0
answerClose = []
sumsofar = 0
fname = "netlist"
lines = []

lines = [line.rstrip('\n') for line in open(fname)]

def constructCircit(lines):
	for x in range(len(lines)):
		if(lines[0]=='R'):

		elif(lines[0]=='R'):

		


for x in range(len(list_of_lists)):
	p = list_of_lists[x]
	N = p[0]
	CDs = p[1]
	found_value = False
	sumsofar = 0
	if(not permute([],p[2:],0)):
		ss = ' '.join(map(str ,answerClose))
		s=sum(answerClose)
		print(ss+" sum:%d" % s)
	list_of_lists[x]=[]
