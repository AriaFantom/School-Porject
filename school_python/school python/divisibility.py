#Write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500

for i in range(100,501):
    a=i%(11)
    b=i%(2)
    if (a==0) and (b!=0):
        print(i)
    else:
        print("not divisible", i)
