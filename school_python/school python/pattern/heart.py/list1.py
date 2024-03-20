r=int(input("Enter the number of rows"))
c=int(input("Enter the number of columns"))

a=[] 
for i in range(0,r):
    lst=[]
    for j in range(0,c):
        x=int(input("Enter something"))
        lst.append(x)
    a.append(lst)
for i in range(0,r):
    for j in range(0,c):
        if i == j or i + j == r-1 : 
            print(a[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()