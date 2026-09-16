#Write a function that calculates the average of all elements in a 2D array.

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
print(sum(values)/16)
