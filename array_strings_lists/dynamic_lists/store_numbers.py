numbers = []

for i in range(3):
    x = str(input("Enter a number"))
    numbers.append(x)

print(numbers)

for i in range(3):
    z = str(input("Enter a number"))
    numbers.append(z)

print("length of the list is",len(numbers))

print(numbers[0])

y = numbers[0]

for j in range(len(numbers)):
    numbers[j] = y

print(numbers)