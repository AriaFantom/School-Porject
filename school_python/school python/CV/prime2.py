A = int(input("enter the number:  "))
B = int(input("enter the 2nd number:  "))


for i in range(A,B):
    if A%i == 0:
        if A<i and B>i:
            print(i)
print("hault")
for j in range(1,B):
    if B%j == 0:
        if A<j and B>j:
            print(j)