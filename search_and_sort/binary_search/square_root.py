def square_root(x):
    if x < 2:
        return x
    
    low = 0
    high = x

    while low<=high:
        mid = (low + high) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
            
x = int(input("Enter a number"))
print("The square root of",x,"is:",square_root(x))