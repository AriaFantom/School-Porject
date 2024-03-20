x = int(input('enter value of x'))
n = int(input('enter value of n'))
fact = 1
b=0
for i in range(2,n+1):
    fact=fact*i
    b += ((-1)**(i))*((x**(i))/fact)
b=b+x
print(b)