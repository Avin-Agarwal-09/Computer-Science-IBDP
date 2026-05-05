arr = [
    [10,3,7,4],
    [2,18,6,1],
    [9,5,12,8],
    [14,11,13,0]
]

largest = 0

for row in arr:
    for column in row:
        if column > largest:
            largest = column
print(largest)