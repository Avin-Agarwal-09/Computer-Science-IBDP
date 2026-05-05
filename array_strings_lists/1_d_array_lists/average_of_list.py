def average(grades):
    total = 0
    for i in range(len(grades)):
        total = total + grades[i]
    return total/len(grades)
grades = [85, 90, 78, 92, 88]
print(average(grades))