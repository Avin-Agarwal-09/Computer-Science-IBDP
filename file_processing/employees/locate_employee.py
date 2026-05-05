f = open("employees.txt","r")
g = open("results.txt","w")

employee_id = str(input("What employee ID do you want: "))
employee_arr = []

random = f.readline()
while random != "":
    y = random
    if "\n" in y:
        y = str(y[:-1])
    else:
        y = str(y)
    y = y.split(",")
    if y[0] == employee_id:
        g.write(f"{y[1]}\n")
    else:
        g.write(f"doesnt exist\n")
    employee_arr.append(y)
    random = f.readline()

print(employee_arr)

f.close()
g.close()