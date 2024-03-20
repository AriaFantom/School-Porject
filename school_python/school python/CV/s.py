#write a program to check weather a string is a palindrome or not

str = input("enter a string:")
l = int(len(str))
k=int(l/2)
f=0
l1 = l-1
for i in range(0,k):
    if str[i] != str[l-i-1]:
        f=1
        break
if f==1:
    print("not palindrome")
else:
    print("palindrome")