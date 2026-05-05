f = open("scores.txt","r")
g = open("distinction.txt","w")
h = open("pass.txt","w")
i = open("fail.txt","w")

student_arr = []

random = f.readline()
while random != "":
    print(random)
    student_id,score = random.split(",")
    if "\n" in score:
        score = int(score[:-1])
    else:
        score = int(score)
    print(score)

    if score >= 70:
        g.write(f"{student_id}\n")
    if score > 50 and score < 69:
        h.write(f"{student_id}\n")
    if score < 50:
        i.write(f"{student_id}\n")

    random = f.readline()

print(student_arr)

f.close()
g.close()
h.close()
i.close()