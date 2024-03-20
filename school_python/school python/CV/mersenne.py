a = int(input("enter mersenne number:  "))
n=int(input("enter times:   "))
for a in range(1,n+1):
    k = (2**a) -1
    print(k , end=" ")
