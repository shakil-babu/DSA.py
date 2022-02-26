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

    def preorderIterative(self):

        # return if the tree is empty
        if self.root is None:
            return

        # create an empty stack and push the root node
        stack = []
        stack.append(self.root)

        # loop till stack is empty
        while stack:

            # pop a node from the stack and print it
            curr = stack.pop()

            print(curr.val, end=' ')

            # push the right child of the popped node into the stack
            if curr.right:
                stack.append(curr.right)

            # push the left child of the popped node into the stack
            if curr.left:
                stack.append(curr.left)

    # Iterative function to perform postorder traversal on the tree

    def postorderIterative(self):

        # return if the tree is empty
        if self.root is None:
            return

        # create an empty stack and push the root node
        stack = []
        stack.append(self.root)

        # create another stack to store postorder traversal
        out = []

        # loop till stack is empty
        while stack:

            # pop a node from the stack and push the data into the output stack
            curr = stack.pop()
            out.append(curr.val)

            # push the left and right child of the popped node into the stack
            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)

        # print postorder traversal
        while out:
            print(out.pop(), end=' ')

    # Iterative function to perform inorder traversal on the tree

    def inorderIterative(self):

        # create an empty stack
        stack = []

        # start from the root node (set current node to the root node)
        curr = self.root

        # if the current node is None and the stack is also empty, we are done
        while stack or curr:

            # if the current node exists, push it into the stack (defer it)
            # and move to its left child
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                # otherwise, if the current node is None, pop an element from the stack,
                # print it, and finally set the current node to its right child
                curr = stack.pop()
                print(curr.val, end=' ')

                curr = curr.right

    def BFS_average(self):
        if self.root is None:
            return []

        data = []
        queue = [self.root]
        while len(queue):
            hegith = []
            length = len(queue)
            for i in range(length):
                current = queue.pop(0)
                hegith.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            data.append(hegith)

        ans = []
        for item in data:
            avg = sum(item) / len(item)
            ans.append(avg)

        return ans


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


print(tree.average())
