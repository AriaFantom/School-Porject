n = int(input("enter the number:  "))
c =0
while (n>0):
    digit=n%10
    if (digit == 0):
        c = c+1 
        break
    n = n//10
if c == 1:
    print("duck")
else:
    print("not a duck")