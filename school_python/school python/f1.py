n=56
n1=n
i=2
s=0
w=0
while n>0:
    f=n%i
    if f==0:
        c=i
        while c>0:
            r=c%10
            s=s+r
            c=c//10
        n=n//10
        i=i-1
    i=i+1
while n1>0:
    k=n1%10
    w+=k
    n1=n//10

if w==s:
    print('smith number')
