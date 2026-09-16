StackSize = 7
Stack = [None] * StackSize
topIndex = -1

def isEmpty():
    global topIndex
    return topIndex == -1

def isFull():
    global topIndex
    return topIndex == StackSize - 1

def push(value):
    global topIndex
    if isFull():
        print("Stack overflow")
    else:
        topIndex += 1
        Stack[topIndex] = value
        print("Element Pushed",value)

def peek():
    if isEmpty():
        print("Stack Underflow")
        return None
    else:
        return Stack[topIndex]

def pop():
    global topIndex
    if isEmpty():
        print("Stack Underflow")
        return None
    else:
        value = Stack[topIndex]
        Stack[topIndex] = 0
        topIndex -= 1
        return value


for i in range(5):
    push(input("Please enter a word: "))

print("peek:",peek())

for i in range(2):
    print("pop:", pop())

print("peek after popping:", peek())

