#Write a program to find the sum of following (Accept values of a, r, n from user) a + ar + ar2 + ar3 + ………..arn


a = int(input('enter value of a'))
r = int(input('enter value of r'))
n = int(input('enter value of n'))
for i in range(1,n+1):
    k = a + (a*r**n)
print(k)