def bubble_sort_limited(arr,x):
    n = len(arr)

    for i in range(x):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # swap elements
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr

print(bubble_sort_limited([5, 4, 3, 2, 1], 2))

