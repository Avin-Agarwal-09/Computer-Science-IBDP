#Create a 2D array, 3x3 and move the smallest value in each row to the first column

numbers = [[10,5,3],
           [34,6,8],
           [2,5,8]
]

def move_smallest_to_first(numbers):
    for i in range(3):
        min_index = 0
        for j in range(1, 3):
            if numbers[i][j] < numbers[i][min_index]:
                min_index = j

 
        numbers[i][0], numbers[i][min_index] = numbers[i][min_index], numbers[i][0]

    return numbers

new_numbers = move_smallest_to_first(numbers)
for i in new_numbers:
    print(i)

    