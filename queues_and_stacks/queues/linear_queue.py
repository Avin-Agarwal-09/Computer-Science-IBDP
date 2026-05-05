QueueSize = 5
Queue = [None] * QueueSize
front = -1
rear = -1

def isEmpty():
    return front == -1 and rear == -1

def isFull():
    return rear == QueueSize -1

def enqueue(value):
    global front,rear
    if isFull():
        print("Queue Overflow")
    else:
        if isEmpty():
            front = 0
            rear += 1
            Queue[rear] = value
            print(f"Enqueued: {value}")

def dequeue():
    global front, rear
    if isEmpty():
        print("Queue Unferflow")
        return None
    else:
        value = Queue[front]
        if front == rear:
            front = -1
            rear = -1

enqueue("Kenzo")
enqueue("Ryan")
print(Queue)
dequeue()
print(Queue)