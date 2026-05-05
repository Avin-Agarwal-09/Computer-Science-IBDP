def selection_sort(arr):
    n = len(arr)
    indices = []
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
            
        arr[i], arr[min_index] = arr[min_index], arr[i]
        indices.append(min_index) 
    return indices

print(selection_sort([20, 12, 10, 15, 2]))