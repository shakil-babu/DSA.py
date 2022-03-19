def treeMax(root):
    if root is None:
        return float('-inf')

    else:
        leftMax = treeMax(root.left)
        rightMax = treeMax(root.right)

        return max(root.data, leftMax, rightMax)
