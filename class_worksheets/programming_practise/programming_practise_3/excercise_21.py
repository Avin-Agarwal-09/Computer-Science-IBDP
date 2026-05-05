print("Enter a number")
Number = input()
OppNumber = ""
for i in range(0, len(Number)):
   OppNumber = OppNumber + Number[len(Number) - i - 1]
print(OppNumber)

