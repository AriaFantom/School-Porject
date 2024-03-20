num = int(input("Please enter any integer to find divisors = "))

print("The Divisors of the Number = ")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
        