RAINBOW = ["Blue", "E", "Green", "D", "Indigo", "F", "Orange", "B", "Red", "A", "Violet", "G", "Yellow", "C"]

COLOUR = []
ORDER = []

for i in range(0, len(RAINBOW), 2):
    COLOUR.append(RAINBOW[i])   
    ORDER.append(RAINBOW[i + 1])   

print("COLOUR:", COLOUR)
print("ORDER:", ORDER)


n = len(ORDER)

for i in range(n - 1):
    for j in range(0, n - i - 1):
        if ORDER[j] > ORDER[j + 1]:
            ORDER[j], ORDER[j + 1] = ORDER[j + 1], ORDER[j]
            COLOUR[j], COLOUR[j + 1] = COLOUR[j + 1], COLOUR[j]

print("Sorted ORDER:", ORDER)
print("Sorted COLOUR:", COLOUR)