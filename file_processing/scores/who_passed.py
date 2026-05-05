f = open("scores.txt","r")
g = open("passed.txt",'w')
scores = f.readline()
x = []
while scores != "":
    y = scores.split(",")
    
    if "\n" in y[1]:
        y[1] = int(y[1][:-1])
    else:
        y[1] = int(y[1])
    scores = f.readline()
    x.append(y)
print(x)
for i in range(len(x)):
    if x[i][1] >= 50:
        g.write(f"{x[i][0]},{x[i][1]}\n")
   

f.close()