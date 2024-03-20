NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
sum = 0
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)
    sum += value

NumList.sort()
mode = NumList[0]

for j in range(1, Number):
    if(mode < NumList[j]):
        mode = NumList[j]

print("mode is: ", mode)

x = len(NumList)

mean = sum/x
print("mean is:  ", mean)

if ((x%2)!= 0):
    k = (x + 1)/2
    print(NumList(k))
    
elif ((x%2)==0):
    l= (x)/2 + 1
    m = (x)/2
    f = (NumList(l)+ NumList(m))/2

    print("median is:  " , f)
