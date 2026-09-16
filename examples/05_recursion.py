"""Topic 5 - Recursion.

Every recursive function needs two parts:
  base case      - a stopping condition that returns without recursing
  recursive case - calls itself on a SMALLER version of the problem

Without a base case the calls never stop and Python raises RecursionError.
"""


def factorial(n):
    if n <= 1:              # base case
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Naive recursion: clear, but recalculates the same terms many times."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def count_vowels(text):
    if text == "":
        return 0
    first = 1 if text[0].lower() in "aeiou" else 0
    return first + count_vowels(text[1:])


def is_palindrome(text):
    """Shrink from both ends: if the outer pair matches, check the inside."""
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


def count_occurrences(values, target):
    if len(values) == 0:
        return 0
    first = 1 if values[0] == target else 0
    return first + count_occurrences(values[1:], target)


def find_minimum(values):
    if len(values) == 1:
        return values[0]
    rest_minimum = find_minimum(values[1:])
    if values[0] < rest_minimum:
        return values[0]
    return rest_minimum


def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


if __name__ == "__main__":
    print("factorial(6):       ", factorial(6))
    print("fibonacci(10):      ", fibonacci(10))
    print("sum_digits(9271):   ", sum_digits(9271))
    print("count_vowels:       ", count_vowels("recursion"))
    print("is_palindrome:      ", is_palindrome("racecar"))
    print("count_occurrences:  ", count_occurrences([1, 3, 3, 7, 3], 3))
    print("find_minimum:       ", find_minimum([9, 2, 7, 4]))
    print("power(2, 10):       ", power(2, 10))
