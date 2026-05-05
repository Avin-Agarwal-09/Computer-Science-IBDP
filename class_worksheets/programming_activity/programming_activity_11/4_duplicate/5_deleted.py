f = open("numb.txt", "r")
numbers = f.read().split()
f.close()

seen = set()
unique = []
for n in numbers:
    if n not in seen:
        unique.append(n)
        seen.add(n)

deleted = len(numbers) - len(unique)

f = open("numb.txt", "a")
for n in range(71, 71 + deleted):
    f.write(str(n) + "\n")
f.close()

print(f"Appended {deleted} numbers from 71 to {70 + deleted}")