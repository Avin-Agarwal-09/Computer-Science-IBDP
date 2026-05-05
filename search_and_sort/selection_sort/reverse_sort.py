def selection_sort(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        max_index = i
        for j in range(0, i+1):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

print(selection_sort([10,13,2,5,3,6]))
