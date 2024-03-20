Number = int(input(" Please Enter any Number: "))
 
print(" sum of Prime numbers between", 1, "and", Number, "are:")
sum = 0
for num in range(1, Number + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           sum +=num
print(sum)