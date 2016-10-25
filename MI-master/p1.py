import os


l = input('Enter your limit: ')
for x in xrange(1,l):
	if(x%2):
		print('Even' + x)
	elif((x%3 || x%5 || x%7 || x%9)and (x!=7)):
		print('Odd' + x)
	elif(x%1 && x%x):
		print('Prime' + x)
