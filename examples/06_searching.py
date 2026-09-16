"""Topic 6 - Searching algorithms.

linear search - works on ANY list, checks each element in turn      O(n)
binary search - needs a SORTED list, halves the range each step     O(log n)

Binary search is faster but sorting first costs more than one linear search,
so linear search wins for a single lookup on unsorted data.
"""


def linear_search(values, target):
    """Return the index of target, or -1 if it is absent."""
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1


def binary_search(values, target):
    """Iterative binary search. The list must already be sorted."""
    low = 0
    high = len(values) - 1

    while low <= high:
        mid = (low + high) // 2
        if values[mid] == target:
            return mid
        elif values[mid] < target:
            low = mid + 1        # target is in the upper half
        else:
            high = mid - 1       # target is in the lower half

    return -1


def recursive_binary_search(values, target, low=0, high=None):
    if high is None:
        high = len(values) - 1

    if low > high:               # base case: range is empty
        return -1

    mid = (low + high) // 2
    if values[mid] == target:
        return mid
    elif values[mid] < target:
        return recursive_binary_search(values, target, mid + 1, high)
    else:
        return recursive_binary_search(values, target, low, mid - 1)


def first_occurrence(values, target):
    """When duplicates exist, keep searching left after a match."""
    low = 0
    high = len(values) - 1
    found = -1

    while low <= high:
        mid = (low + high) // 2
        if values[mid] == target:
            found = mid
            high = mid - 1       # a match may still lie further left
        elif values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return found


def search_insert_position(values, target):
    """Where target is, or where it would go to keep the list sorted."""
    low = 0
    high = len(values) - 1

    while low <= high:
        mid = (low + high) // 2
        if values[mid] == target:
            return mid
        elif values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low


def integer_square_root(n):
    """Binary search over the answer space rather than over a list."""
    low = 0
    high = n
    best = 0

    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            best = mid
            low = mid + 1
        else:
            high = mid - 1

    return best


if __name__ == "__main__":
    unsorted = ["apple", "pear", "banana", "kiwi"]
    print("linear_search 'banana':  ", linear_search(unsorted, "banana"))
    print("linear_search 'mango':   ", linear_search(unsorted, "mango"))

    sorted_values = [2, 4, 4, 4, 9, 13, 21, 30]
    print("binary_search 13:        ", binary_search(sorted_values, 13))
    print("recursive_binary 21:     ", recursive_binary_search(sorted_values, 21))
    print("first_occurrence 4:      ", first_occurrence(sorted_values, 4))
    print("insert position for 10:  ", search_insert_position(sorted_values, 10))
    print("integer_square_root(50): ", integer_square_root(50))
