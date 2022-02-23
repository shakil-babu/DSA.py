def postOrder(node):
    if node.left:
        postOrder(node.left)
    if node.right:
        postOrder(node.right)

    print(node.val)
