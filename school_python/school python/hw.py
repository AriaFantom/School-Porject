RN = int(input("enter your roll number"))

N = str(input("enter your name"))

a = int(input("enter your phy marks"))
b = int(input("enter your chem marks"))
c = int(input("enter your comp. sci marks"))

#number_list = [a,b,c]
#avg = sum(number_list)/len(number_list)
#print("The average is ", round(avg,2))
avg = (a+b+c)/3


if avg>=85:
    g="excellent"

elif avg>= 70:
     g="v.good"

elif avg>=60:
     g="good"

else:
    g="not upto the mark"

print("The roll no. , name , grade of the student is" ,RN , N , g)        