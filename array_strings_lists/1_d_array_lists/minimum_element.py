def min(temperatures):
    minimum = 10000
    for i in range(len(temperatures)):
        if minimum > temperatures[i]:
            minimum = temperatures[i]
    return minimum
temperatures = [15, 8, 22, 5, 18, 3]
print(min(temperatures))
