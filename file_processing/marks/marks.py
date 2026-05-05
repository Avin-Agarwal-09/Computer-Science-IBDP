f = open("marks.txt","r")
marks = f.readline()
marks_total = 0
student_count = 0
x=0
while marks != "":
    print(marks)
    if "/n" in marks:
        x = int(marks[:-1])
        print(x)
    else:
        x = int(marks)
    marks_total += x
    student_count += 1
    marks = f.readline()

average = marks_total/student_count
rounded_average = f"{average:.2f}"
print("average is:", rounded_average)
print("student count", student_count)

f.close()

g = open("summary.txt","w")

g.write(f"Number of students: {student_count}\n")
g.write(f"Average of marks is: {rounded_average}")
g.close()