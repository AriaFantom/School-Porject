q = []
Number = int(input("Please enter the Total Number of List Elements: "))
sum = 0
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    q.append(value)
    sum += value
print(q)
q.sort()
mode = q[0]
l,m,k,f=0,0,0,0
for j in range(1, Number):
    if(mode < q[j]):
        mode = q[j]
print("mode is: ", mode)
x = len(q)
mean = sum/x
print("mean is:  ", mean)
s = len(q)
if ((s%2)!= 0):
    k = (s + 1)/2
    print(k)
    print("median is:  ", q[int(k+1)])
elif ((s%2)==0):
    l= ((s)/2 + 1)
    m = ((s)/2)
    f = (q[int(l-l)]+ q[int(m-1)])/2
    print("median is:  " , f)