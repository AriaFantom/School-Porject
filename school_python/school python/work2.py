F = int(input("enter the first number:"))
S = int(input("enter the second number"))
select = int(input("enter the desired operation : 1 for multiply , 2 for divide , 3 for addition, 4 for substraction , 5 for percentage , 6 for exponential power"))
 
if select == 1:
    W = (F*S) 
    print("the required answer is:" , round(W) )
elif select ==2: 
    X = (F/S)
    print("the required number is : " , round(X)) 
elif select == 3:
    Y = (F+S)
    print("the required answer is : " , round(Y))    
elif select == 4:
    Z = (F-S)
    print("the required number is:" , round(Z))    
elif select == 5:
    A = (F*100)/S
    print("the required number is:" , round(A))
elif select == 6:
    B = (F**S)
    print("The required number is : " , round(B))
else:
    print("Wrong input!")
