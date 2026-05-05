def position_after_one_pass(arr,x):
    n = len(arr)
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
    return arr.index(x)
    
print(position_after_one_pass([3, 2, 1], 2))
