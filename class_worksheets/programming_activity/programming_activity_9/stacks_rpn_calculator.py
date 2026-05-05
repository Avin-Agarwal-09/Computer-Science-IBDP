import Stacks_Functions

word = input("Enter a operation: ")
Stacks_Functions.StackSize = len(word.replace(" ", ""))
Stacks_Functions.Stack = [0] * Stacks_Functions.StackSize
Stacks_Functions.topIndex = -1

def math_operations(num1, num2, operation):
    if operation == "+":
        return int(num1) + int(num2)
    elif operation == "-":
        return int(num1) - int(num2)
    elif operation == "*":
        return int(num1) * int(num2)
    elif operation == "/":
        return int(num1) / int(num2)
    elif operation == "**":
        return int(num1) ** int(num2)
    
curr_string = ""
operator = ["+","-","*","/","**"]

for i in range(len(word)):

    if word[i] == " " and curr_string != "":
        Stacks_Functions.push(curr_string)
        curr_string = ""
    elif word[i] in operator:
        number2 = Stacks_Functions.pop()
        number1 = Stacks_Functions.pop()
        final_value = math_operations(number1,number2,word[i])
        Stacks_Functions.push(final_value)
    else:
        curr_string = curr_string + word[i]

print("Answer: ",Stacks_Functions.Stack[Stacks_Functions.topIndex] )
