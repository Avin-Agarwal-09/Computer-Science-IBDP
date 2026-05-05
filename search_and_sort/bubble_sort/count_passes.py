def bubble_sort_with_passes(arr):
    n = len(arr)
    counter = 0

    for i in range(n - 1):
        counter += 1
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # swap elements
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return counter, arr


print(bubble_sort_with_passes([4, 3, 2, 1]))
