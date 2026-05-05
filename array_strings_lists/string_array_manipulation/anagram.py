def anagrams(word1, word2):
    if len(word1) != len(word2):
        return False
    for char in word1:
        if word1.count(char) != word2.count(char):
            return False
    return True

word1 = "apple"
word2 = "peach"
print(anagrams(word1, word2))