a = int(input("Enter the number of terms: "))
n1, n2 = 0, 1
count = 0
while count < a:
    print(n1)
    n1, n2 = n2, n1 + n2
    count += 1


n=int(input("Enter the number of terms: "))
a=0
b=1
for i in range(0,n):
    print(a)
    c=a+b
    a=b
    b=c

    