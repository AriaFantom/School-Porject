n = (input("enter number:"))
l = len(n)
a = int(n)**2
print(a%10)
if (a%10)**l == int(n):
    print("automorphic number")