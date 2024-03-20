r=int(input("Enter the number of rows"))
c=int(input("Enter the number of columns"))

a=[]
for i in range(0,r):
    lst=[]
    for j in range(0,c):
        x=int(input("Enter something"))
        lst.append(x)
    a.append(lst)

#k=0
print(a)
for i in range(0,r):
    k=0
    for j in range(0,c):
        k+=a[i][j]
    print(k)
#print(k)