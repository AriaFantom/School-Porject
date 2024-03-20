n = int(input("enter the prime number to detect if its a twin prime or not : "))
r = n + 2
for i in range (2,r):
    if r%i != 0:
        print("twin prime")
        break
    else:
        print("not twin prime")