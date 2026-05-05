def largest_after_one_pass(arr):
    n = len(arr)

    for j in range(n-1):
        if arr[j] > arr[j + 1]:
            # swap elements
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
    return arr

print(largest_after_one_pass([2, 3, 1]))

