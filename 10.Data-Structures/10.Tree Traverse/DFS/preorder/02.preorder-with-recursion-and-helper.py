def preorderDFS(self):
    data = []
    if self.root is None:
        return data

    def traverse(node):
        data.append(node.val)
        if node.left:
            traverse(node.left)
        if node.right:
            traverse(node.right)

    traverse(self.root)
    return data
