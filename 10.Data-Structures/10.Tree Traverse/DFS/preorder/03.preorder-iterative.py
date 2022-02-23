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
