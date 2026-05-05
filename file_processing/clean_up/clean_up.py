f = open("raw.txt","r")
g = open("clean.txt","w")

random = f.readline()


while random != "":
    if random != "\n":
        g.write(random)

    random = f.readline()

f.close()
g.close()