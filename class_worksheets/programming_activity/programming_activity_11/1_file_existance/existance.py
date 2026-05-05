try:
    f = open("name.txt", "r")
    name = f.read().strip()
    f.close()
    print("Hello, " + name)
except FileNotFoundError:
    name = input("What is your name? ")
    f = open("name.txt", "w")
    f.write(name)
    f.close()
    print("Nice to meet you, " + name + "!")