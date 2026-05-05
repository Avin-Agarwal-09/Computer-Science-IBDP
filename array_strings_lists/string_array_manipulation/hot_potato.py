def hotPotato(names, k):
    queue = names[:]
    while len(queue) > 1:
        for i in range(k-1):
            queue.append(queue.pop(0))
            print(queue)
        queue.pop(0)
        print("a")
        print(queue)
    return queue[0]

names = ["Alice", "Bob", "Cathy", "Dan"]
k = 3
print(hotPotato(names, k))
