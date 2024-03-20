


print("Operation: F to C(then press 1), C to F(then press 2)")
select = input("Select operations: ")


if select == "1":
   F = int(input('Enter temperature in Farenheit: '))
   C = (F-32)*5/9
   
   print("the temperature in celcius is" , round(C) )

elif select == "2":
   C = int(input('Enter temperature in Celsius: '))
   F = (9*C/5)+32
   
   print("the temperature in Farenheit is" , round(F) )
else :
    print("wrong input")
