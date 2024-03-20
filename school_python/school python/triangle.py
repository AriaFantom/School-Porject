number1 = int(input('Enter the first side: '))
number2 = int(input('Enter the second side: '))
number3 = int(input('Enter the third side: '))
if number1 > number2 and number1 > number3:
    number1=k
    number2,number3=c,w
elif number2 > number1 and number2 > number3:
    number2=k
    number1,number3=c,w
elif number3 > number1 and number3 > number2:
    number3=k
    number1,number2=c,w 
if k<(c+w):
    print("sides are of triangle")
else:
    print("sides are not of triangle")