NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = (input("Please enter the Value of %d Element : " %i))
    NumList.append(value)
a = input("to find:  ")
if a in NumList:
    print("its there")
else:
    print("its not")

