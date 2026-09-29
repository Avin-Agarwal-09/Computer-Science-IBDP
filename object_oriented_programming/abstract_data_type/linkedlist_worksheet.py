class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def delete_value(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next



def reverse(self):
    prev = None #tracking the previous node         
    current = self.head #will start looking from the start of the list

    while current: #start of the loop
        next_node = current.next #saving the next node before overwitign
        current.next = prev #reverse the pointer
        prev = current   #move the previous pointer forward to the one that is currently being accessed
        current = next_node    # move current to the node that was saved   

    self.head = prev #the old tail becomes the new head