import Stacks_Functions

def are_parentheses_matched(s):
    Stacks_Functions.Stack = [0] * Stacks_Functions.StackSize
    Stacks_Functions.topIndex = -1

    for char in s:
        if char == "(":
            Stacks_Functions.push(char)
        elif char == ")":
            if Stacks_Functions.pop() is None:
                return False
    
    return Stacks_Functions.isEmpty()

testString1 = "((()))"      
testString2 = "(()"

print(testString1, "->", "Matched" if are_parentheses_matched(testString1) else "Not Matched")
print(testString2, "->", "Matched" if are_parentheses_matched(testString2) else "Not Matched")