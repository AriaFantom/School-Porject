x = int(input("enter the number: "))
n = int(input("enter the number of times: "))
a = 1
for i in range(1,n+1):
    b = a+((-1)**i)*(x**(i))
    a=b
print(b)

x = int(input('enter value of x'))
n = int(input('enter value of n'))
a = 1
for i in range(1,n+1):
    b = a + ((-1)**(i))*((x**(i)))
    a=b
print(b)