def optimized_bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # swap elements
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True
        
        if swapped == True:
            break

    return arr

print(optimized_bubble_sort([1, 2, 3, 4]))
