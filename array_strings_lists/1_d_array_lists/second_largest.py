def second_largest(scores):
    first = 0
    second = -1
    for i in range(len(scores)):
        if first < scores[i]:
            second = first
            first = scores[i]
    return second
scores = [45, 89, 67, 92, 78, 92]
print(second_largest(scores))
