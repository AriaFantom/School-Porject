oct = int(input("enter octal number"))
k=str(oct)
a=0
for i in k:
    if i=='0':
        a='000'
    elif i=='1':
        a='001'
    elif i=='2':
        a='010'
    elif i=='3':
        a='011'
    elif i=='4':
        a='100'
    elif i=='5':
        a='101'
    elif i=='6':
        a='110'
    elif i=='7':
        a='111'
    a+=a
print(a)