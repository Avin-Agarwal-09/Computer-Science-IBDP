def selection_sort(arr):
    n = len(arr)
    counter = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            counter +=1 
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print("number of comparisons are:", counter)
    return arr

print(selection_sort([4, 3, 2, 1]))