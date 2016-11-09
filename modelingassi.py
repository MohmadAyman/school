import sys
import numpy as np

fname = "2.txt"
lines = []
current_voltage_source = 0
current_current_source = 0
voltages_m = []
current_m = []
lines = [line.rstrip('\n') for line in open(fname)]
m = 0
n = len(lines[0].split(' ')) - 3
for x in range(len(lines)):
	lines[x] =lines[x].split(' ')
	if(lines[x][0]=='Vsrc'):
		m=m+1

B = np.zeros((n,m))	## Calculate M first and use it
G = np.zeros((n,n))
D = np.zeros((m,m))
Z = np.zeros((n+m,1))

A = np.zeros((n+m,n+m))

def constructCircit(lines):
	global current_voltage_source
	global m
	global current_current_source
	for x in range(len(lines)):
		vs = []
		for i in range(n+1):
			if(i!=0):
				vs.append(lines[x][i].strip('v'))
		if(len(vs)>2):# more than two nodes, then a 'v' is to be elminated from the lest
			index = vs.index('0')
			del vs[index]
		if(lines[x][0]=='R'):
			if('0' in vs):
				 index = vs.index('0')
				 del vs[index]
				 #Logic in the past three lines to be fixed
				 v = int(lines[x][1+n])
				 v = 1/v   #v for value
				 G[int(vs[0])-1][int(vs[0])-1] += v
			else:
				 v = int(lines[x][1+n])  #v for value of the component
				 v=1/v
				 G[int(vs[0])-1][int(vs[1])-1] -= v
				 G[int(vs[1])-1][int(vs[0])-1] -= v
				 G[int(vs[1])-1][int(vs[1])-1] += v
				 G[int(vs[0])-1][int(vs[0])-1] += v
				 print(int(vs[0])-1)

		if(lines[x][0]=='Vsrc'):
			i = current_voltage_source
			v = int(lines[x][n+1])
			current_voltage_source += 1
			Z[current_voltage_source+m][0] = v #bug in here
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
		if(lines[x][0]=='Isrc'): ## to be fixed
			Z[current_current_source][0] = int(lines[x][n+1])
			current_current_source +=1



constructCircit(lines)
m = current_voltage_source
C = np.transpose(B)
print(n)
print(m)
print(G)
print(B)
print(C)
print(D)
print(Z)

for x in range(n):
	for i in range(n):
		A[x][i] = G[x][i]

# for x in range(n):
# 	for i in range(n):
# 		A[x][i] = B[x][i]
j = n
ii = jj =0
while(ii<m+n-m):
	while(j<n+m):
		A[ii][j] = B[ii][jj]
		jj +=1
		j+=1
	ii +=1

i = n
ii = jj =0
while(i<m+n):
	while(jj<n+m-m):
		A[i][jj] = C[ii][jj]
		jj +=1
	i+=1
	ii +=1


i = n
ii = jj =0
while(i<m+n):
	while(jj<n+m-m):
		A[i][jj] = C[ii][jj]
		jj +=1
	i+=1
	ii +=1

i = n
j =n
ii = jj =0
while(i<m+n):
	while(j<n+m):
		A[i][j] = D[ii][jj]
		jj +=1
		j+=1
	i+=1
	ii +=1

	
print(A)

V = np.linalg.solve(A,Z)
print(V)


