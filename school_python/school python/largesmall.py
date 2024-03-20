NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

smallest = largest = NumList[0]

for j in range(1, Number):
    if(smallest > NumList[j]):
        smallest = NumList[j]
    elif (largest < NumList[j]):
        largest = NumList[j]
        
print("The Smallest Element in this List is : ", smallest)
print("The Largest Element in this List is : ", largest)