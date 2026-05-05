#Create a program that calculates the sum of each row and each column in a 4×4 matrix.

def create_matrix():
    matrix = [
        [10, 2, 4, 5],
        [3, 7, 3, 7],
        [5, 1, 9, 12],
        [4, 2, 5, 12]
    ]
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(row)

def sum(matrix):
        total = 0
        for row in matrix:
            for value in row:
                total += value
        return total


values = create_matrix()
display_matrix(values)
print(sum(values))
