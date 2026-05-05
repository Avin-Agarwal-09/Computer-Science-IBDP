#Write a program that reads a 3×3 matrix and calculates the sum of all odd elements of the array

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

def sum_odd(matrix):
        total = 0
        for row in matrix:
            for value in row:
                if value % 2 == 1:  
                    total += value
        return total


values = create_matrix()
display_matrix(values)
print(sum_odd(values))
