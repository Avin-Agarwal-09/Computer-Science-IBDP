def find_min(lst):

    if len(lst) == 1:
        return lst[0]
    if lst[0] < lst[1]:
        return find_min(lst)
    else:
        lst.pop(0)
        return find_min(lst)

n = [10,5,3,4,7,8]
print(find_min(n))
