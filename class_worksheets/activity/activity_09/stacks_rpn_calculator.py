import stacks_functions

word = input("Enter a operation: ")
stacks_functions.StackSize = len(word.replace(" ", ""))
stacks_functions.Stack = [0] * stacks_functions.StackSize
stacks_functions.topIndex = -1

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
        stacks_functions.push(curr_string)
        curr_string = ""
    elif word[i] in operator:
        number2 = stacks_functions.pop()
        number1 = stacks_functions.pop()
        final_value = math_operations(number1,number2,word[i])
        stacks_functions.push(final_value)
    else:
        curr_string = curr_string + word[i]

print("Answer: ",stacks_functions.Stack[stacks_functions.topIndex] )
