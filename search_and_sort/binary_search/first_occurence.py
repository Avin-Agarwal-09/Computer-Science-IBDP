def first_occurrence(array,target):

    low = 0
    high = len(array)-1
    result = -1

    while low<=high:
        mid = (low + high) // 2
        if array[mid] == target:
            result = mid
            high = mid -1
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

print(first_occurrence([1,3,5,6], 7))
