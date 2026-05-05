def even(numbers):
    new_array = []
    for i in range(len(numbers)):
        if numbers[i-1] % 2:
            new_array.append(numbers[i])
    return new_array
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even(numbers))