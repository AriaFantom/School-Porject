x = int(input("enter x"))
n = int(input("enter the number of terms"))
s=1

for i in range(1,n+1):
    f=1
    for j in range(1,i+1):
        f = f*j
        s = s + (x**i)/f
        print(s)
        