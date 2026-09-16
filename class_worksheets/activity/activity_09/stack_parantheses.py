import stacks_functions

def are_parentheses_matched(s):
    stacks_functions.Stack = [0] * stacks_functions.StackSize
    stacks_functions.topIndex = -1

    for char in s:
        if char == "(":
            stacks_functions.push(char)
        elif char == ")":
            if stacks_functions.pop() is None:
                return False
    
    return stacks_functions.isEmpty()

testString1 = "((()))"      
testString2 = "(()"

print(testString1, "->", "Matched" if are_parentheses_matched(testString1) else "Not Matched")
print(testString2, "->", "Matched" if are_parentheses_matched(testString2) else "Not Matched")