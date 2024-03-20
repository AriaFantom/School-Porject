RN = int(input("enter your roll number"))

N = str(input("enter your name"))

a = int(input("enter your phy marks"))
b = int(input("enter your chem marks"))
c = int(input("enter your comp. sci marks"))
from statistics import mean
number_list = [a,b,c]
avg = mean(number_list)
print("The average is ", round(avg,2))

if avg>=85:
    print("very good")

elif avg>= 70:
    print("very good")

elif avg>=60:
    print("good")

else:
    print("not upto the mark")    
