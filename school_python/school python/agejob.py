a=float(input("enter your age: "))


if a>1 and a<30:
    print("you are young and unaccepted, return in the year ", (2022 + (36-a)))
elif a>=30 and a<=45:
    print("you are accepted, enjoy working")
else:
    print("you are older, should have come within the years " , (2022-(a-30)) , " - " , (2022-(a-45)))