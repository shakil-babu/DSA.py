def postOrder(self):
    data = []
    if self.root is None:
        return data

    def traverse(node):
        if node.left:
            traverse(node.left)
        if node.right:
            traverse(node.right)

        data.append(node.val)
    traverse(self.root)
    return data
