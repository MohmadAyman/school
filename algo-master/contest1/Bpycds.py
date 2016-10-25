import sys

list_of_lists = []
maxN = 0
answerClose = []
sumsofar = 0

for line in sys.stdin:
    if(line =='\n'):
    	break
    new_list = [int(elem) for elem in line.split()]
    list_of_lists.append(new_list)


def permute(sofar , rest, sumsofar):
	if(sumsofar==N):
		print(' '.join(map(str ,sofar))+" sum:%d" % sumsofar)
		return True
	elif(sumsofar<N):
		global maxN
		global answerClose
		if(sumsofar>maxN):
			maxN = sumsofar
			answerClose = sofar
	elif(sumsofar>N):
		return

	if(len(rest)==0):
		return
	else:
		for i in range(len(rest)):
			if(permute(sofar+[rest[i]], rest[0:i]+rest[i+1:], sumsofar+rest[i])):
				rest = []
				return True
	return False

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
