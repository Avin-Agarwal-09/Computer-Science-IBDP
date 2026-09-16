print("This is a calculator Enter first Integer")
FirstInteger = int(input())
print("This is a calculator Enter second Integer")
SecondInteger = int(input())
print("what function do you want to run")
function = input()
if function == "add":
   print(FirstInteger + SecondInteger)
elif function == "sub":
   print(FirstInteger - SecondInteger)
elif function == "mul":
   print(FirstInteger * SecondInteger)
elif function == "div":
   print(FirstInteger / SecondInteger)
