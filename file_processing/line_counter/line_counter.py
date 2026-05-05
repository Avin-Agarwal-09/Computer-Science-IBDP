f = open("data.txt","r")
g = open("count.txt","w")

counter = 0

random = f.readline()
while random != "":
    counter += 1
    random = f.readline()

g.write(f"Number of lines: {counter}")

f.close()
g.close()