arr = [[1,2,3],[4,5,6]]
total = 0
counter = 0

for row in arr:
    for column in row:
        total += column
        counter += 1
        print(column)

print(total)
print(counter)
print(total/counter)
