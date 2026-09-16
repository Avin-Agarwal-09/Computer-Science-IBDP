"""Topic 8 - Abstract data types: stacks and queues.

stack - LIFO (last in, first out).  push / pop / peek / isEmpty / isFull
queue - FIFO (first in, first out). enqueue / dequeue / peek / isEmpty / isFull

An ADT is defined by its OPERATIONS, not its implementation. Both classes
below store their data in a fixed-size array, as IB pseudocode expects.
"""


class Stack:
    def __init__(self, size=5):
        self.size = size
        self.items = [None] * size
        self.top = -1            # -1 means empty

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

    def push(self, value):
        if self.isFull():
            print("Stack overflow")
            return False
        self.top += 1
        self.items[self.top] = value
        return True

    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
            return None
        value = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        """Look at the top without removing it."""
        if self.isEmpty():
            return None
        return self.items[self.top]


class CircularQueue:
    """A circular queue reuses the space freed by dequeue.

    A linear queue wastes it: once rear reaches the end the queue reports
    full even though the front slots are empty. Wrapping with % fixes that.
    """

    def __init__(self, size=5):
        self.size = size
        self.items = [None] * size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        if self.isFull():
            print("Queue overflow")
            return False
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.items[self.rear] = value
        return True

    def dequeue(self):
        if self.isEmpty():
            print("Queue underflow")
            return None
        value = self.items[self.front]
        self.items[self.front] = None
        if self.front == self.rear:        # that was the last item
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return value

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[self.front]


def reverse_with_stack(text):
    """Classic stack application: LIFO order reverses the input."""
    stack = Stack(len(text))
    for char in text:
        stack.push(char)

    reversed_text = ""
    while not stack.isEmpty():
        reversed_text += stack.pop()
    return reversed_text


def brackets_balanced(text):
    """Push openers, pop on closers and check they match."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = Stack(len(text))

    for char in text:
        if char in "([{":
            stack.push(char)
        elif char in pairs:
            if stack.isEmpty() or stack.pop() != pairs[char]:
                return False

    return stack.isEmpty()       # leftover openers mean unbalanced


def evaluate_rpn(tokens):
    """Reverse Polish Notation: operands go on the stack, operators pop two."""
    stack = Stack(len(tokens))

    for token in tokens:
        if token in "+-*/":
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.push(left + right)
            elif token == "-":
                stack.push(left - right)
            elif token == "*":
                stack.push(left * right)
            else:
                stack.push(left / right)
        else:
            stack.push(float(token))

    return stack.pop()


def hot_potato(names, count):
    """Queue application: rotate the queue, then eliminate whoever is at the front."""
    queue = CircularQueue(len(names) + 1)
    for name in names:
        queue.enqueue(name)

    while True:
        for _ in range(count):
            queue.enqueue(queue.dequeue())    # move front to the back
        eliminated = queue.dequeue()
        if queue.peek() is None:
            return eliminated
        print("  eliminated:", eliminated)


if __name__ == "__main__":
    print("--- Stack ---")
    stack = Stack(3)
    stack.push("A")
    stack.push("B")
    stack.push("C")
    stack.push("D")                  # overflow
    print("peek:    ", stack.peek())
    print("pop:     ", stack.pop())
    print("isFull:  ", stack.isFull())
    print("isEmpty: ", stack.isEmpty())

    print("\n--- Circular queue ---")
    queue = CircularQueue(3)
    queue.enqueue("Kenzo")
    queue.enqueue("Ryan")
    print("dequeue: ", queue.dequeue())
    queue.enqueue("Julian")          # wraps into the freed slot
    print("contents:", queue.items)
    print("peek:    ", queue.peek())

    print("\n--- Applications ---")
    print("reverse_with_stack: ", reverse_with_stack("stack"))
    print("balanced '{[()]}':  ", brackets_balanced("{[()]}"))
    print("balanced '{[(])}':  ", brackets_balanced("{[(])}"))
    print("RPN 3 4 + 2 *:      ", evaluate_rpn(["3", "4", "+", "2", "*"]))

    print("\nhot potato:")
    print("  winner:    ", hot_potato(["Avin", "Ryan", "Kenzo", "Julian"], 3))
