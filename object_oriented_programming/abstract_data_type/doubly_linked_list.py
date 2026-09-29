class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def display_reverse(self):
        elements = []
        current = self.tail
        while current:
            elements.append(current.data)
            current = current.prev
        return elements

my_doubly_linked_list = DoublyLinkedList()

my_doubly_linked_list.append(10)
my_doubly_linked_list.append(20)
my_doubly_linked_list.append(30)
my_doubly_linked_list.append(40)

print("Forward:", my_doubly_linked_list.display())
print("Reverse:", my_doubly_linked_list.display_reverse())