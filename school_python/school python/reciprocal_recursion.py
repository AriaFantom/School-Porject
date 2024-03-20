x = int(input('enter value of x'))
n = int(input('enter value of n'))
b=0
for i in range(1,x+1):
    
    b += 1/(n-i)

print(int(b))