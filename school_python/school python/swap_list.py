list = [1,2,3,4,5,6,7,8,9,10]

first_half = list[:int(len(list)/2)]

second_half = list[int(len(list)/2):]

list = second_half + first_half

print(list)