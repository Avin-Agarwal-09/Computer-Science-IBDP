numbers = []

for i in range(4):
    x = str(input("Enter a number"))
    numbers.append(x)

print(numbers)

temp_second = numbers[1]
temp_third = numbers[2]
numbers[1] = temp_third
numbers[2] = temp_second

print(numbers)
