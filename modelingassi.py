import sys
import numpy as np

fname = "7.txt"
lines = []
current_voltage_source = 0
current_current_source = 0
voltages_m = []
current_m = []
lines = [line.rstrip('\n') for line in open(fname)]
m = 0
H = 0
n = len(lines[0].split(' ')) - 3
n2 = n
steps=False
for x in range(len(lines)):
	lines[x] =lines[x].split(' ')
	if(lines[x][0]=='Vsrc'):
		m+=1
	elif(lines[x][0]=='I'):
		print('fiound an inductor')
		m+=1
		steps=True


B = np.zeros((n,m))	## Calculate M first and use it
G = np.zeros((n,n))
D = np.zeros((m,m))
Z = np.zeros((n+m,1))

A = np.zeros((n+m,n+m))
#Hard coded
V = np.zeros((2,1))

def constructCircit(lines, H, v1, v2):
	global current_voltage_source
	global m
	global current_current_source
	x = 0
	current_current_source = 0
	current_voltage_source = 0
	for x in range(len(lines)):
		vs = []
		for i in range(n+1):
			if(i!=0):
				vs.append(lines[x][i].strip('v'))
		if(len(vs)>2):# more than two nodes, then a 'v' is to be elminated from the lest
			index = vs.index('0')
			del vs[index]
		if(lines[x][0]=='R' or lines[x][0]=='C' or lines[x][0]=='I'):
			if(lines[x][0]=='R'):
				if('0' in vs):
					 index = vs.index('0')
					 del vs[index]
					 v = int(lines[x][1+n])
					 v = float(1)/v   #v for value
					 G[int(vs[0])-1][int(vs[0])-1] += v
				else:
					 v = float(lines[x][1+n])  #v for value of the component
					 v=float(1)/v
					 G[int(vs[0])-1][int(vs[1])-1] -= v
					 G[int(vs[1])-1][int(vs[0])-1] -= v
					 G[int(vs[1])-1][int(vs[1])-1] += v
					 G[int(vs[0])-1][int(vs[0])-1] += v
			elif(lines[x][0]=='I'):
				i = current_voltage_source
				v = int(lines[x][n+1])
				current_voltage_source += 1
				# v = i * L/H, where i is updated every iteration
				Z[current_voltage_source+m][0] = v
				#Z done
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
				#B done

			elif(lines[x][0]=='C'):
				node1 = 0
				node2 = 0
				if('0' in vs):
					 index = vs.index('0')
					 del vs[index]
					 if(index==0):
					 	node2 = vs[0]
					 #Logic in the past three lines to be fixed
					 # v = c*j/H
					 v = float(lines[x][3])/H
					 G[int(vs[0])-1][int(vs[0])-1] += v
				else:
					 node1 = vs[0]
					 node2 = vs[1]
					 v = float(lines[x][3])/H  #v for value of the component
					 G[int(vs[0])-1][int(vs[1])-1] -= v
					 G[int(vs[1])-1][int(vs[0])-1] -= v
					 G[int(vs[1])-1][int(vs[1])-1] += v
					 G[int(vs[0])-1][int(vs[0])-1] += v
			# 	# Add the current source with i = v*c/H
				if(node1==0):
					if(node2==1):
						i = v1 * (float(lines[x][3]))/H
					elif(node2==2):
						i = v2 * (float(lines[x][3]))/H
				elif(node1==1):
					if(node2==0):
						i = -v1 * float(lines[x][3])/H
					elif(node2==2):
						i = (v2-v1) * (float(lines[x][3]))/H
				elif(node1==2):
					if(node2==0):
						i = -v2 * (float(lines[x][3]))/H
					elif(node2==2):
						i = (-v2+v1) * (float(lines[x][3]))/H

				# this is a very bad thing thats i'm going to do
				# Z[int(vs[0])-1][0] += i
				# if(len(vs)==2):
				# 	Z[int(vs[1])-1][0] -= i
				Z[int(vs[0])-1][0] += 0
				if(len(vs)==2):
					Z[int(vs[1])-1][0] -= 0

		if(lines[x][0]=='Vsrc'):
			i = current_voltage_source
			v = int(lines[x][n+1])
			# current_voltage_source += 1
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
			Z[current_current_source][0] = float(lines[x][n+1])
			current_current_source +=1


H=0.1
constructCircit(lines, H, V[0][0], V[1][0])
C = np.transpose(B)
for x in range(n):
	for i in range(n):
		A[x][i] = G[x][i]
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

