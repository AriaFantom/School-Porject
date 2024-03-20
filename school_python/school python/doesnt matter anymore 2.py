side = int(input("Please Enter any Side of a Square  : "))

print("Hollow Square Star Pattern") 
if side%2 != 0:
    for i in range(side):
            for j in range(side):
                if(i == 0 or i == side - 1 or j == 0 or j == side - 1 or i==((side+1)/2)-1 or j==((side+1)/2)-1  ):
                    print('*', end = '  ')
                else:
                    print(' ', end = '  ')
            print()
else:
        for i in range(side):
            for j in range(side):
                if(i == 0 or i == side - 1 or j == 0 or j == side - 1 or i==((side)/2)-1 or j==((side)/2)-1  ):
                    print('*', end = '  ')
                else:
                    print(' ', end = '  ')
            print()

