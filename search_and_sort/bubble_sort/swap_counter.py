def bubble_sort_swap_count(arr):
    n = len(arr)
    counter = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # swap elements
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                counter += 1

    return arr,counter

print(bubble_sort_swap_count([1, 2, 3]))

