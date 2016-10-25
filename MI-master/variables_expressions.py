'''
Created on Sep 5, 2016

@author: farida
'''
import math



#int and float variables
x = 8
y = 20

print(x)
print("Addition: "+str(x+y)) # expression evaluation needs explicit type conversion to string
print("Multiplication: "+str(x*y))
print("Division: "+str(y/x))
print("Floor Division: "+str(y//x))
print("2 Power 8: "+str(2**8))
print("y Modulus 3: "+str(y%3))
k = 4.0
print("x times k: "+str(x*k))

print(type(x))
print(type(k))
print(type(y/x))
print(type(y//x))


#bool
a= True
b = False
print(type(a))

print("a AND b : "+str(a and b))
print("a OR b : "+str(a or b))
print("NOT a  : "+str(not a))

print("a bitwise AND b : "+str(a & b))
print("a bitwise OR b : "+str(a | b))
print("a XOR b : "+str(a ^ b))

print("9 > 5 : "+ str(9>5) )
print("9 < 5 : "+ str(9<5) )
print("9 == 8 : "+ str(9==8) )
print("9 != 8 : "+ str(9!=8))

#string
z= 'hello'
l= "world"
print(type(z))

name = "class 2017"
concatenated_str = "{} {} {}!".format(z.capitalize(),l.capitalize(),name.capitalize())
print(concatenated_str)
print(concatenated_str.split(sep=' '))
print(concatenated_str.split(sep=' ')[2][:])
print(concatenated_str.replace('Class 2017', '2017 Graduates'))
print(concatenated_str.find("Class")) 

print(concatenated_str+' didn\'t change')

text= concatenated_str+"\n" "Hi "+name.capitalize()
print(text[:23])
print(text)
print('C:\some\name')  # here \n oncatenated_str.split(sep=' ')means newline!
print(r'C:\some\name') # r: raw string to avoid interpreting special characters
print(3*'Hi')
print(3*'Hi'.swapcase())
print(3*'Hi'.casefold())
print(3*'Hi'.upper())
print(text.partition('\n'))
print(text.partition('\n')[2])
print(text.splitlines())
print(' '.join(text.splitlines()))
print(' '.join([z,l,name]))


numbers=[1,13,301,5343,89380]
for n in numbers:
    print(str(n).zfill(5))


#List
squares = [1,4,8,16,25]
print(type(squares))
print(type(squares[1]))
print(squares[2]) #indexing
squares[2] = 9 #mutable
print(squares[:])
print(squares[-2]) #circular list
squares.append(36)
print(squares)
squares+= [49,64,81,100]
print(squares)
print(len(squares))
squares[10:11]=[121,144]
print(squares[:6])
print(squares[6:])

#2d list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(type(matrix))
print(matrix[0])
matrix[1][0]=0
print(matrix[1])
matrix.append([10,11,12])
print(matrix)
print(len(matrix))
print(len(matrix[3]))


#tuple
location =(0,10)
print(location)
print(type(location))
(x,y)=location
print(x)
print(y)
location=(x,y,20)
print(location)
print(location.count(0))
print(location.__getitem__(2))
print(location.index(20))

#dict: dictionary
french = dict()
french['yes'] = 'oui'
french['no'] = 'non'
french['one'] = 'un'
french['two'] = 'deux'
french['three'] = 'trois'

print(french)
print(type(french))
print(french['two'])
french.__setitem__("four", "quatre")
print("Count in french: {one}, {two}, {three}, {four}".format(**french))

french = {'one':'un',
          'two' :'deux',
          'three' : 'trois',
          'four' : 'quatre',
          'five' : 'cinq',
          'six' : 'six',
          'seven' : 'sept',
          'eight' : 'huit',
          'nine' : 'neuf',
          'ten' : 'dix'
          }
print (french)
          

