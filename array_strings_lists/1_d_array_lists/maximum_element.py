def max(scores):
    highest = 0
    for i in range(len(scores)):
        if highest < scores[i]:
            highest = scores[i]
    return highest
scores=[85, 92, 78, 95, 88]
print(max(scores))
