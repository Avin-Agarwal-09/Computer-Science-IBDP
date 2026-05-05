f = open("numb.txt", "r")
lines = f.readlines()
f.close()

numbers = [0] * len(lines)
i = 0
for line in lines:
    line = line.replace("\n", "")
    if line != "":
        numbers[i] = int(line)
        i += 1
numbers = numbers[:i]

