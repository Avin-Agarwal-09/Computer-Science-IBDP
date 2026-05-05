value = "Julian"

StackSize = len(value)
Stack = [None] * StackSize
topIndex = -1

def isEmpty():
    return topIndex == -1

def isFull():
    return topIndex == StackSize - 1

def push(char):
    global topIndex
    if not isFull():
        topIndex += 1
        Stack[topIndex] = char

def pop():
    global topIndex
    if not isEmpty():
        char = Stack[topIndex]
        topIndex -= 1
        return char
    return None


for char in value:
    push(char)

reversed_name = ""
while not isEmpty():
    reversed_name += pop()

print("Reversed name:", reversed_name)
