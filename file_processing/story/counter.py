f = open("story.txt","r")
g = open("count.txt","w")

random = f.readline()
count = 0


while random != "":
    sentence = random.split()
    for word in sentence:
        if "\n" in word:
            word = word[:-1]
            if word == "the":
                count += 1
        else:
            if word == "the":
                count += 1

    random = f.readline()

g.write(str(count))


f.close()
g.close()


# while random != "":
#     sentence = random.split(" ")
#     for word in sentence:
#         if word == "the" or word == "the\n":
#             count += 1
#     random = f.readline()