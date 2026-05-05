def bubble_sort_evens(arr):
    even_arr = []
    indices_arr = []
    n = len(arr)

    for i in range(n):
        if arr[i] % 2 == 0:
            even_arr.append(arr[i])
            indices_arr.append(i)

    m = len(even_arr)
    for i in range(m-1):
        for j in range(m - 1 - i):
                if even_arr[j] > even_arr[j + 1]:
                    # swap elements
                    temp = even_arr[j]
                    even_arr[j] = even_arr[j + 1]
                    even_arr[j + 1] = temp

    counter = 0 
    for i in range(n):
         if arr[i] % 2 == 0:
              arr[i] = even_arr[counter]
              counter += 1
              

    return arr

print(bubble_sort_evens([5, 2, 3, 8, 1, 4]))
