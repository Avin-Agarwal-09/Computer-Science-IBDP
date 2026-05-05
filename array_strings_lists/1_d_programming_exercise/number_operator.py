value = int(input("Enter a number"))
list = [0 for i in range(value)]
sum_even = 0
avg = 0
total = 0
odd_count = 0
for i in range(value):
    list[i] = int(input("Enter a number"))
    if total % 2 == 0:
        sum_even += list[i]
    else:
        odd_count +=1
    total+=list[i]

print("Sum of even numbers",sum_even)
print("average:",total/value)
print("odd",odd_count)
