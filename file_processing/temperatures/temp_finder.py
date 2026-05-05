f = open("temperatures.txt","r")
g = open("stats.txt","w")

max_temp = -100
min_temp = 100
total = 0
counter = 0

random = f.readline()
while random != "":

    temperature = int(random)
    if temperature > max_temp:
        max_temp = temperature
    if temperature < min_temp:
        min_temp = temperature
    total += temperature
    counter += 1

    random = f.readline()
  
avg = round(total/counter,1)
max_temp = round(max_temp,1)
min_temp = round(min_temp,1)

g.write(f"Max Temperature: {max_temp}\n")
g.write(f"Min Temperature: {min_temp}\n")
g.write(f"Average Temperature: {avg}\n")

f.close()
g.close()
