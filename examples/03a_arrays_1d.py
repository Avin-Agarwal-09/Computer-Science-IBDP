"""Topic 3a - One dimensional arrays and lists.

The standard traversal patterns. Each is written with explicit loops rather
than built-ins (sum, max, min) because the loop is the examinable part.
"""


def total(numbers):
    running = 0
    for value in numbers:
        running += value
    return running


def average(numbers):
    if len(numbers) == 0:
        return 0
    return total(numbers) / len(numbers)


def largest(numbers):
    """Assume the first element is the largest, then correct as you traverse."""
    biggest = numbers[0]
    for value in numbers:
        if value > biggest:
            biggest = value
    return biggest


def smallest(numbers):
    lowest = numbers[0]
    for value in numbers:
        if value < lowest:
            lowest = value
    return lowest


def second_largest(numbers):
    """Track the top two in a single pass, ignoring duplicates of the largest."""
    biggest = second = None
    for value in numbers:
        if biggest is None or value > biggest:
            second = biggest
            biggest = value
        elif value != biggest and (second is None or value > second):
            second = value
    return second


def count_occurrences(numbers, target):
    count = 0
    for value in numbers:
        if value == target:
            count += 1
    return count


def filter_even(numbers):
    evens = []
    for value in numbers:
        if value % 2 == 0:
            evens.append(value)
    return evens


def reverse(numbers):
    """Build a new list by inserting each element at the front."""
    reversed_list = []
    for value in numbers:
        reversed_list.insert(0, value)
    return reversed_list


def remove_duplicates(numbers):
    """Keep the first occurrence of each value, preserving order."""
    seen = []
    for value in numbers:
        if value not in seen:
            seen.append(value)
    return seen


def frequency(values):
    counts = {}
    for value in values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts


if __name__ == "__main__":
    numbers = [4, 8, 15, 16, 23, 42, 8]

    print("List:              ", numbers)
    print("Total:             ", total(numbers))
    print("Average:           ", average(numbers))
    print("Largest:           ", largest(numbers))
    print("Smallest:          ", smallest(numbers))
    print("Second largest:    ", second_largest(numbers))
    print("Occurrences of 8:  ", count_occurrences(numbers, 8))
    print("Evens:             ", filter_even(numbers))
    print("Reversed:          ", reverse(numbers))
    print("Duplicates removed:", remove_duplicates(numbers))
    print("Frequency:         ", frequency(numbers))
