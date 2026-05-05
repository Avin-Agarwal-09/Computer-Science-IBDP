f = open("marks.txt","r")
g = open("above_avg.txt","w")


random = f.readline()
total = 0
counter = 0
average = 0
marks = []

while random != "":
    if "\n" in random:
        marks.append(int(random[:-1]))
        total += (int(random[:-1]))
        counter += 1
    else:
        marks.append(int(random))
        total += (int(random))
        counter += 1

    random = f.readline()

average = total / counter

for i in range(len(marks)):
    if marks[i] > average:
        g.write(f"{str(marks[i])}\n")



f.close()
g.close()