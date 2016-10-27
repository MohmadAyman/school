import sys
import numpy as np

list_of_lists = []
answerClose = []
sumsofar = 0
fname = "netlist.txt"
lines = []
current_voltage_source = 0
current_current_source = 0
voltages_m = []
current_m = []
lines = [line.rstrip('\n') for line in open(fname)]
n = len(lines[0].split(' ')) - 3
m = 0
B = np.zeros((2,n))	## Calculate M first and use it
G = np.zeros((n,n))
D = np.zeros((2,2))
i = np.zeros((n,1))
e = np.zeros((2,1))
Z = np.zeros((n+2,1))

def constructCircit(lines):
	global current_voltage_source
	global m
	global current_current_source
	for x in range(len(lines)):
		vs = []
		lines[x] =lines[x].split(' ')
		for i in range(n+1):
			if(i!=0):
				vs.append(lines[x][i].strip('v'))
		if(len(vs)>2):# more than two nodes, then a 'v' is to be elminated from the lest
			index = vs.index('0')
			del vs[index]
		m = len(vs)
		if(lines[x][0]=='R'):
			if('0' in vs):
				 index = vs.index('0')
				 del vs[index]
				 #Logic in the past three lines to be fixed
				 v = int(lines[x][1+n])  #v for value
				 G[int(vs[0])-1][int(vs[0])-1] += v
				 print(int(vs[0])-1)
			else:
				 v = int(lines[x][1+n])  #v for value of the component
				 G[int(vs[0])-1][int(vs[1])-1] -= v
				 G[int(vs[1])-1][int(vs[0])-1] -= v
				 G[int(vs[1])-1][int(vs[1])-1] += v
				 G[int(vs[0])-1][int(vs[0])-1] += v
				 print(int(vs[0])-1)

		if(lines[x][0]=='Vsrc'):
			current_voltage_source += 1
			v = int(lines[x][n+1])
			e[current_voltage_source][0] = v
			i = current_voltage_source
			if('0' in vs):
				index = vs.index('0')
				if(v>0):
					B[int(vs[index-1])-1][i] = 1
				else:
					B[int(vs[index-1])-1][i] = -1
			else:
				if(v>0):
					B[int(vs[0])-1][i] = 1
					B[int(vs[1])-1][i] = -1
				else:
					B[int(vs[0])-1][i] = -1
					B[int(vs[1])-1][i] = 1
		if(lines[x][0]=='Isrc'):
			current_current_source +=1
			i[current_current_source][0] = int(lines[x][n+1])



constructCircit(lines)
C = np.transpose(B)
print(C)
print(G)
print(B)
print(D)
print(i)
print(e)

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
