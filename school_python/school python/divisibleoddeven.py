n = int(input("enter n:"))
m = int(input("enter m:"))
for i in range(1,n+1):
    a = m%i
    if a==0:
        print("divisible by ", i)
if n%2 ==0:
    print("entered number is even")
else:
    print("entered number is odd")