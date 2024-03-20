#n=int(input("enter the number of rows:"))
#for i in range(0,n):
    #print(('*'*(2*(i)+1))+' '*(n-i-1))

#n=int(input("enter the number of rows: "))
#for i in range(0,n):
 #   print(' '*(i+1)+'*'*(n-i)+'*'*(n-i-1))
z=""
n=int(input("enter"))
k=ord("A")
for i in range(1,n+1):
    z=chr(k)*i
    k=k+1
    print(z)