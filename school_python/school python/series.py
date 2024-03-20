#import math

#x = int(input('enter value of x'))
#n = int(input('enter value of n'))
 
#a = 1-x
#for i in range (1,n):
    #b = a + ((-1)**(i+1))*((x**(i+1))/math.factorial(i+1))
    #a=b
#print(b)    

x = int(input('enter value of x'))
n = int(input('enter value of n'))
a=1
fact= 1
for i in range(1,n+1):
    fact=fact*i
    b = a + ((-1)**(i))*((x**(i))/fact)
    a=b
print(b)