number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
number3 = int(input('Enter the third number: '))
if number1 > number2 and number1 > number3:
    print('The largest number is: ', number1)
elif number2 > number1 and number2 > number3:
    print('The largest number is: ', number2)
elif number3 > number1 and number3 > number2:
    print('The largest number is: ', number3)
else:
    print('The numbers are equal')