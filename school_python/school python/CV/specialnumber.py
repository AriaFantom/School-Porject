n = int(input("enter the number:"))
n1 = n
s = 0
while(n>0):
    r = n%10
    f = 1
    for i in range (1 , r+1):
        f = f*i
    s = s + f
    n = n//10
if (n1 ==s):
    print("special number")
else:
    print("not a special number")