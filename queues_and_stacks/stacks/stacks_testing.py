StackSize = 5
Stack = [0] * StackSize
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

def peek():
    if isEmpty():
        print("Stack Underflow")
        return None
    else:
        return Stack[topIndex]

push("A")
push("B")
push("C")

print("isEmpty:",isEmpty())

print("isFull", isFull())

print("push:", push("D"))

print("pop:",pop())

print("Peek:",peek())