class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        elements = []
        if not self.head:
            return elements
        current = self.head
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break
        return elements

my_circular_singly_linked_list = CircularSinglyLinkedList()

my_circular_singly_linked_list.append(10)
my_circular_singly_linked_list.append(20)
my_circular_singly_linked_list.append(30)
my_circular_singly_linked_list.append(40)

print("Circular Singly Linked List:", my_circular_singly_linked_list.display())