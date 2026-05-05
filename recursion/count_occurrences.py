def count_occurrences(numbers, value):
    if not numbers:
        return 0
    first_count= 1 if numbers[0] == value else 0
    return first_count + count_occurrences(numbers[1:], value)
numbers = [10,5,2,2,4,10,2,3,6,8,5,7]
value = int(input("Enter a value to be searched:"))
print(count_occurrences(numbers, value))