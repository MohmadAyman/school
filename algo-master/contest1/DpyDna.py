import sys
import copy

list_of_lists = []
list_of_DNA_lists =[]

list_of_sofar = []
answer = []
answerG =[]

l = sys.stdin.readline()

# def uniq(lst):
#     last = object()
#     for item in lst:
#         if item == last:
#             continue
#         yield item
#         last = item

for x in range(int(l)):
    line = sys.stdin.readline()
    new_list = [int(elem) for elem in line.split()]
    list_of_lists.append(new_list)
    line = sys.stdin.readline()
    new_DNA_list = line.rstrip()
    list_of_DNA_lists.append(new_DNA_list)

def permute(sofar , rest):
	if(len(rest)==0):
		answer.append(sofar)
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
	mut_list_G = []
	mut_list_T = []	
	mut_list_C = []
	p = list_of_lists[x]
	G = p[0]
	K = p[1]
	L = list_of_DNA_lists[x]

	for j in range(K):
		mut_list_G.append('G')
		mut_list_C.append('C')
		mut_list_T.append('T')

	#I dont have to call the function 3 times!!!
	permute([],list(L[0:G-K])+mut_list_T)
	list_of_sofar =[]

	answerG = list(answer)

	for x in range(len(answer)):
		for i in range(len(answer[x])):
			if(answer[x][i]=='T'):
				answerG[x][i]='G'


	answer = sorted(answer)

	print(len(answer)+1)
	for x in range(len(answer)):
		print(''.join(answer[x]))
		print(''.join(answerG[x]))

	answer =[]