def constructCircitIterations(lines, H, v1, v2):
	global current_voltage_source
	global m
	global current_current_source
	x = 0
	current_current_source = 0
	current_voltage_source = 0
	for x in range(len(lines)):
		vs = []
		for i in range(n+1):
			if(i!=0):
				vs.append(lines[x][i].strip('v'))
		if(len(vs)>2):# more than two nodes, then a 'v' is to be elminated from the lest
			index = vs.index('0')
			del vs[index]
		if(lines[x][0]=='R' or lines[x][0]=='C' or lines[x][0]=='I'):
			if(lines[x][0]=='I'):
				i = current_voltage_source
				v = int(lines[x][n+1])
				current_voltage_source += 1
				# v = i * L/H, where i is updated every iteration
				Z[current_voltage_source+m][0] = v
				#Z done
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
				#B done

			elif(lines[x][0]=='C'):
				node1 = 0
				node2 = 0
				if('0' in vs):
					 index = vs.index('0')
					 del vs[index]
					 if(index==0):
					 	node2 = int(vs[0])
					 else:
					 	node1 = int(vs[0])
					 #Logic in the past three lines to be fixed
					 # v = c*j/H
					 v = float(lines[x][3])/H
					 G[int(vs[0])-1][int(vs[0])-1] += v
				else:
					 node1 = int(vs[0])
					 node2 = int(vs[1])
					 v = float(lines[x][3])/H  #v for value of the component
					 G[int(vs[0])-1][int(vs[1])-1] -= v
					 G[int(vs[1])-1][int(vs[0])-1] -= v
					 G[int(vs[1])-1][int(vs[1])-1] += v
					 G[int(vs[0])-1][int(vs[0])-1] += v
				if(node1==0):
					if(node2==1):
						i = (float(v1) * float(lines[x][3])/H)
					elif(node2==2):
						i = (float(v2) * float(lines[x][3])/H)
				elif(node1==1):
					if(node2==0):
						i = (float(-v1) * float(lines[x][3])/H)
					elif(node2==2):
						i = (float(v2-v1) * float(lines[x][3])/H)
				elif(node1==2):
					if(node2==0):
						i = (float(-v2) * float(lines[x][3])/H)
					elif(node2==2):
						i = (float(-v2+v1) * float(lines[x][3])/H)

				# print(i)
				Z[int(vs[0])-1][0] += i
				if(len(vs)==2):
					Z[int(vs[1])-1][0] -= i


for x in range(1,10):
	print(Z)
	constructCircitIterations(lines, H, V[0][0], V[1][0])
	V = np.linalg.solve(A,Z)
	# print(V)


# import sys
# import numpy as np

# fname = "1.txt"
# lines = []
# current_voltage_source = 0
# current_current_source = 0
# voltages_m = []
# current_m = []
# lines = [line.rstrip('\n') for line in open(fname)]
# m = 0
# n = len(lines[0].split(' ')) - 3
# for x in range(len(lines)):
# 	lines[x] =lines[x].split(' ')
# 	if(lines[x][0]=='Vsrc'):
# 		m=m+1

# B = np.zeros((n,m))	## Calculate M first and use it
# G = np.zeros((n,n))
# D = np.zeros((m,m))
# Z = np.zeros((n+m,1))

# A = np.zeros((n+m,n+m))

# def constructCircit(lines):
# 	global current_voltage_source
# 	global m
# 	global current_current_source
# 	for x in range(len(lines)):
# 		vs = []
# 		for i in range(n+1):
# 			if(i!=0):
# 				vs.append(lines[x][i].strip('v'))
# 		if(len(vs)>2):# more than two nodes, then a 'v' is to be elminated from the lest
# 			index = vs.index('0')
# 			del vs[index]
# 		if(lines[x][0]=='R'):
# 			if('0' in vs):
# 				 index = vs.index('0')
# 				 del vs[index]
# 				 #Logic in the past three lines to be fixed
# 				 v = int(lines[x][3])
# 				 G[int(vs[0])-1][int(vs[0])-1] += float(1)/v
# 			else:
# 				 v = int(lines[x][3])  #v for value of the component
# 				 G[int(vs[0])-1][int(vs[1])-1] -= float(1)/v
# 				 G[int(vs[1])-1][int(vs[0])-1] -= float(1)/v
# 				 G[int(vs[1])-1][int(vs[1])-1] += float(1)/v
# 				 G[int(vs[0])-1][int(vs[0])-1] += float(1)/v
# 				 print(G)

# 		if(lines[x][0]=='Vsrc'):
# 			i = current_voltage_source
# 			v = int(lines[x][n+1])
# 			current_voltage_source += 1
# 			Z[current_voltage_source+m][0] = v #bug in here
# 			if('0' in vs):
# 				index = vs.index('0')
# 				if(v>0):
# 					B[int(vs[index-1])-1][i] = 1
# 				else:
# 					B[int(vs[index-1])-1][i] = -1
# 			else:
# 				if(v>0):
# 					B[int(vs[0])-1][i] = 1
# 					B[int(vs[1])-1][i] = -1
# 				else:
# 					B[int(vs[0])-1][i] = -1
# 					B[int(vs[1])-1][i] = 1
# 		if(lines[x][0]=='Isrc'): ## to be fixed
# 			Z[current_current_source][0] = int(lines[x][n+1])
# 			current_current_source +=1



# constructCircit(lines)
# m = current_voltage_source
# C = np.transpose(B)
# print(n)
# print(m)
# print(G)
# print(B)
# print(C)
# print(D)
# print(Z)

# for x in range(n):
# 	for i in range(n):
# 		A[x][i] = G[x][i]

# # for x in range(n):
# # 	for i in range(n):
# # 		A[x][i] = B[x][i]
# j = n
# ii = jj =0
# while(ii<m+n-m):
# 	while(j<n+m):
# 		A[ii][j] = B[ii][jj]
# 		jj +=1
# 		j+=1
# 	ii +=1

# i = n
# ii = jj =0
# while(i<m+n):
# 	while(jj<n+m-m):
# 		A[i][jj] = C[ii][jj]
# 		jj +=1
# 	i+=1
# 	ii +=1


# i = n
# ii = jj =0
# while(i<m+n):
# 	while(jj<n+m-m):
# 		A[i][jj] = C[ii][jj]
# 		jj +=1
# 	i+=1
# 	ii +=1

# i = n
# j =n
# ii = jj =0
# while(i<m+n):
# 	while(j<n+m):
# 		A[i][j] = D[ii][jj]
# 		jj +=1
# 		j+=1
# 	i+=1
# 	ii +=1

	
# print(A)

# V = np.linalg.solve(A,Z)
# print(V)