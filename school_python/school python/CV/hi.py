NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = (input("Please enter the Value of %d Element : " %i))
    NumList.append(value)
rev=""
string2=""
for i in range(0,Number):
   string2= NumList[i] 
   k = len(string2)
   m = string2[k::-1]
   print(m)