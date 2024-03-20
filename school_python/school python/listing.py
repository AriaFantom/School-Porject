a = [2,10,25,37]
k = len(a)
h=[]
for i in range(0,k):
    if ((a[i])%2) == 0:
        m = (a[i])/2
        h.append(m)
    
    else:
        n = (a[i])*2
        h.append(n)

print(h)