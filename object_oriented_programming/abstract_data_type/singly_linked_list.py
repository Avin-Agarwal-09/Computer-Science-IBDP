class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_value(self, target_value, data):
        current = self.head
        while current is not None:
            if current.data == target_value:
                new_node = ListNode(data)
                new_node.next = current.next
                current.next = new_node
            current = current.next
        print(f"Node with data {target_value} not found.")

    def insert_at_end(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
        current.next = new_node

class ListNode:
    def __init__(self, data=0):
        self.data = data
        self.next = None

def main():

    my_list = LinkedList()

    my_list.insert_at_end(10)
    my_list.insert_at_end(20)
    my_list.insert_at_end(30)

    print("Original linked list:")
    my_list.print_list()

    my_list.insert_at_beginning(5)

    print("After inserting 5 at the beginning:")
    my_list.print_list()

    my_list.insert_after_value(10, 15)

    print("After inserting 15 in the middle:")
    my_list.print_list()
    my_list.insert_at_end(40)

    print("After inserting 40 at the end:")
    my_list.print_list()

main()


def delete_node(self, data):
    current = self.head
    prev = None

    if current != None and current.data == data:
        self.head = current.next
        current = None
        return

    while current != None and current.data != data:
        prev = current
        current = current.next

    if current == None:
        print(f"Node with data {data} not found.")
        return

    prev.next = current.next
    current = None

def search(self, key):
    current = self.head
    while current != None:
        if current.data == key:
            return True
        current = current.next
    return False
