def existsInTree(root, val):
    if root is None:
        return False

    else:
        inLeft = existsInTree(root.left, val)
        inRight = existsInTree(root.right, val)

        return root.data == val or inLeft or inRight 
