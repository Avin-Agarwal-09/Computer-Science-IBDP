def selection_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if arr[min_index] < arr[i]:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    print("number of swaps are:", swaps)

arr = [5, 4, 3, 2, 1]
print(selection_sort(arr))