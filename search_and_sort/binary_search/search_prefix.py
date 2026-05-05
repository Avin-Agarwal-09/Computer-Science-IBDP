def search_prefix(array,target):

    array = sorted(array)
    low = 0
    high = len(array)-1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if array[mid].startswith(target):
            result = mid
            high = mid -1
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

target = "band"
array = ["apple", "application", "banana", "band", "bandage", "cat"]


print(search_prefix(array,target))