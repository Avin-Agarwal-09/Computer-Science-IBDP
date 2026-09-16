from random import randint

f = open("numb.txt", "w")
for i in range(100):
    f.write(str(randint(1, 70)) + "\n")
f.close()
print("100 random numbers written to numb.txt")