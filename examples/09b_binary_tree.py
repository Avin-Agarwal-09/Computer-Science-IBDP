"""Topic 9b - Abstract data types: binary search trees.

A binary search tree keeps every value in sorted position:
    everything in a node's LEFT subtree is smaller than the node
    everything in its RIGHT subtree is larger

                 50
               /    \\
             30      70
            /  \\    /  \\
          20   40  60   80

That invariant makes search O(log n) on a balanced tree - at each node you
discard half the remaining values, exactly like binary search.

The three traversals (examinable - know the output order of each):
    pre-order  root, left, right    - copying a tree
    in-order   left, root, right    - visits a BST in ASCENDING order
    post-order left, right, root    - deleting a tree
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_below(self.root, data)

    def _insert_below(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_below(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_below(node.right, data)
        # equal values are ignored - a BST holds no duplicates

    def search(self, target):
        current = self.root
        while current is not None:
            if target == current.data:
                return True
            elif target < current.data:
                current = current.left       # discard the right subtree
            else:
                current = current.right      # discard the left subtree
        return False

    def find_minimum(self):
        """The smallest value is the leftmost node."""
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def find_maximum(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data

    def height(self):
        return self._height_below(self.root)

    def _height_below(self, node):
        if node is None:
            return 0
        return 1 + max(self._height_below(node.left), self._height_below(node.right))

    def pre_order(self):
        values = []
        self._pre_order(self.root, values)
        return values

    def _pre_order(self, node, values):
        if node is not None:
            values.append(node.data)
            self._pre_order(node.left, values)
            self._pre_order(node.right, values)

    def in_order(self):
        values = []
        self._in_order(self.root, values)
        return values

    def _in_order(self, node, values):
        if node is not None:
            self._in_order(node.left, values)
            values.append(node.data)
            self._in_order(node.right, values)

    def post_order(self):
        values = []
        self._post_order(self.root, values)
        return values

    def _post_order(self, node, values):
        if node is not None:
            self._post_order(node.left, values)
            self._post_order(node.right, values)
            values.append(node.data)


if __name__ == "__main__":
    tree = BinarySearchTree()
    for value in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(value)

    print("pre-order:  ", tree.pre_order())
    print("in-order:   ", tree.in_order(), "<- sorted")
    print("post-order: ", tree.post_order())

    print("\nsearch 40:  ", tree.search(40))
    print("search 45:  ", tree.search(45))
    print("minimum:    ", tree.find_minimum())
    print("maximum:    ", tree.find_maximum())
    print("height:     ", tree.height())
