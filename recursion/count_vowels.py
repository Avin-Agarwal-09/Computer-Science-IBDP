def count_vowels(word):
    if not word:
        return 0
    return (1 if word[0] in 'aeiou' else 0) + count_vowels(word[1:])

word = str(input("Enter a word"))
print(count_vowels(word))