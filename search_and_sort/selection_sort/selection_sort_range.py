def selection_sort_range(arr,start,end):
    n = len(arr)
    for i in range(start,end+1):
        min_index = i
        for j in range(i + 1, end+1):
            if arr[4, 3, 2, 1][j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort_range([9, 8, 7, 6, 5, 4], 1, 4)) 