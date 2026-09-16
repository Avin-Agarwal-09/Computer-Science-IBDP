# Sample DATA array (assumed to be pre-inputted)
DATA = [15, 3, 22, 8, 47, 31, 6, 19, 42, 11]
N = len(DATA)

for i in range(N - 1):
    for j in range(0, N - i - 1):
        if DATA[j] > DATA[j + 1]:
            DATA[j], DATA[j + 1] = DATA[j + 1], DATA[j]

if N % 2 != 0:
    median = DATA[N // 2]
else:
    mid1 = DATA[(N // 2) - 1]
    mid2 = DATA[N // 2]
    median = (mid1 + mid2) / 2

print("Sorted DATA:", DATA)
print("N =", N)
print("Median =", median)