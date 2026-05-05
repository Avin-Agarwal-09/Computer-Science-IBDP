f = open("numb.txt", "r")
numbers = f.read().split()
f.close()

numbers = [int(n) for n in numbers]

for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

f = open("numb.txt", "w")
for n in numbers:
    f.write(str(n) + "\n")
f.close()

print(numbers)