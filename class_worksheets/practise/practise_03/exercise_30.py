def numbers(k):
  for i in range(1, k + 1):
    for j in range(k - i + 1):
      print(i, end=" ")
    print()

value = int(input("Enter a number: "))
numbers(value)