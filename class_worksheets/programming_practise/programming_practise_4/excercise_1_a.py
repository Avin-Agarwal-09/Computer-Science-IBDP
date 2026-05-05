str1 = str(input("Enter a string: "))
print("Original String is", str1)
res = str1[0]
length = len(str1)
middle = int(length / 2)
res = res + str1[middle]
res = res + str1[length - 1]
print("New String:", res)