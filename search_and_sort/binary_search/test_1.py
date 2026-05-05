def binarysearch(searchArray, left, right, searchTerm):
    searchArray = sorted(searchArray)
    while left<right:
        midpoint = left + (right-left)//2
        if searchArray[midpoint] == searchTerm:
            return midpoint
        elif searchArray[midpoint]<searchTerm:
            left = midpoint + 1
        else:
            right = midpoint - 1
    return -1

searchArray = [10,15,17,25,32,45,345,567,32,43,245,456,123,465,32,5643,1,567,342,765,987,223]
left = 0
right = len(searchArray)-1
searchTerm = int(input("Enter a number"))
print(binarysearch(searchArray, left, right, searchTerm))