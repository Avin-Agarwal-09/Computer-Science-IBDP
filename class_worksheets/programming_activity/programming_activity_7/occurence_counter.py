#Write a function that counts how many times a specific value appears in a 2D array.

def count_value(matrix, target):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                count += 1
    return count

matrix = [
        [10, 2, 4, 5],
        [3, 7, 3, 7],
        [5, 1, 9, 12]
        ]

target = int(input("Enter a number"))
print(count_value(matrix,target))