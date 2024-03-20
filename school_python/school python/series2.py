x = int(input('enter value of x'))
n = int(input('enter value of n'))
b=1
for i in range(1,n+1):
    b += ((-1)**(i))*(x**(i))

print(b)