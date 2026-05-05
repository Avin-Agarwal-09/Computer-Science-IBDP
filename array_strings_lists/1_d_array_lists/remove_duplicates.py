items = [1, 2, 2, 3, 4, 3, 5]

result = []
for x in items:
    if x not in result:
        result.append(x)

print(result)
