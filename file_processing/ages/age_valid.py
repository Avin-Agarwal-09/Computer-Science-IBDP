f = open("ages.txt","r")
g = open("valid_ages.txt","w")

age = 0
random = f.readline()
while random != "":
    try:
        age = int(random)
        if age >= 0 and age <= 120:
            g.write(f"{age}\n")
            print(age)
    except:
        random = f.readline()
        continue
    random = f.readline()
    

f.close()
g.close()
