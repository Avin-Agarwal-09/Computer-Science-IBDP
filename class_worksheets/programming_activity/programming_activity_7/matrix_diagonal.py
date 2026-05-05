def create_matrix():
    matrix = [
        [10, 2, 4],
        [3, 7, 3],
        [5, 1, 9]
    ]
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(row)

def diagonal_matrix(matrix):
    total = 0
    for i in range(3):
        total += matrix[i][i]
    return total

def other_diagonal(matrix):
    total = 0
    for i in range(3):
        total += matrix[i][2 - i]
    return total

values = create_matrix()
display_matrix(values)
print(diagonal_matrix(values))
print(other_diagonal(values))
