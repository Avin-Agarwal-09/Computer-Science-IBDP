def search(fruits,target):
    for i in range(len(fruits)):
        if fruits[i] == target:
            return i
    else:
        return -1
fruits = ['apple', 'banana', 'orange', 'grape']
target = 'orange'
print(search(fruits,target))