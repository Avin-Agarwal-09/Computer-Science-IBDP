#Write a program that counts how many even numbers are in a 2D array of integers.

def count_value(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 2 == 0:
                count += 1
    return count

matrix = [
        [10, 2, 4, 5],
        [3, 7, 3, 7],
        [5, 1, 9, 12]
        ]

print(count_value(matrix))