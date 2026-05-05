def occurences(data,target):
    counter = 0
    for i in range(len(data)):
        if target == data[i]:
            counter += 1
    return counter
data = [1, 2, 2, 3, 2, 4, 2, 5]
target = 2
print(occurences(data,target))
