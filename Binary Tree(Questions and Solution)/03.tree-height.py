def treeHeight(root):
    if root is None:
        return float('-inf')

    else:
        leftHeight = treeHeight(root.left)
        rightHeight = treeHeight(root.right)

        return 1 + max(leftHeight, rightHeight)
