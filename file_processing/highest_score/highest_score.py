f = open("scores.txt","r")
g = open("ranking.txt","w")

students = []

random = f.readline()

while random != "":

    y = random

    if "\n" in y:
        y = (y[:-1])

    name, score = y.split(",")
    students.append([name,int(score)])

    random = f.readline()

print(students)


temp_student = ""

for i in range(len(students)):
    for j in range(len(students)-1):
        if students[j][1] < students [j+1][1]:
            temp_student = students[j]
            students[j] = students[j+1]
            students[j+1] = temp_student

for i in range(len(students)):
    g.write(f"{students[i][0]},{str(students[i][1])}\n")

f.close()
g.close()