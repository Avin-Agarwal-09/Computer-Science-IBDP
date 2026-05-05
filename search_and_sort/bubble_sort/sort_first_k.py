def bubble_sort_first_k(arr,k):

    for i in range(k - 1):
        for j in range(k - 1 - i):
            if arr[j] > arr[j + 1]:
                # swap elements
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr

print(bubble_sort_first_k([8, 6, 7, 5], 2))
