def inOrder(node):
    if node.left:
        inOrder(node.left)
    print(node.val)
    if node.right:
        inOrder(node.right)
