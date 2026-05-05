data = ['a', 'b', 'a', 'c', 'b', 'a']

freq = {}
for item in data:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print(freq)
