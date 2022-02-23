def inOrder(self):
    data = []
    if self.root is None:
        return data

    def traverse(node):
        if node.left:
            traverse(node.left)

        data.append(node.val)
        if node.right:
            traverse(node.right)

    traverse(self.root)
    return data
