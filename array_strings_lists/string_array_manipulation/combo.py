def analyse_sentence(sentence):
    words = sentence.split()
    vowels = "aeiouAEIOU"
    total_words = len(words)
    longest_word = ""
    for word in words:
        if len(word)> len(longest_word):
            longest_word = word
    vowel_count = 0
    for word in words:
        if word and word[0] in vowels:
            vowel_count = vowel_count +1
    return total_words, longest_word, vowel_count

sentence = str(input("Enter a sentence"))
print(analyse_sentence(sentence))