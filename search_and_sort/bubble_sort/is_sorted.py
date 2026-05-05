def is_sorted(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] < arr[i+1]:
            pass
        else:
            return False
    return True

print(is_sorted([1,2,3]))
