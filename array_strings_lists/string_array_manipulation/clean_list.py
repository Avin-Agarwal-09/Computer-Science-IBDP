def clean_list(words):
    seen = set()
    result = []
    for word in reversed(words):
        if word not in seen:
            seen.add(word)
            result.append(word)
    return result[::-1]

words = ["apple", "banana", "apple", "orange", "banana"]
cleaned = clean_list(words)
print(cleaned)

