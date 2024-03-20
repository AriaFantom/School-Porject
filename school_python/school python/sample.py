x = int(input("Enter the x's value: "))
n = int(input("Enter the nth value: "))
S=1

for i in range(2,n+1):
    f=1
    for j in range(1,i+1):
        f *= j
    S = S + (-1**i)*(x**i)/f
print(S)