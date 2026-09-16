"""Topic 7 - Sorting algorithms.

                best        average/worst   stable   notes
bubble sort     O(n)        O(n^2)          yes      early-exit makes best case O(n)
selection sort  O(n^2)      O(n^2)          no       fewest swaps of the simple sorts
insertion sort  O(n)        O(n^2)          yes      excellent on nearly-sorted data
merge sort      O(n log n)  O(n log n)      yes      needs O(n) extra memory
quick sort      O(n log n)  O(n^2) worst    no       fastest in practice, sorts in place

All functions sort a COPY so the demo list below stays unsorted between calls.
"""


def bubble_sort(values):
    """Repeatedly swap adjacent out-of-order pairs; the largest 'bubbles' right."""
    values = values.copy()
    n = len(values)

    for i in range(n - 1):
        swapped = False
        # after i passes the last i elements are already in place
        for j in range(n - 1 - i):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
        if not swapped:          # early exit: nothing moved, so it is sorted
            break

    return values


def selection_sort(values):
    """Find the smallest remaining value and swap it into position i."""
    values = values.copy()
    n = len(values)

    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if values[j] < values[smallest]:
                smallest = j
        if smallest != i:
            values[i], values[smallest] = values[smallest], values[i]

    return values


def insertion_sort(values):
    """Take each value and slide it back into the sorted left-hand portion."""
    values = values.copy()

    for i in range(1, len(values)):
        current = values[i]
        j = i - 1
        while j >= 0 and values[j] > current:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = current

    return values


def merge_sort(values):
    """Divide and conquer: split in half, sort each half, merge them back."""
    if len(values) <= 1:
        return values.copy()

    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])
    return merge(left, right)


def merge(left, right):
    """Merge two already-sorted lists into one sorted list."""
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])      # whichever side still has values
    merged.extend(right[j:])
    return merged


def quick_sort(values):
    """Pick a pivot, partition around it, then sort each partition."""
    if len(values) <= 1:
        return values.copy()

    pivot = values[len(values) // 2]
    smaller = []
    equal = []
    larger = []

    for value in values:
        if value < pivot:
            smaller.append(value)
        elif value > pivot:
            larger.append(value)
        else:
            equal.append(value)

    return quick_sort(smaller) + equal + quick_sort(larger)


def bubble_sort_descending(values):
    values = values.copy()
    n = len(values)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if values[j] < values[j + 1]:    # only the comparison flips
                values[j], values[j + 1] = values[j + 1], values[j]
    return values


def count_swaps(values):
    """Instrumented bubble sort - a common exam question."""
    values = values.copy()
    swaps = 0
    passes = 0
    n = len(values)

    for i in range(n - 1):
        passes += 1
        swapped = False
        for j in range(n - 1 - i):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swaps += 1
                swapped = True
        if not swapped:
            break

    return swaps, passes


def is_sorted(values):
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True


if __name__ == "__main__":
    numbers = [29, 10, 14, 37, 14, 3]
    print("Unsorted:        ", numbers)
    print("bubble_sort:     ", bubble_sort(numbers))
    print("selection_sort:  ", selection_sort(numbers))
    print("insertion_sort:  ", insertion_sort(numbers))
    print("merge_sort:      ", merge_sort(numbers))
    print("quick_sort:      ", quick_sort(numbers))
    print("descending:      ", bubble_sort_descending(numbers))

    swaps, passes = count_swaps(numbers)
    print(f"bubble stats:     {swaps} swaps over {passes} passes")

    print("is_sorted(before):", is_sorted(numbers))
    print("is_sorted(after): ", is_sorted(bubble_sort(numbers)))

    words = ["pear", "apple", "kiwi", "banana"]
    print("strings sorted:  ", bubble_sort(words))
