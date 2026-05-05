def sum(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total

numbers = [5, 10, 15, 20, 25]
print(sum(numbers))