n = int(input("enter the number:  "))
temp=n
k =0

while (n>0):
    d=n%10
    k = k + (d**3)

    n = n//10
    
if (k==temp):
    print("armstrong number")
else:
    print('not an armstrong number')