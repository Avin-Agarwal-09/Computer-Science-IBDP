f = open("words.txt","r")
g = open("longest.txt","w")

longest = 0
longest_word = ""

random = f.readline()
while random != "":
    if len(random) > longest:
        longest_word = random
        longest = len(random)
    random = f.readline()

g.write(f"longest word: {longest_word}")

f.close()
g.close()