height=float(input("enter your height(in metres or feet): "))
weight=float(input("enter your weight(in kilograms): "))
BMI=(weight)/(height**2)
if BMI < 18.5:
    print("you are underweight and your BMI is ", BMI)
elif BMI >=18.5 and BMI<=25:
    print("you are normal and your BMI is ", BMI)
else:
    print("you are obese and your BMI is", BMI)