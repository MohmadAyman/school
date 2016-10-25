import sys

list_of_lists = []
answer =[]
list_of_sofar=[]

for line in sys.stdin:
    new_list = [int(elem) for elem in line.split()]
    if(len(new_list)==0):
    	break
    list_of_lists.append(new_list)

def permute(sofar , rest):
	found_value = False
	if(found_value):
		return
	sumsofar = sum(sofar)
	if(sumsofar==N):
		answer.append(sofar)
		found_value = True
		return
	if(len(rest)==0):
		return
	else:
		for i in range(len(rest)):
			next_ = sofar+[rest[i]]
			if(next_ in list_of_sofar):
				pass
			else:
				list_of_sofar.append(next_)
				permute(next_, rest[0:i]+rest[i+1:])

for x in range(len(list_of_lists)):
	p = list_of_lists[x]
	N = p[0]
	CDs = p[1]
	permute([],p[2:])
	if(len(answer)==0):
		print('NONE')
	else:
		for x in range(len(answer)):
			answer[x].sort()
			print(answer)
		for x in range(len(answer)):
			if(answer[x] in answer):	
				pass
			else:
				print(answer[x])
	list_of_sofar = []
	answer = []