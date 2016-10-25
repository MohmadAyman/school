'''
Created on Sep 6, 2016

@author: farida
'''
import string
import random

from numpy import square



score = random.randint(1,100)

#if/elif/else
if score >= 90:
    print (str(score) +" is more than 90: A")
elif score >= 80:
    print (str(score) +" is between 80 and 90: B")
elif score >= 70:
    print (str(score) +" is between 70 and 80: C")
elif score > 60:
    print (str(score) +" is between 60 and 70: D")
else:
    print (str(score) +" is less than 60: Failed")
 
#NO switch case

#for definite loops
print("Numbers in range of 5 [0,1,2,3,4]")
for i in range(5):
    print(i, end=" ") 

print("\nSquare of numbers in range of 5 [0,1,2,3,4]")
for i in square(range(5)):
    print(i, end=" ") 
names=['Ahmed','Amira','Mohamed','Mohsen','Abeer']
names+=['Mona','Dalia','Menna','Yasmine','Malak','Omar']
print("")
print(sorted(names))
print(sorted(names,reverse=True))
names.remove('Menna')
print(names)

[print(n) for n in names]


for x in string.ascii_lowercase:
    count = 0
    for name in names:
        if(name.casefold().startswith(x)): #if_statement
            count+=1
    if(count > 0):
            print(str(x).upper()+" : "+str(count))
 

#while indefinite loop
temp = 27
low_threshold = 20
high_threshold = 30
while temp>low_threshold: #indefinite loop
    temp -= 1
    print("Current temperature is "+str(temp))
 
 
#take input from user   
temp = input("Enter the current temperature:")
while True: #indefinite loop
    if (int(temp)<low_threshold or int(temp) >high_threshold):
        break   #break statement
    print("While loop: Current temperature is "+str(temp))
    temp = input("Enter the current temperature:")
 
#continue   
for letter in 'Python':    
    if letter == 'h':
        continue #continue statement
    print ('Current Letter :'+ letter)

#pass
for letter in 'Python': 
    if (letter == 'h'):
        pass
        print ('This is pass block')
    print ('Current Letter :'+letter)      
      
#try/except
try: #to avoid ValueError: invalid literal for int() with base 10
    int_value = input("Enter an integer please :")
    print(int(int_value))
except:
    print("The value entered is not an integer!")
finally:
    print("Executed in both cases.")   

