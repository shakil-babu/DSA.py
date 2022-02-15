class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def addLeft(self, node):
        self.left = node

    def addRight(self, node):
        self.right = node

    def createTree(self):
        """
            2
          /   \
        7       9
       /  \      \
      1    6      8    
        """
        two = Node(2)
        seven = Node(7)
        nine = Node(9)
        two.left = seven
        two.right = nine
        one = Node(1)
        six = Node(6)
        seven.left = one
        seven.right = six
        eight = Node(8)
        nine.right = eight


if __name__ == "__main__":
    root = BinaryTree()
    print(root)
