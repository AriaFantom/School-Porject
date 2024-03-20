a = int(input("enter a"))
b = int(input("enter b"))
l = int(input("enter the limit"))
k = (a+(b**0.5))/(a-b)
w=0
for i in range(2,(l+1),2):
    if i%2 == 0:
        k += i*(a+(b**0.5))/(a-b)
    elif i%4 == 0:
        w += i*(a+(b**0.5))/(a-b)
print(k+w)