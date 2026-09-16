ROOMNUMS = [2,216,15,109,156,120,93,18,21,56]

target = int(input("Enter target"))

def check(target,ROOMNUMS):
    found = False
    for i in range(len(ROOMNUMS)):
        if target == ROOMNUMS[i]:
            print(f"the student in room {target} has paid the bill")
            found = True
    if found == False:
        print(f"the student in room {target} has not paid the bill")

def sort(ROOMNUMS):
    n = len(ROOMNUMS)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if ROOMNUMS[j] < ROOMNUMS[j + 1]:
                temp = ROOMNUMS[j]
                ROOMNUMS[j] = ROOMNUMS[j + 1]
                ROOMNUMS[j + 1] = temp

    return ROOMNUMS

check(target,ROOMNUMS)
print(sort(ROOMNUMS))