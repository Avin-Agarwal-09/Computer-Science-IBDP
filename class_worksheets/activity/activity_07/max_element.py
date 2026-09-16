#Create a program that finds the maximum element in each row of a matrix and stores the results in a 1D array.

matrix = [
    [10, 2, 4],
    [3, 7, 3],
    [5, 1, 9]
]

max_values = [0, 0, 0]

for i in range(3):
    max_in_row = matrix[i][0]
    for j in range(3):
        if matrix[i][j] > max_in_row:
            max_in_row = matrix[i][j]
    max_values[i] = max_in_row

print(max_values)
