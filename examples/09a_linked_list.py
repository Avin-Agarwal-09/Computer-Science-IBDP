"""Topic 9a - Abstract data types: linked lists.

A linked list stores each value in a NODE that also holds a pointer to the
next node. The list itself only knows where the head is; the last node points
to None.

              head
               |
             [10|*]-->[25|*]-->[30|/]

vs an array:  insertion/deletion is O(1) once you are at the right node
              (no shuffling), but you cannot jump to index n - you must
              traverse from the head, so access is O(n).
"""


class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = ListNode(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:      # walk to the last node
            current = current.next
        current.next = new_node

    def insert_after_value(self, target, data):
        """Insert directly after the FIRST node holding target."""
        current = self.head
        while current is not None:
            if current.data == target:
                new_node = ListNode(data)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next

        print(f"Node with data {target} not found.")
        return False

    def delete(self, target):
        """Deleting means pointing the previous node past the doomed one."""
        current = self.head
        previous = None

        while current is not None:
            if current.data == target:
                if previous is None:         # deleting the head
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next

        return False

    def search(self, target):
        """Return the position of target, or -1. Traversal only - no indexing."""
        current = self.head
        position = 0
        while current is not None:
            if current.data == target:
                return position
            current = current.next
            position += 1
        return -1

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def to_list(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return values

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(20)
    linked_list.insert_at_end(30)
    linked_list.insert_after_value(20, 25)

    print("Linked list:")
    linked_list.print_list()

    print("length:       ", linked_list.length())
    print("search 25:    ", linked_list.search(25))
    print("search 99:    ", linked_list.search(99))

    linked_list.delete(20)
    print("after delete: ", linked_list.to_list())

    linked_list.insert_after_value(99, 1)     # not found
    print("is_empty:     ", linked_list.is_empty())
