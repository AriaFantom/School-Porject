NumList = []
q=[]
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)
    k=(value)**3
    q.append(k)
print("the cubed list is" ,q)