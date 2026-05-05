def search_insert_position(array,target):
    low = 0
    high = len(array)
    while low<high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low

array = [1,3,5,6]
target = 7

print(search_insert_position(array,target))