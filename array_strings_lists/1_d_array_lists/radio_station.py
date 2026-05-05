station = [0,1,2,3,4,5]
radio = [100.4,90.2,104.5,93.8,106.2]
max = 0
min = 100000

for i in range(len(radio)):
    if radio[i] > max:
        max = radio[i]
    if radio[i] < min:
        min = radio[i]
print(max-min)