QueueSize = 5
Queue = [None] * QueueSize
front = -1
rear = -1

def isEmpty():
    return front == -1 and rear == -1

def isFull():
    return (rear + 1) % QueueSize == front

def enqueue(value):
    global front,rear
    if isFull():
        print("Queue Overflow")
    else:
        if front == -1:
            front = 0
        rear = (rear+1) % QueueSize
        Queue[rear] = value
        print(f"Enqueued: {value}")

def dequeue():
    global front, rear
    if isEmpty():
        print("Queue Underflow")
        return None
    else:
        value = Queue[front]
        Queue[front] = None
        if front == rear:
            front = rear = -1
        else:
            front = (front + 1) % QueueSize
        print(f"Dequeued: {value}")
        return value


enqueue("Kenzo")
enqueue("Ryan")
print(Queue)
dequeue()
print(Queue)