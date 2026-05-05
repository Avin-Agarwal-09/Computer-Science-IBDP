def findSearch(productID,target):
    Count = 0
    while Count != -1:
        if productID[Count]==target:
            return Count
        elif Count == len(productID):
            return -1
            Count = -1
        else:
            Count += 1

productID = [10,4,15,30]
target = 15
print(findSearch(productID,target))