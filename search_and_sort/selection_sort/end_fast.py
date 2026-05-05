def selection_sort(arr):
    n = len(arr)
    for i in range(n):
            sorted = True
            

            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
                elif arr[j] < arr[j-1]:
                     sorted = False
                     break
            if sorted:
                 break
                
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([1,2,3,4,5]))