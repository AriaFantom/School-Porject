x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
if x > y:
    s = y
else:
    s = x
for i in range(1,s + 1):
    if((x % i == 0) and (y % i == 0)):
        hcf = i
print("The H.C.F. of", x,"and", y,"is", hcf)