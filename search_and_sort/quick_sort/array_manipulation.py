

# partition function
def partition(arr, low, high):
    
    # choose the pivot
    pivot = arr[high]
    
    # index of smaller element and indicates 
    # the right position of pivot found so far
    i = low - 1
    
    # traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to 
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    # move pivot after smaller elements and
    # return its position
    swap(arr, i + 1, high)
    return i + 1

# swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# the QuickSort function implementation
def quickSort(arr, low, high):
    if low < high:
        
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)
        
        # recursion calls for smaller elements
        # and greater or equals elements
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def even_only(arr):
    new_arr = []
    index_arr = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            new_arr.append(arr[i])
            index_arr.append(i)
    return new_arr, index_arr

arr = [9,4,7,2,6,5]
print(even_only(arr))
even_arr, index_arr = even_only(arr)
low = 0
high = len(even_arr) - 1
print(quickSort(even_arr,low,high))
print(even_arr)

counter = 0
for i in range(len(arr)):
    if i in index_arr:
        arr[i] = even_arr[counter]
        counter += 1


print(arr)

