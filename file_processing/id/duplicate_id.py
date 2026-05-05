f = open("ids.txt","r")
g = open("duplicates.txt","w")

seen = []

random = f.readline()
while random != "":
    print(seen)
    y = random
    if "\n" in y:
        y = str(y[:-1])
    else:
        y = str(y)

    if y in seen:
        g.write(f"{y}\n")
    else:
        seen.append(y)
    random = f.readline()

f.close()
g.close()