#Write a program to check wheter each digits of number provided by the user input as 'a' is divisible by the number 'n' 
#provided by the user if all the 
#number is divisible print - all good. if some are divisible then print 'its ok some are divisible' if none is divisible then print no



a = int(input("enter a"))
n = int(input("enter n"))
w=0
k2=0
k1=1
while (a>0):
    digit=a%10
    if digit <= 9:
        if digit %n ==0 :
            k1 = 3
        elif digit%n !=0:
            k2 = 1
    w =w + ((k1)+(k2))
    #print(w)
    
    a = a//10

#print(w)
if w%3==0:
   print("all good")
elif w>0:
   print("its ok some are divisible")
elif w==0:
   print("no")