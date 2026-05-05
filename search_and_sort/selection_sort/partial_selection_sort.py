def selection_sort(arr,swaps):
    n = len(arr)
    for i in range(swaps):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([7, 6, 5, 4, 3], 2))