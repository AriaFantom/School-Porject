A = int(input("enter 1 for SI and 2 for CI"))
if A == 1:
    P=int(input("enter the absolute value of principal" ))
    R= int(input("enter the rate of interest"))
    T= int(input("enter the time"))
    SI =  (P*R*T)/100 
    print("the desired SI is :" , round(SI))
elif A == 2:
    p=int(input("enter the absolute value of principal: "))
    r=int(input("enter the rate of ineterest: "))
    t = int(input("enter the time period: "))
    n = int(input("enter the compound frequency: "))
    CI =  p*(1 + r/n)**t 
    print("the desired CI :" , round(CI))
else:
    print("wrong input!!")