"""Topic 4 - String manipulation.

Strings are immutable sequences: you can index and slice them, but every
"change" actually builds a new string.
"""

VOWELS = "aeiou"


def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text


def is_palindrome(text):
    """Compare only letters, ignoring case and punctuation."""
    cleaned = ""
    for char in text.lower():
        if char.isalnum():
            cleaned += char
    return cleaned == reverse_string(cleaned)


def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in VOWELS:
            count += 1
    return count


def analyse_sentence(sentence):
    """Word count, longest word, and words that start with a vowel."""
    words = sentence.split()

    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    vowel_starters = 0
    for word in words:
        if word and word[0].lower() in VOWELS:
            vowel_starters += 1

    return len(words), longest_word, vowel_starters


def word_frequency(sentence):
    counts = {}
    for word in sentence.lower().split():
        word = word.strip(".,!?")
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def most_common_word(sentence):
    counts = word_frequency(sentence)
    best_word = ""
    best_count = 0
    for word, count in counts.items():
        if count > best_count:
            best_word = word
            best_count = count
    return best_word, best_count


def is_anagram(first, second):
    """Two strings are anagrams if their letters have identical frequencies."""
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()
    if len(first) != len(second):
        return False
    return sorted(first) == sorted(second)


def count_substring(text, target):
    """Count overlapping occurrences by sliding a window along the string."""
    count = 0
    for i in range(len(text) - len(target) + 1):
        if text[i:i + len(target)] == target:
            count += 1
    return count


def capitalise_words(sentence):
    result = []
    for word in sentence.split():
        result.append(word[0].upper() + word[1:].lower())
    return " ".join(result)


if __name__ == "__main__":
    print("Reversed:       ", reverse_string("computer"))
    print("Palindrome:     ", is_palindrome("A man, a plan, a canal: Panama"))
    print("Not palindrome: ", is_palindrome("computer science"))
    print("Vowels:         ", count_vowels("Object Oriented Programming"))

    words, longest, vowel_starters = analyse_sentence("the quick brown fox ate an apple")
    print(f"Analysis:        {words} words, longest '{longest}', {vowel_starters} vowel-initial")

    print("Most common:    ", most_common_word("the cat sat on the mat, the end"))
    print("Anagram:        ", is_anagram("listen", "silent"))
    print("'ss' in Mississippi:", count_substring("Mississippi", "ss"))
    print("Capitalised:    ", capitalise_words("hELLo wORLD again"))
