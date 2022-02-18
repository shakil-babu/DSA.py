class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node
            return
        else:
            current = self.root
            while True:
                if val == current.val:
                    return
                if current.val < val:
                    if current.right is None:
                        current.right = node
                        return
                    else:
                        current = current.right

                elif current.val > val:
                    if current.left is None:
                        current.left = node
                        return
                    else:
                        current = current.left

    def BFS(self):
        if self.root is None:
            return []

        data = []
        queue = [self.root]
        while len(queue):
            current = queue.pop(0)
            data.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return data

    def DFSinOrder(self):
        if self.root is None:
            return []
        data = []

        def traverse(root):
            if root.left:
                traverse(root.left)
            data.append(root.val)
            if root.right:
                traverse(root.right)
        traverse(self.root)

        return data


# initialization
"""
                       10
                      /  \
                     8    15
                    / \   / \
                   5   9 13  20
  
  
"""

tree = BinarySearchTree()
tree.insert(10)
tree.insert(8)
tree.insert(15)
tree.insert(5)
tree.insert(9)
tree.insert(13)
tree.insert(20)

print(tree.DFSinOrder())
