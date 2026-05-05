numbers = []

for i in range(3):
    x = str(input("Enter a number"))
    numbers.append(x)

print(numbers)

y = numbers[1]
numbers.append(y)

for i in range(len(numbers)):
    if numbers[i] == y:
        print("number was found at:",i)

