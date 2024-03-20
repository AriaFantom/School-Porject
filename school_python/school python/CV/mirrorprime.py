n = int(input("enter the prime number"))
tempNum = n
rev = 0   
while tempNum > 0:
    numDig = tempNum % 10
    rev = rev * 10 + numDig
    tempNum = tempNum // 10
print(rev)
for j in range (2 , rev):
    if (n%j) != 0:
        print("mirror")
        break
    else:
        print("not a mirror prime")