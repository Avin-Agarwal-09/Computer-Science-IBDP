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


# Test data
if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(20)
    linked_list.insert_at_end(30)
    linked_list.insert_after_value(20, 25)

    print("Linked list:")
    linked_list.print_list()


