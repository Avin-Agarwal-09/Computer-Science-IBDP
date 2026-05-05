f = open("students.txt","r")
g = open("results.txt","r")
h = open("honours.txt","w")

students = f.readline()
student_arr = []
while students != "":
    y = students.split(",")
    if "\n" in y[1]:
        y[1] = str(y[1][:-1])
    else:
        y[1] = str(y[1])
    student_arr.append(y)
    students = f.readline()
print(student_arr)

results = g.readline()
results_arr = []
while results != "":
    y = results.split(",")
    if "\n" in y[1]:
        y[1] = str(y[1][:-1])
    else:
        y[1] = str(y[1])
    results_arr.append(y)
    results = g.readline()
print(results_arr)

for i in range(len(student_arr)):
    if student_arr[i][0] == results_arr[i][0]:
        if int(results_arr[i][1]) >= 60:
            final_string = student_arr[i][1] + "," + results_arr[i][1]
            h.write(f"{final_string}\n")


f.close()
g.close()
h.close()