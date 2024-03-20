#sum of number in odd places in an user input number
n=(input("enter number"))
f=0
for i in range(1,len(n)+1):
    if i%2 != 0:
        f+=int(n[i-1])
print(f)