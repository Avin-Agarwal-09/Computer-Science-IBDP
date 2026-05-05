f = open("log.txt","r")
g = open("reports.txt","w")
logs = []

logging = f.readline()

while logging != "":
    y = logging
    if "\n" in y:
        y = str(y[:-1])
    else:
        y = str(y)
    logs.append(y)

    logging = f.readline()

distinct_logs = []
for i in range(len(logs)):
    if logs[i] in distinct_logs:
        continue
    distinct_logs.append(logs[i])

print("Distinct_logs: ",distinct_logs)

for i in range(len(distinct_logs)):
    counter = 0
    for j in range(len(logs)):
        if distinct_logs[i] == logs[j]:
            counter += 1
    final_string = distinct_logs[i] + ": " + str(counter)
    g.write(f"{final_string}\n")
    print(final_string)



f.close()
g.close()