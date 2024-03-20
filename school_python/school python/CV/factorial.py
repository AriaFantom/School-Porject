n =  int(input("enter the number: "))
fact = 1
  
for i in range(1,n+1):
    fact = fact * i
      
print ("The factorial of the number is : ",end="")
print (fact)