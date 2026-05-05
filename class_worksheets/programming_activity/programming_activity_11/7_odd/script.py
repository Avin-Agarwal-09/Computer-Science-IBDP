f = open("numb.txt", "r")
numbers = f.read().split()
f.close()

odd = []
for n in numbers:
    if int(n) % 2 != 0:
        odd.append(n)

f = open("odd.txt", "w")
for n in odd:
    f.write(n + "\n")
f.close()

print(f"Odd numbers found: {len(odd)}")
print(odd)