try:
    f = open("counter.txt", "r")
    count = int(f.read())
    f.close()
except FileNotFoundError:
    count = 0

count += 1
f = open("counter.txt", "w")
f.write(str(count))
f.close()
print("This program has run " + str(count) + " times.") 