def countStudents(students, sandwiches):
    rounds = 0
    while students and rounds < len(students):
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            rounds = 0
        else:
            students.append(students.pop(0))
            rounds = rounds + 1
    return len(students)

students = [0, 1, 0, 1, 0]
sandwiches = [1, 1, 0, 0, 0]
print(countStudents(students,sandwiches))

