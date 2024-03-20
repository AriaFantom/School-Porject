num = int(input("enter the number: "))
tempnum = num
rev = 0
while tempNum > 0:
    numDig = tempNum % 10
    rev = rev * 10 + numDig
    tempNum = tempNum // 10
print("The reverse of num is:", rev)
if rev == num:
    print("The given number is Palindrome.")
else:
    print("The given number is not Palindrome.")