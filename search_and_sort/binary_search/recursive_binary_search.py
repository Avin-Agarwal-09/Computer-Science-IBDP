books = ["23","45", "12"].sort()
low = 0
high = len(books)
target = int(input("Enter a target to be searched: "))

def recursiveSearch(books, target, low, high):
    mid = 0
    if low >= high:
        return -1
    else:
        mid = len(books) // 2
        if target < mid:
            high = mid - 1
        elif target > mid:
            low = mid +1
        elif target == mid:
            return mid
        return recursiveSearch(books, target, low, high)
        
print(recursiveSearch(books,target,low,high))

        
