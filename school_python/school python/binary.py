integer=int(input("enter the integer:  "))


binary_string = ''


while(integer > 0):
    digit = integer % 2
    binary_string += str(digit)
    integer = integer // 2
binary_string = binary_string[::-1]
print(binary_string)