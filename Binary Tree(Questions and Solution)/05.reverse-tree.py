def reverseTree(root):
    if root is None:
        return

    else:
        reverseTree(root.left)
        reverseTree(root.right)
        root.left, root.right = root.right, root.left
