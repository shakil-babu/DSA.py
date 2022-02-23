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
