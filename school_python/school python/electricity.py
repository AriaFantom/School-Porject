a = int(input('neter number of hrs TV ran: '))
b = int(input('enter number of hrs fridge ran '))
c = int(input('enter number of hrs 4 bulbs ran  '))
d = int(input('enter number of hrs 3 fans ran  '))

final = ((a*120)+ (b*800) + (c*40) + (d*35))*0.008

print("Amt to be paid: rupees " , final)
