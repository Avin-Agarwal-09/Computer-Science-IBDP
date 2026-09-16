sentence = "the cat sat on the mat"
words = sentence.split()
print("Total words:", len(words))
most = ""
highest = 0
for w in words:
    count = words.count(w)
    print(w, "=", count)
    if count > highest:
        highest = count
        most = w
print("Most frequent word:", most)
